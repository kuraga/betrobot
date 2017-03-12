#!/bin/bash -xe

rm -rf tmp/update/combined

python3 betrobot/combine/stage1.py
python3 betrobot/combine/clean.py Goal Cross CornerTaken Shot SavedShot MissedShots
