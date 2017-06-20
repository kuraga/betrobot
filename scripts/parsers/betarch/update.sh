#!/bin/bash -xe

rm -rf tmp/data/betarch

python3 betrobot/scripts/parsers/betarch/stage1.py

python3 betrobot/scripts/parsers/betarch/stage2.py
