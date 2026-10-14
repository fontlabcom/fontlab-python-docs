# this_file: tests/test_docs_workflow.py
"""CI must provision sibling private sources and run every acceptance gate."""

from pathlib import Path

import yaml


def test_workflow_when_loaded_then_provisions_sources_and_required_gates():
    root = Path(__file__).resolve().parents[1]
    workflow = yaml.load(
        (root / ".github/workflows/docs.yml").read_text(), Loader=yaml.BaseLoader
    )
    assert set(workflow["on"]) == {"push", "pull_request"}, (
        "Both docs event types are required"
    )
    job = workflow["jobs"]["docs"]
    assert job["runs-on"] == "ubuntu-latest", "Acceptance runs on Ubuntu"
    steps = job["steps"]
    checkouts = [
        step["with"] for step in steps if step.get("uses") == "actions/checkout@v4"
    ]
    assert len(checkouts) == 10, "Docs and all nine producer checkouts must be present"
    assert {item["path"] for item in checkouts} == {
        "fontlab-python-docs",
        "fontlab-echopy",
        "pythonqtside",
        "fontlab-glyport",
        "typerig-lib",
        "fontlab-remopy",
        "fontlab-fontlabapp",
        "fontlab-grablab",
        "fontlab-fly",
        "fontlab-aidus-code",
    }, "Checkout paths must match the source planner's sibling directories"
    for item in checkouts[1:]:
        assert item["repository"] == "fontlabcom/" + item["path"], (
            "Use the producer origin"
        )
        if item["path"] != "typerig-lib":
            assert item["token"] == "${{ secrets.FONTLAB_DOCS_READ_TOKEN }}", (
                "Private sources require the read secret"
            )
        assert item["persist-credentials"] == "false", (
            "Do not retain checkout credentials"
        )
    commands = [step["run"] for step in steps if "run" in step]
    assert commands == [
        "uv sync --locked",
        "uv run --no-sync python -m playwright install --with-deps chromium",
        "uv run --frozen python -m pytest -q tests",
        "./scripts/accept-consumer.sh",
        "./build.sh --check",
        "uv run --no-sync python scripts/a11y_check.py --site .build/site --out a11y.json",
    ], "Run all gates in order with first-run network provisioning"
    assert not any(step.get("continue-on-error") for step in steps), (
        "Failures must fail CI"
    )
    uploads = [
        step for step in steps if step.get("uses") == "actions/upload-artifact@v4"
    ]
    assert len(uploads) == 2 and all(step["if"] == "always()" for step in uploads), (
        "Keep failure receipts and site artifacts"
    )
