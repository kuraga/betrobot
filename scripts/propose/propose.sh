#!/bin/bash -xe


find data/providers -type f -name "provider-*.pkl" -exec python3 scripts/propose/propose.py "{}" \;
