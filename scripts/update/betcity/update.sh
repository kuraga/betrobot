#!/bin/bash -xe


date -R
today=$(date "+%Y-%m-%d")

rm -rf tmp/update/betcity
mkdir -p tmp/update/betcity

./node_modules/.bin/xvfb-maybe nodejs scripts/update/betcity/stage1.js
./scripts/update/betcity/stage2.py
./scripts/update/betcity/incorporate.py

rm -f "data/betcityDatesHtml/${today}_*.html"
mv -f tmp/update/betcity/datesHtml/* data/betcityDatesHtml

rm -rf tmp/update/betcity
