#!/bin/bash -xe

rm -rf tmp/update/whoscored
mkdir -p tmp/update/whoscored

python3 betrobot/parsers/whoscored/stage1.py

python3 betrobot/parsers/whoscored/stage2.py

python3 betrobot/parsers/whoscored/stage3.py
