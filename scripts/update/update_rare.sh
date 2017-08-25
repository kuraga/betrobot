#!/bin/bash -xe


./scripts/update/whoscored/update.sh

echo "--------------------------------------------------"

./scripts/update/betcity/update.sh

echo "--------------------------------------------------"

# WARNING: Перезапуск сервера необходим, т.к. мы обновили данные, читаемые только при запуске
./scripts/web/stop.sh || echo

# FIXME: Исправить этот костыль
rm -rf tmp/caches/web_cache.db
cp -R tmp/caches/main_cache.db tmp/caches/web_cache.db

./scripts/web/start.sh
