#!/usr/bin/env bash
dir=${0%/*}
if [ "$dir" = "$0" ]; then
    dir="."
fi
cd "$dir"

uv run --project ../.. properdocs build -v -f ../mkdocs.yml
