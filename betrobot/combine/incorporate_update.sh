#!/bin/bash -xe

find tmp/update/combined/matchesJson -type f -name "*.json" -exec mongoimport --db betrobot --collection matches --file "{}" --quiet \;
find tmp/update/combined/matchesJson-cleaned -type f -name "*.json" -exec mongoimport --db betrobot --collection matchesCleaned --file "{}" --quiet \;

mv -vf tmp/update/combined/* data/combined
