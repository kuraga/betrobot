#!/bin/bash -xe

find tmp/update/combined/matchesJson -type f -name "*.json" -exec mongoimport --db betrobot --collection matches --file "{}" \;
find tmp/update/combined/matchesJson-cleaned -type f -name "*.json" -exec mongoimport --db betrobot --collection matchesCleaned --file "{}" \;

cp -vrf tmp/update/combined/* data/combined && rm -rf tmp/update/combined/*
