#!/bin/bash -xe

rm -rf tmp/update/betcity
mkdir -p tmp/update/betcity

python3 betrobot/parsers/betcity/stage2.py
