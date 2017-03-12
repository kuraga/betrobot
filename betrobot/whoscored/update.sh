#!/bin/bash -xe

rm -rf tmp/update/whoscored
mkdir -p tmp/update/whoscored

python3 betrobot/whoscored/stage1.py

python3 betrobot/whoscored/stage2.py

python3 betrobot/whoscored/stage3.py
