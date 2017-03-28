#!/bin/bash -xe

find tmp/update/betcity/matchesJson -type f -name "*.json" -exec mongoimport --db betrobot --collection bets --file "{}" --quiet \;

mv -v -S~ tmp/update/betcity/matches_metadata.json data/betcity
# FIXME: Ошибка: каталог не пуст
mv -vf tmp/update/betcity/* data/betcity
