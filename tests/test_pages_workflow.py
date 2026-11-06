# this_file: tests/test_pages_workflow.py
"""Trusted-main routing, immutable inputs, epoch transfer and private diagnostics."""

import os
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


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
    assert "PRIVATE-SOURCE-SENTINEL" in (private / "build.log").read_text()
    assert private.stat().st_mode & 0o077 == 0
    assert (private / "build.log").stat().st_mode & 0o077 == 0
