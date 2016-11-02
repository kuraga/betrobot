#!/bin/bash -xe

date -R
curl -sL https://www.betsbc.com/new/#/line/line_ids=a:1 --proxy socks5://127.0.0.1:9050 > /dev/null || ( systemctl restart tor && sleep 15 )

rm data/betcity/matches.html data/betcity/matches_metadata.json

./node_modules/.bin/xvfb-maybe nodejs betcity/stage1.js
python3 betcity/stage2.py

mongo betrobot --eval "db.bets.drop()" --quiet
find data/betcity/matchesJson -name "*.json" -exec mongoimport --db betrobot --collection bets --file "{}" --quiet \;

cp data/betcity/matches.html data/betcity/datesHtml/$(date +%Y-%m-%d).html
