#!/usr/bin/env bash
# this_file: scripts/accept-consumer.sh
# Required build-plus-browser gate: absent inputs/browser are failures.
set -euo pipefail
cd "$(dirname "$0")/.."
uv sync --locked
uv run --no-sync python -m playwright install chromium
./build.sh "$@"
FONTLAB_REQUIRE_CONSUMER=1 uv run --no-sync python -m pytest -q -s tests/test_search_identities.py -k full_index
