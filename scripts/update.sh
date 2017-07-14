#!/bin/bash -xe

rm -rf tmp/update
mkdir -p tmp/update

./scripts/whoscored/update.sh
./scripts/betcity/update.sh

python3 scripts/incorporate/incorporate.py
## python3 scripts/check/check_proposed_by_combined.py

rm -rf tmp/update
