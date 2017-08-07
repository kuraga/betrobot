#!/bin/bash -xe


find data/providers -type f -name "provider-*.pkl" -exec ./scripts/propose/propose.py "{}" \;
