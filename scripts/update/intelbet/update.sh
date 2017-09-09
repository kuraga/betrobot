#!/bin/bash -xe


rm -rf tmp/update/intelbet/*

./scripts/update/intelbet/stage1.py
./scripts/update/intelbet/stage2.py
./scripts/update/intelbet/stage3.py
./scripts/update/intelbet/match_names.py
./scripts/update/intelbet/incorporate.py

rm -rf tmp/update/intelbet/*
