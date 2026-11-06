#!/usr/bin/env bash
# this_file: scripts/accept-consumer.sh
# Required build-plus-browser gate: absent inputs/browser are failures.
set -euo pipefail
umask 077
cd "$(dirname "$0")/.."
# Preserve the Pages helper's public stream; standalone use falls back to stdout.
if ! { true >&3; } 2>/dev/null; then exec 3>&1; fi
current_stage=dependencies
diagnostics=
trap 'code=$?; if [[ -n "$diagnostics" ]]; then rm -f "$diagnostics/report.xml"; rmdir "$diagnostics"; fi; if (( code )); then printf "Consumer stage %s failed (exit %s); private diagnostics withheld.\n" "$current_stage" "$code" >&3; fi' EXIT
stage() {
    current_stage=$1
    printf 'Consumer stage: %s\n' "$current_stage" >&3
}
stage dependencies
uv sync --locked
stage browser
uv run --no-sync python -m playwright install chromium
stage build
./build.sh "$@"
stage full-index
diagnostics=$(mktemp -d "${TMPDIR:-/tmp}/docs-consumer.XXXXXX")
consumer_exit=0
FONTLAB_REQUIRE_CONSUMER=1 uv run --no-sync python -m pytest -q -s tests/test_search_identities.py -k full_index --junitxml="$diagnostics/report.xml" || consumer_exit=$?
if (( consumer_exit )); then
    uv run --no-sync python - "$diagnostics/report.xml" >&3 <<'PY' || true
import re
import sys
import xml.etree.ElementTree as ET

try:
    report = ET.parse(sys.argv[1])
except (OSError, ET.ParseError):
    print("Consumer pytest failure: unavailable")
else:
    allowed = {"AssertionError", "Error", "TimeoutError", "Failed", "ImportError",
               "ModuleNotFoundError", "RuntimeError", "MemoryError", "OSError",
               "ValueError", "KeyError", "StopIteration"}
    for failure in report.iter():
        if failure.tag not in {"failure", "error"}:
            continue
        # Only the fixed test's decimal line and an allowlisted class can escape.
        text = failure.text or ""
        lines = re.findall(r"^tests/test_search_identities\.py:([0-9]+):", text, re.MULTILINE)
        names = re.findall(r"^E\s+([\w.]+):", text, re.MULTILINE)
        line, name = lines[-1] if lines else "0", names[-1] if names else "unknown"
        category = name.rsplit(".", 1)[-1]
        category = category if category in allowed else "unknown"
        print(f"Consumer pytest failure: class={category} line={int(line)}")
PY
    exit "$consumer_exit"
fi
stage complete
