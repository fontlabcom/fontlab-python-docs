#!/usr/bin/env bash
# this_file: scripts/pages-build.sh
# Source-bearing diagnostics never reach public Actions logs or artifacts.
set -euo pipefail
umask 077
: "${DOCS_PRIVATE_RUNTIME:?Private ephemeral runtime is required}"
: "${SOURCE_DATE_EPOCH:?Source X timestamp must be preserved in both jobs}"
store=${1:?Private input checkout is required}
mkdir -p "$DOCS_PRIVATE_RUNTIME"
exec 3>&1
exec >>"$DOCS_PRIVATE_RUNTIME/build.log" 2>&1
trap 'code=$?; if (( code )); then printf "::error::Complete documentation gate failed; private diagnostics withheld.\n" >&3; fi' EXIT
export UV_PROJECT_ENVIRONMENT="$DOCS_PRIVATE_RUNTIME/environment"
export UV_CACHE_DIR="$DOCS_PRIVATE_RUNTIME/uv-cache"
export PLAYWRIGHT_BROWSERS_PATH="$DOCS_PRIVATE_RUNTIME/browsers"
export PYTHONDONTWRITEBYTECODE=1
uv sync --locked --group dev
uv run --no-sync python -m scripts.pages_inputs prepare "$store" "$DOCS_PRIVATE_RUNTIME"
export FONTLAB_API_SOURCE_ROOT="$DOCS_PRIVATE_RUNTIME/inputs/packages"
export FONTLAB_EXAMPLES_EXPORT="$DOCS_PRIVATE_RUNTIME/inputs/examples"
export PYTHONPATH="$FONTLAB_API_SOURCE_ROOT"
export FONTLAB_REQUIRE_CONSUMER=1
uv run --no-sync python -m playwright install --with-deps chromium
./scripts/accept-consumer.sh --offline
uv run --no-sync python -B -m pytest -q -rs -p no:cacheprovider tests
node --test scripts/search_backend/tests.cjs
uv run --no-sync python scripts/a11y_check.py --site .build/site --out "$DOCS_PRIVATE_RUNTIME/a11y.json"
uv run --no-sync python -m scripts.interaction_check --site .build/site --out "$DOCS_PRIVATE_RUNTIME/interaction.json"
./build.sh --check --offline
raw_exit=0
uv run --no-sync python -m scripts.pages_inputs capture .build/site "$DOCS_PRIVATE_RUNTIME/audit" "$DOCS_PRIVATE_RUNTIME/release-audit.json" || raw_exit=$?
printf '%s\n' "$raw_exit" > "$DOCS_PRIVATE_RUNTIME/release-audit.exit"
uv run --no-sync python -m scripts.pages_inputs disposition "$DOCS_PRIVATE_RUNTIME/release-audit.json" "$raw_exit"
printf 'Complete frozen-input documentation, Python, Node, search, accessibility and interaction gates passed; release audit retains reviewed exit 1.\n' >&3
