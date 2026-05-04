#!/usr/bin/env bash

set -ev

FIX_FLAG=""
if [[ "$1" == "--fix" ]]; then
  FIX_FLAG="--fix"
fi

if [[ -z $GITHUB_ACTION ]]; then
  ruff format conflux tests examples
else
  ruff format --check conflux tests examples
fi

ruff check $FIX_FLAG conflux tests examples
ty check conflux tests examples
