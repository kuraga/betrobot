#!/bin/bash -xe

rm -rf tmp/update
mkdir -p tmp/update

./betrobot/whoscored/update.sh
./betrobot/betcity/update.sh
./betrobot/combine/update.sh

./betrobot/whoscored/incorporate_update.sh
./betrobot/betcity/incorporate_update.sh
./betrobot/combine/incorporate_update.sh

python3 betrbot/check_proposed.py

rm -rf tmp/update
