#!/bin/bash -xe

rm -rf data/betarch/datesHtml data/betarch/matchesJson data/betarch/matches_metadata.json
cp -vrf tmp/update/betarch/* data/betarch && rm -rf tmp/update/betarch/*
