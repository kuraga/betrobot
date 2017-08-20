#!/usr/bin/env python3


import pymongo
import argparse
from betrobot.util.database_util import db


def _create_indexes():
    db.create_collection('match_header')
    match_headers_collection = db['match_headers']
    match_headers_collection.drop_indexes()
    match_headers_collection.create_index('uuid', unique=True)
    match_headers_collection.create_index('region_id')
    match_headers_collection.create_index('tournament_id')
    match_headers_collection.create_index('date')
    match_headers_collection.create_index('home')
    match_headers_collection.create_index('away')
    match_headers_collection.create_index([('date', pymongo.ASCENDING), ('home', pymongo.ASCENDING), ('away', pymongo.ASCENDING)], unique=True)

    db.create_collection('additional_info')
    additional_info_collection = db['additional_info']
    additional_info_collection.create_index('match_uuid', unique=True)

    db.create_collection('matches')
    matches_collection = db['matches']
    matches_collection.create_index('match_uuid', unique=True)

    db.create_collection('bets')
    bets_collection = db['bets']
    bets_collection.create_index('match_uuid', unique=True)

    db.create_collection('prediction_infos')
    additional_info_collection = db['prediction_infos']
    additional_info_collection.create_index('match_uuid')


def _db_init():
    _create_indexes()


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _db_init()
