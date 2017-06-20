#!/bin/bash -xe

rm -rf tmp/update/combined

python3 betrobot/scripts/combine/stage1.py
python3 betrobot/scripts/combine/clean.py Goal Cross CornerTaken Card Shot
