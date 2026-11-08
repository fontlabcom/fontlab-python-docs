# this_file: tests/test_pages_workflow.py
"""Trusted-main routing, immutable inputs, epoch transfer and private diagnostics."""

import os
import json
import hashlib
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
    (project / "scripts/archive_search").mkdir()
    for name in ("package.json", "package-lock.json"):
        (project / "scripts/archive_search" / name).write_text('{}')
    binary = tmp_path / "bin"
    binary.mkdir()
    driver = f"#!{sys.executable}\n" + '''import os,sys,json
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
elif name in {'node','npm'}: stage='node-tests'
elif name=='accept-consumer.sh': stage='consumer'
else: stage='accepted-check'
print('PRIVATE-SOURCE-SENTINEL',stage,args)
command='compiler' if name=='npm' else ('root-node' if name=='node' and args[-1]=='scripts/search_backend/tests.cjs' else 'ui-node' if name=='node' and args[-1]=='scripts/archive_search/tests-ui.cjs' else 'archive-node' if name=='node' else stage)
with open(os.environ['CI_TEST_CALLS'],'a') as log: log.write(json.dumps({'command':command,'name':name,'args':args})+'\\n')
if os.environ.get('CI_TEST_FAIL_COMMAND')==command: raise SystemExit(8)
if os.environ.get('CI_TEST_FAIL_STAGE')==stage: raise SystemExit(7)
if stage=='release-audit': raise SystemExit(int(os.environ['CI_TEST_AUDIT_EXIT']))
if stage=='audit-disposition' and args[-1]!='1': raise SystemExit(23)
'''
    for path in (binary / "uv", binary / "node", binary / "npm", project / "build.sh", project / "scripts/accept-consumer.sh"):
        path.write_text(driver)
        path.chmod(0o755)

    def run(fail_stage="", audit_exit="1", fail_command=""):
        private = tmp_path / "PRIVATE-SOURCE-SENTINEL-runtime"
        store = tmp_path / "PRIVATE-SOURCE-SENTINEL-store"
        calls = tmp_path / "calls.jsonl"
        command = [os.environ.get("ARCHIVE_SHELL_BASH", "bash"), str(ROOT / "scripts/pages-build.sh"), str(store)]
        env = os.environ | {"PATH": str(binary) + os.pathsep + os.environ["PATH"],
                              "DOCS_PRIVATE_RUNTIME": str(private), "SOURCE_DATE_EPOCH": "1700000000",
                              "CI_TEST_FAIL_STAGE": fail_stage, "CI_TEST_AUDIT_EXIT": audit_exit,
                              "CI_TEST_FAIL_COMMAND": fail_command, "CI_TEST_CALLS": str(calls)}
        trace = tmp_path / "trace"
        with trace.open("w") as stream:
            if os.environ.get("ARCHIVE_SHELL_EVIDENCE"):
                env.update(BASH_XTRACEFD=str(stream.fileno()), PS4='+${BASH_SOURCE}:${LINENO}: ')
                command.insert(1, "-x")
            result = subprocess.run(command, cwd=project, capture_output=True, text=True, env=env, pass_fds=(stream.fileno(),))
        if os.environ.get("ARCHIVE_SHELL_EVIDENCE"):
            evidence = Path(os.environ["ARCHIVE_SHELL_EVIDENCE"])
            evidence.mkdir(parents=True, exist_ok=True)
            label = f"{fail_stage or 'success'}-{audit_exit}-{fail_command or 'none'}"
            (evidence / (label + ".trace")).write_bytes(trace.read_bytes())
            (evidence / (label + ".json")).write_text(json.dumps({"exit": result.returncode,
                "script_sha256": hashlib.sha256((ROOT / "scripts/pages-build.sh").read_bytes()).hexdigest(),
                "calls": [json.loads(line) for line in calls.read_text().splitlines()],
                "stdout": result.stdout, "stderr": result.stderr}, indent=2))
        assert "PRIVATE-SOURCE-SENTINEL" not in result.stdout + result.stderr
        assert str(private) not in result.stdout + result.stderr
        assert "PRIVATE-SOURCE-SENTINEL" in (private / "build.log").read_text()
        assert private.stat().st_mode & 0o077 == 0
        assert (private / "build.log").stat().st_mode & 0o077 == 0
        if not fail_stage and not fail_command:
            invoked = [json.loads(line) for line in calls.read_text().splitlines()]
            compiler = next(row for row in invoked if row["command"] == "compiler")
            assert compiler["args"] == ["ci", "--prefix", ".build/archive-compiler", "--ignore-scripts", "--no-audit", "--no-fund"]
            assert (project / ".build/archive-compiler/package.json").read_text() == '{}'
            assert (project / ".build/archive-compiler/package-lock.json").read_text() == '{}'
            names = [row["command"] for row in invoked]
            assert names[names.index("compiler"):names.index("ui-node") + 1] == ["compiler", "root-node", "archive-node", "ui-node"]
        if fail_command:
            invoked = [json.loads(line) for line in calls.read_text().splitlines()]
            assert invoked[-1]["command"] == fail_command
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


def test_private_build_when_audit_is_green_then_existing_disposition_rejects_zero(private_gate):
    result, private = private_gate(audit_exit="0")
    assert result.returncode == 23
    assert (private / "release-audit.exit").read_text() == "0\n"


@pytest.mark.parametrize("command", ["compiler", "root-node", "archive-node", "ui-node"])
def test_private_build_when_each_distinct_node_command_fails_then_later_commands_do_not_run(private_gate, command):
    result, _ = private_gate(fail_command=command)
    assert result.returncode == 8
    assert "stage node-tests failed (exit 8)" in result.stdout
    assert "Documentation stage: complete" not in result.stdout


@pytest.mark.parametrize("missing", ["DOCS_PRIVATE_RUNTIME", "SOURCE_DATE_EPOCH", "store"])
@pytest.mark.parametrize("empty", [False, True])
def test_private_build_when_required_input_is_absent_or_empty_then_fails_before_dependent_steps(tmp_path, missing, empty):
    env = os.environ | {"DOCS_PRIVATE_RUNTIME": str(tmp_path / "runtime"), "SOURCE_DATE_EPOCH": "1700000000"}
    command = [os.environ.get("ARCHIVE_SHELL_BASH", "bash"), str(ROOT / "scripts/pages-build.sh")]
    if missing != "store":
        command.append(str(tmp_path / "store"))
        env.pop(missing)
        if empty:
            env[missing] = ""
    elif empty:
        command.append("")
    trace = tmp_path / "trace"
    with trace.open("w") as stream:
        if os.environ.get("ARCHIVE_SHELL_EVIDENCE"):
            env.update(BASH_XTRACEFD=str(stream.fileno()), PS4='+${BASH_SOURCE}:${LINENO}: ')
            command.insert(1, "-x")
        result = subprocess.run(command, cwd=tmp_path, capture_output=True, text=True, env=env, pass_fds=(stream.fileno(),))
    assert result.returncode != 0
    assert (missing if missing != "store" else "Private input checkout is required") in result.stderr
    assert "Documentation stage:" not in result.stdout
    assert not (tmp_path / "runtime").exists()
    if os.environ.get("ARCHIVE_SHELL_EVIDENCE"):
        evidence = Path(os.environ["ARCHIVE_SHELL_EVIDENCE"])
        evidence.mkdir(parents=True, exist_ok=True)
        label = f"required-{missing}-{'empty' if empty else 'absent'}"
        (evidence / (label + ".trace")).write_bytes(trace.read_bytes())
        (evidence / (label + ".json")).write_text(json.dumps({"exit": result.returncode, "stdout": result.stdout, "stderr": result.stderr,
            "script_sha256": hashlib.sha256((ROOT / "scripts/pages-build.sh").read_bytes()).hexdigest()}, indent=2))


@pytest.fixture
def consumer_gate(tmp_path):
    project = tmp_path / "PRIVATE-SOURCE-SENTINEL-project"
    (project / "scripts").mkdir(parents=True)
    (project / "tests").mkdir()
    consumer = project / "scripts/accept-consumer.sh"
    consumer.write_bytes((ROOT / "scripts/accept-consumer.sh").read_bytes())
    (project / "tests/consumer_error.py").write_text(
        "from playwright.sync_api import Error\n"
        "def fail(): raise Error('PRIVATE-SOURCE-SENTINEL')\n"
    )
    (project / "tests/test_search_identities.py").write_text(
        "import os\nfrom consumer_error import fail\n"
        "def test_full_index():\n"
        "    print('PRIVATE-SOURCE-SENTINEL')\n"
        "    kind = os.environ.get('CI_TEST_EXCEPTION', '')\n"
        "    if kind == 'assertion': assert False, 'PRIVATE-SOURCE-SENTINEL'\n"
        "    if kind == 'playwright': fail()\n"
        "    if kind == 'unknown': raise Exception('PRIVATE-SOURCE-SENTINEL')\n"
    )
    binary = tmp_path / "bin"
    binary.mkdir()
    driver = f"#!{sys.executable}\n" + '''import os,sys,subprocess
from pathlib import Path
args=sys.argv[1:]
if Path(sys.argv[0]).name=='build.sh': stage='build'
elif args[0]=='sync': stage='dependencies'
elif 'playwright' in args: stage='browser'
elif 'pytest' in args: stage='full-index'
else:
    index=args.index('python')
    os.execv(sys.executable,[sys.executable,*args[index+1:]])
print('PRIVATE-SOURCE-SENTINEL',stage,args,flush=True)
if os.environ.get('CI_TEST_FAIL_STAGE')==stage: raise SystemExit(7)
if stage=='full-index':
    report=Path(next(arg.split('=',1)[1] for arg in args if arg.startswith('--junitxml=')))
    assert report.parent.stat().st_mode & 0o077 == 0
    if os.environ.get('CI_TEST_MALFORMED_XML')=='1':
        report.write_text('<PRIVATE-SOURCE-SENTINEL')
        raise SystemExit(9)
    index=args.index('python')
    code=subprocess.run([sys.executable,*args[index+1:]]).returncode
    assert report.stat().st_mode & 0o077 == 0
    raise SystemExit(code)
'''
    for path in (binary / "uv", project / "build.sh"):
        path.write_text(driver)
        path.chmod(0o755)
    private_tmp = tmp_path / "PRIVATE-SOURCE-SENTINEL-tmp"
    private_tmp.mkdir()

    def run(fail_stage="", exception="", public_fd=True, malformed_xml=False):
        log = tmp_path / "PRIVATE-SOURCE-SENTINEL.log"
        wrapper = 'exec 3>&1; exec >"$1" 2>&1; exec bash "$2" --offline'
        command = ["bash", "-c", wrapper, "consumer-test", str(log), str(consumer)]
        if not public_fd:
            command = ["bash", str(consumer), "--offline"]
        result = subprocess.run(command, cwd=project, capture_output=True, text=True,
                                env=os.environ | {"PATH": str(binary) + os.pathsep + os.environ["PATH"],
                                                  "TMPDIR": str(private_tmp), "CI_TEST_FAIL_STAGE": fail_stage,
                                                  "CI_TEST_EXCEPTION": exception,
                                                  "CI_TEST_MALFORMED_XML": str(int(malformed_xml))})
        if public_fd:
            assert "PRIVATE-SOURCE-SENTINEL" not in result.stdout + result.stderr
            assert "PRIVATE-SOURCE-SENTINEL" in log.read_text()
        assert not list(private_tmp.iterdir()), "Ephemeral JUnit diagnostics must be removed"
        return result

    return run


@pytest.mark.parametrize("stage", ["dependencies", "browser", "build", "full-index"])
def test_consumer_when_substep_fails_then_static_stage_and_original_exit_are_public(consumer_gate, stage):
    result = consumer_gate(fail_stage=stage)
    assert result.returncode == 7
    assert f"Consumer stage {stage} failed (exit 7)" in result.stdout
    assert "Consumer stage: complete" not in result.stdout
    if stage == "full-index":
        assert "Consumer pytest failure: unavailable" in result.stdout


@pytest.mark.parametrize("exception,classification,line", [
    ("assertion", "AssertionError", 6), ("playwright", "Error", 7), ("unknown", "unknown", 8),
])
def test_consumer_when_real_pytest_fails_then_only_allowlisted_class_and_line_escape(consumer_gate, exception, classification, line):
    result = consumer_gate(exception=exception)
    assert result.returncode == 1
    assert f"Consumer pytest failure: class={classification} line={line}" in result.stdout
    assert "Consumer stage full-index failed (exit 1)" in result.stdout


def test_consumer_when_junit_is_malformed_then_diagnostics_are_withheld_deleted_and_exit_preserved(consumer_gate):
    result = consumer_gate(malformed_xml=True)
    assert result.returncode == 9
    assert "Consumer pytest failure: unavailable" in result.stdout
    assert "Consumer stage full-index failed (exit 9)" in result.stdout


@pytest.mark.parametrize("public_fd", [True, False])
def test_consumer_when_passes_then_all_substeps_run_with_or_without_inherited_fd(consumer_gate, public_fd):
    result = consumer_gate(public_fd=public_fd)
    assert result.returncode == 0, result.stdout + result.stderr
    stages = [line.removeprefix("Consumer stage: ") for line in result.stdout.splitlines()
              if line.startswith("Consumer stage: ")]
    assert stages == ["dependencies", "browser", "build", "full-index", "complete"]
    assert "Consumer pytest failure:" not in result.stdout
