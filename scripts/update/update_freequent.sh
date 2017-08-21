#!/bin/bash -xe


./scripts/update/intelbet/update.sh

echo "--------------------------------------------------"

./scripts/update/propose/propose.sh

echo "--------------------------------------------------"

# WARNING: Перезапуск сервера необходим, т.к. мы обновили данные, читаемые только при запуске
./scripts/server/stop.sh
./scripts/server/start.sh
