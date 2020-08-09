#!/usr/bin/env bash
dir=${0%/*}
if [ "$dir" = "$0" ]; then
    dir="."
fi
cd "$dir"

python2 -m mkdocs build -v -f ../mkdocs.yml --dirty
