#!/bin/bash -xe


./scripts/update/intelbet/update.sh

echo "--------------------------------------------------"

./scripts/propose/propose.sh

echo "--------------------------------------------------"

# WARNING: Перезапуск сервера необходим, т.к. мы обновили данные, читаемые только при запуске
./scripts/web/stop.sh || echo
./scripts/web/start.sh
