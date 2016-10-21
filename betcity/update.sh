#!/bin/bash -xe

date -R
curl -sL https://www.betsbc.com/new/#/line/line_ids=a:1 --proxy socks5://127.0.0.1:9050 > /dev/null || ( systemctl restart tor && sleep 15 )

rm -rf data/betcity/matchesJson data/betcity/matches.html
mkdir -p data/betcity

./node_modules/.bin/xvfb-maybe nodejs betcity/stage1.js
python3 betcity/stage2.py

mongo betrobot --eval "db.bets.drop()" --quiet
find data/betcity/matchesJson -name '*.json' -exec mongoimport --db betrobot --collection bets --file '{}' --quiet \;

rm -rf data/betcity/matchesJson
