#!/bin/bash -xe

find tmp/update/betcity/matchesJson -type f -name "*.json" -exec mongoimport --db betrobot --collection bets --file "{}" \;

mv -v -S~ tmp/update/betcity/matches_metadata.json data/betcity
cp -vrf tmp/update/betcity/* data/betcity && rm -rf tmp/update/betcity/*
