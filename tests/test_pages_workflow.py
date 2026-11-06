# this_file: tests/test_pages_workflow.py
"""Trusted-main routing, immutable inputs, epoch transfer and private diagnostics."""

import os
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
STAGES = (
    "environment", "inputs", "browser", "consumer", "python-tests", "node-tests",
    "accessibility", "interaction", "accepted-check", "release-audit",
    "audit-disposition", "complete",
)


def test_workflow_when_every_main_push_then_x_y_rebuild_same_frozen_inputs():
    workflow = yaml.load((ROOT / ".github/workflows/docs.yml").read_text(), Loader=yaml.BaseLoader)
    assert workflow["on"] == {"push": {"branches": ["main"]}}
    assert workflow["permissions"] == {"contents": "read"}
    jobs = workflow["jobs"]
    assert set(jobs) == {"build", "qualify-generated-output"}
    assert "github.ref == 'refs/heads/main'" in jobs["build"]["if"]
    paths, epochs = [], []
    for name, job in jobs.items():
        private = [step for step in job["steps"] if step.get("with", {}).get("repository") == "fontlabcom/fontlab-python-docs-inputs"]
        assert len(private) == 1
        settings = private[0]["with"]
        assert settings["ref"] == "688dbac51848d8a58b81f2cd8b3d0270385ddd9e"
        assert settings["ssh-key"] == "${{ secrets.DOCS_INPUTS_SSH_KEY }}"
        assert settings["ssh-strict"] == "true" and settings["persist-credentials"] == "false"
        assert settings["fetch-depth"] == "1" and settings["submodules"] == "false"
        gates = [step for step in job["steps"] if "pages-build.sh" in step.get("run", "")]
        assert len(gates) == 1
        paths.append(gates[0]["env"]["DOCS_PRIVATE_RUNTIME"])
        epochs.append(gates[0]["env"]["SOURCE_DATE_EPOCH"])
        for step in job["steps"]:
            if "uses" in step:
                assert len(step["uses"].split("@")[1]) == 40
        assert not any("upload-artifact" in step.get("uses", "") or "actions/cache" in step.get("uses", "") for step in job["steps"])
    assert paths[0] == paths[1], "Absolute private input locations are part of accepted config provenance"
    assert epochs == ["${{ steps.epoch.outputs.value }}", "${{ needs.build.outputs.epoch }}"]
    y = jobs["qualify-generated-output"]
    assert y["permissions"] == {"contents": "read", "pages": "write"}
    assert y["steps"][0]["with"]["ref"] == "${{ needs.build.outputs.sha }}"
    assert "lineage" in y["steps"][1]["run"], "Y source identity must precede secret access"
    assert any("pages_publish pages" in step.get("run", "") for step in y["steps"])


def test_private_build_when_tool_prints_source_then_public_log_is_sanitized(tmp_path):
    binary = tmp_path / "bin"
    binary.mkdir()
    uv = binary / "uv"
    uv.write_text("#!/bin/sh\nprintf 'PRIVATE-SOURCE-SENTINEL\\n'\nexit 7\n")
    uv.chmod(0o755)
    private = tmp_path / "private"
    result = subprocess.run(["bash", str(ROOT / "scripts/pages-build.sh"), str(tmp_path / "store")],
                            cwd=ROOT, capture_output=True, text=True,
                            env=os.environ | {"PATH": str(binary) + os.pathsep + os.environ["PATH"],
                                              "DOCS_PRIVATE_RUNTIME": str(private), "SOURCE_DATE_EPOCH": "1700000000"})
    assert result.returncode == 7
    assert "PRIVATE-SOURCE-SENTINEL" not in result.stdout + result.stderr
    assert "private diagnostics withheld" in result.stdout
    assert "stage environment failed (exit 7)" in result.stdout
    assert "PRIVATE-SOURCE-SENTINEL" in (private / "build.log").read_text()
    assert private.stat().st_mode & 0o077 == 0
    assert (private / "build.log").stat().st_mode & 0o077 == 0


@pytest.fixture
def private_gate(tmp_path):
    project = tmp_path / "project"
    (project / "scripts").mkdir(parents=True)
    binary = tmp_path / "bin"
    binary.mkdir()
    driver = f"#!{sys.executable}\n" + '''import os,sys
from pathlib import Path
args=sys.argv[1:]
name=Path(sys.argv[0]).name
if name=='uv':
    if args[0]=='sync': stage='environment'
    elif 'prepare' in args: stage='inputs'
    elif 'playwright' in args: stage='browser'
    elif 'pytest' in args: stage='python-tests'
    elif 'scripts/a11y_check.py' in args: stage='accessibility'
    elif 'scripts.interaction_check' in args: stage='interaction'
    elif 'capture' in args: stage='release-audit'
    elif 'disposition' in args: stage='audit-disposition'
    else: raise SystemExit(99)
elif name=='node': stage='node-tests'
elif name=='accept-consumer.sh': stage='consumer'
else: stage='accepted-check'
print('PRIVATE-SOURCE-SENTINEL',stage,args)
if os.environ.get('CI_TEST_FAIL_STAGE')==stage: raise SystemExit(7)
if stage=='release-audit': raise SystemExit(int(os.environ['CI_TEST_AUDIT_EXIT']))
if stage=='audit-disposition' and args[-1]!='1': raise SystemExit(23)
'''
    for path in (binary / "uv", binary / "node", project / "build.sh", project / "scripts/accept-consumer.sh"):
        path.write_text(driver)
        path.chmod(0o755)

    def run(fail_stage="", audit_exit="1"):
        private = tmp_path / "PRIVATE-SOURCE-SENTINEL-runtime"
        store = tmp_path / "PRIVATE-SOURCE-SENTINEL-store"
        result = subprocess.run(
            ["bash", str(ROOT / "scripts/pages-build.sh"), str(store)], cwd=project,
            capture_output=True, text=True,
            env=os.environ | {"PATH": str(binary) + os.pathsep + os.environ["PATH"],
                              "DOCS_PRIVATE_RUNTIME": str(private), "SOURCE_DATE_EPOCH": "1700000000",
                              "CI_TEST_FAIL_STAGE": fail_stage, "CI_TEST_AUDIT_EXIT": audit_exit},
        )
        assert "PRIVATE-SOURCE-SENTINEL" not in result.stdout + result.stderr
        assert str(private) not in result.stdout + result.stderr
        assert "PRIVATE-SOURCE-SENTINEL" in (private / "build.log").read_text()
        return result, private

    return run


@pytest.mark.parametrize("stage", [value for value in STAGES[:-1] if value != "release-audit"])
def test_private_build_when_stage_fails_then_reports_only_static_stage_and_exit(private_gate, stage):
    result, _ = private_gate(fail_stage=stage)
    assert result.returncode == 7
    assert f"stage {stage} failed (exit 7)" in result.stdout
    assert "Documentation stage: complete" not in result.stdout


def test_private_build_when_all_stages_pass_then_expected_audit_one_reaches_disposition(private_gate):
    result, private = private_gate()
    assert result.returncode == 0, result.stdout + result.stderr
    stages = [line.removeprefix("Documentation stage: ") for line in result.stdout.splitlines()
              if line.startswith("Documentation stage: ")]
    assert stages == list(STAGES)
    assert "Documentation release-audit exit: 1" in result.stdout
    assert (private / "release-audit.exit").read_text() == "1\n"
    assert "::error::" not in result.stdout


def test_private_build_when_audit_exit_is_unexpected_then_disposition_still_fails(private_gate):
    result, private = private_gate(audit_exit="7")
    assert result.returncode == 23
    assert "Documentation release-audit exit: 7" in result.stdout
    assert "stage audit-disposition failed (exit 23)" in result.stdout
    assert (private / "release-audit.exit").read_text() == "7\n"
