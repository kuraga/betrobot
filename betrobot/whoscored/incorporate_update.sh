#!/bin/bash -xe

mv -v -S~ tmp/update/whoscored/matches_metadata.json data/whoscored
mv -vf tmp/update/whoscored/* data/whoscored
