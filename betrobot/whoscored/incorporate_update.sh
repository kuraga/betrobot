#!/bin/bash -xe

mv -v -S~ tmp/update/whoscored/matches_metadata.json data/whoscored
cp -vrf tmp/update/whoscored/* data/whoscored && rm -rf tmp/update/whoscored/*
