#!/bin/bash -xe


BETROBOT_CACHE_PATH="tmp/caches/server_cache.db" ./scripts/web/main.py 2>> logs/server.error.log 1>> logs/server.stdout.log &

PID=$!
echo "${PID}" > tmp/server.pid
echo "PID: ${PID}"
