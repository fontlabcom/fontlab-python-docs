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
# Bounded so a hung apt or CDN fetch fails by name, not after ten silent minutes.
# A stale apt index is the commonest cause, so refresh it first (CI only).
# No tool output is ever echoed publicly: on failure only fixed strings
# (stage, exit code, timeout flag) are printed; full output stays in the private log.
code=0
if [[ -n "${GITHUB_ACTIONS:-}" ]] && command -v sudo >/dev/null; then
    timeout -k 10 120 sudo apt-get update || true
fi
timeout -k 10 300 uv run --no-sync python -m playwright install --with-deps chromium || code=$?
if (( code )); then
    if (( code == 124 )); then echo "browser stage: install timed out after 300 s (exit 124)" >&3
    else echo "browser stage: install failed (exit $code)" >&3; fi
    exit "$code"
fi
stage consumer
./scripts/accept-consumer.sh --offline
stage python-tests
uv run --no-sync python -B -m pytest -q -rs -p no:cacheprovider tests
stage node-tests
mkdir -p .build/archive-compiler
cp scripts/archive_search/package.json scripts/archive_search/package-lock.json .build/archive-compiler/
npm ci --prefix .build/archive-compiler --ignore-scripts --no-audit --no-fund
node --test scripts/search_backend/tests.cjs
node --test scripts/archive_search/tests.cjs
node --test scripts/archive_search/tests-ui.cjs
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
