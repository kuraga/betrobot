#!/bin/bash -x

date -R
today=$(date "+%Y-%m-%d")

curl -sL https://www.betsbc.com/current/#/line/line_ids=a:1 --proxy socks5://127.0.0.1:9050 > /dev/null || ( systemctl restart tor && sleep 15 )

rm -rf tmp/update/betcity
mkdir -p tmp/update/betcity

./node_modules/.bin/xvfb-maybe nodejs bbetrobot/parsers/etcity/stage1.js
mv tmp/update/betcity/current.html data/betcity/datesHtml/${today}.html
echo ${today} > data/betcity/datesHtml/next.txt
python3 betrobot/parsers/betcity/stage2.py

mongo betrobot --eval "db.bets.drop()"
find tmp/update/betcity/matchesJson -name "*.json" -exec mongoimport --db betrobot --collection bets --file "{}" \;

rm -rf tmp/update/betcity
