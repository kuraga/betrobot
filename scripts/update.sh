#!/bin/bash -xe

rm -rf tmp/update
mkdir -p tmp/update

./scripts/whoscored/update.sh
./scripts/betcity/update.sh
./scripts/combine/update.sh

./scripts/whoscored/incorporate_update.sh
./scripts/betcity/incorporate_update.sh
./scripts/combine/incorporate_update.sh

## python3 scripts/check/check_proposed_by_combined.py

rm -rf tmp/update
