#!/bin/bash -xe


rm -rf tmp/update/whoscored
mkdir -p tmp/update/whoscored

./scripts/update/whoscored/save_headers_templater.py
./node_modules/.bin/xvfb-maybe nodejs tmp/update/whoscored/save_headers.js

./scripts/update/whoscored/stage1.py
./scripts/update/whoscored/stage2.py
./scripts/update/whoscored/stage3.py
./scripts/update/whoscored/incorporate.py

rm -rf tmp/update/whoscored
