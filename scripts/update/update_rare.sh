#!/bin/bash -xe


./scripts/update/whoscored/update.sh

echo "--------------------------------------------------"

./scripts/update/betcity/update.sh

echo "--------------------------------------------------"

# WARNING: Перезапуск сервера необходим, т.к. мы обновили данные, читаемые только при запуске
./scripts/server/stop.sh

# FIXME: Исправить этот костыль
rm -rf tmp/caches/server_cache.db
cp -R tmp/caches/main_cache.db tmp/caches/server_cache.db

./scripts/server/start.sh
