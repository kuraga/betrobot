#!/bin/bash -x

date -R
d=$(date +%Y-%m-%d)

curl -sL https://www.betsbc.com/new/#/line/line_ids=a:1 --proxy socks5://127.0.0.1:9050 > /dev/null || ( systemctl restart tor && sleep 15 )

mv data/betcity data/_betcity
mkdir -p data/betcity data/betcity/datesHtml data/betcity/matchesJson

./node_modules/.bin/xvfb-maybe nodejs betcity/stage1.js
mv data/betcity/_matches.html data/betcity/datesHtml/${d}.html
python3 betcity/stage2.py

mongo betrobot --eval "db.bets.drop()" --quiet
find data/betcity/matchesJson -name "*.json" -exec mongoimport --db betrobot --collection bets --file "{}" --quiet \;

mv data/betcity/datesHtml/${d}.html data/_betcity/datesHtml/${d}.html
rm -rf data/betcity
mv data/_betcity data/betcity
