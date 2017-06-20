#!/bin/bash -xe

rm -rf tmp/update
mkdir -p tmp/update

./betrobot/parsers/whoscored/update.sh
./betrobot/parsers/betcity/update.sh
./betrobot/scripts/combine/update.sh

./betrobot/parsers/whoscored/incorporate_update.sh
./betrobot/parsers/betcity/incorporate_update.sh
./betrobot/scripts/combine/incorporate_update.sh

## python3 betrbot/scripts/check/check_proposed_by_combined.py

rm -rf tmp/update
