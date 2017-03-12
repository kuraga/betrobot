#!/bin/bash -xe

find betrobot/data/providers -type f -name "provider-*.pkl" exec python3 betrobot/propose.py "{}" proposed \;
