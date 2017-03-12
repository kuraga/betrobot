#!/bin/bash -xe

rm -rf tmp/data/betarch

python3 betrobot/betarch/stage1.py

python3 betrobot/betarch/stage2.py
