#!/bin/bash -xe

rm -rf data/betarch/datesHtml data/betarch/matchesJson data/betarch/matches_metadata.json
mv -vf tmp/update/betarch/* data/betarch
