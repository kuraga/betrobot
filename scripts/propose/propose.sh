#!/bin/bash -xe


mongo betrobot --eval "db.prediction_infos.drop();"
mongo betrobot --eval "db.proposed.drop();"

find data/providers -type f -name "provider-*.pkl" -exec ./scripts/propose/propose.py "{}" \;
