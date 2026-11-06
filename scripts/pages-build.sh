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
current_stage=environment
trap 'code=$?; if (( code )); then printf "::error::Complete documentation stage %s failed (exit %s); private diagnostics withheld.\n" "$current_stage" "$code" >&3; fi' EXIT
stage() {
    current_stage=$1
    printf 'Documentation stage: %s\n' "$current_stage" >&3
}
export UV_PROJECT_ENVIRONMENT="$DOCS_PRIVATE_RUNTIME/environment"
export UV_CACHE_DIR="$DOCS_PRIVATE_RUNTIME/uv-cache"
export PLAYWRIGHT_BROWSERS_PATH="$DOCS_PRIVATE_RUNTIME/browsers"
export PYTHONDONTWRITEBYTECODE=1
stage environment
uv sync --locked --group dev
stage inputs
uv run --no-sync python -m scripts.pages_inputs prepare "$store" "$DOCS_PRIVATE_RUNTIME"
export FONTLAB_API_SOURCE_ROOT="$DOCS_PRIVATE_RUNTIME/inputs/packages"
export FONTLAB_EXAMPLES_EXPORT="$DOCS_PRIVATE_RUNTIME/inputs/examples"
export PYTHONPATH="$FONTLAB_API_SOURCE_ROOT"
export FONTLAB_REQUIRE_CONSUMER=1
stage browser
uv run --no-sync python -m playwright install --with-deps chromium
stage consumer
./scripts/accept-consumer.sh --offline
stage python-tests
uv run --no-sync python -B -m pytest -q -rs -p no:cacheprovider tests
stage node-tests
node --test scripts/search_backend/tests.cjs
stage accessibility
uv run --no-sync python scripts/a11y_check.py --site .build/site --out "$DOCS_PRIVATE_RUNTIME/a11y.json"
stage interaction
uv run --no-sync python -m scripts.interaction_check --site .build/site --out "$DOCS_PRIVATE_RUNTIME/interaction.json"
stage accepted-check
./build.sh --check --offline
stage release-audit
raw_exit=0
uv run --no-sync python -m scripts.pages_inputs capture .build/site "$DOCS_PRIVATE_RUNTIME/audit" "$DOCS_PRIVATE_RUNTIME/release-audit.json" || raw_exit=$?
printf '%s\n' "$raw_exit" > "$DOCS_PRIVATE_RUNTIME/release-audit.exit"
printf 'Documentation release-audit exit: %s\n' "$raw_exit" >&3
stage audit-disposition
uv run --no-sync python -m scripts.pages_inputs disposition "$DOCS_PRIVATE_RUNTIME/release-audit.json" "$raw_exit"
stage complete
printf 'Complete frozen-input documentation, Python, Node, search, accessibility and interaction gates passed; release audit retains reviewed exit 1.\n' >&3
