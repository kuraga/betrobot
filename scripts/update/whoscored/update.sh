#!/bin/bash -xe


rm -rf tmp/update/whoscored
mkdir -p tmp/update/whoscored

python3 scripts/update/whoscored/save_headers_templater.py
./node_modules/.bin/xvfb-maybe nodejs tmp/update/whoscored/save_headers.js

python3 scripts/update/whoscored/stage1.py
python3 scripts/update/whoscored/stage2.py
python3 scripts/update/whoscored/stage3.py
python3 scripts/update/whoscored/incorporate.py

rm -rf tmp/update/whoscored
