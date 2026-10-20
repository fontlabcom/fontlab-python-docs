#!/usr/bin/env bash
# this_file: build.sh
set -euo pipefail
cd "$(dirname "$0")"
for argument in "$@"; do
  if [[ "$argument" == "--offline" ]]; then export UV_OFFLINE=true; fi
done
uv sync --locked
uv run --no-sync python -m scripts.build_site "$@"

# Keep source/artifact checks read-only; only a successful build stages docs/.
case " $* " in
  *" --check "*|*" --serve "*) ;;
  *) uv run --no-sync python -m scripts.promote_site ;;
esac
