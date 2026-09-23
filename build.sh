#!/usr/bin/env bash
# this_file: build.sh
set -euo pipefail
cd "$(dirname "$0")"
uv run properdocs build -f fontlab7/mkdocs.yml
uv run properdocs build -f pythonqt/mkdocs.yml
touch docs/.nojekyll
