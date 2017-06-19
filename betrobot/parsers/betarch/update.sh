#!/bin/bash -xe

rm -rf tmp/data/betarch

python3 betrobot/parsers/betarch/stage1.py

python3 betrobot/parsers/betarch/stage2.py
