#!/usr/bin/env python3


import tqdm
import argparse
import numpy as np
from betrobot.util.database_util import db
from betrobot.betting.bets_checking import check_bet


def _check_proposed():
    proposed_collection = db['proposed']

    sample = proposed_collection.find({ 'ground_truth': None })
    for bet in tqdm.tqdm(sample, total=sample.count()):
        ground_truth = check_bet(bet)
        proposed_collection.update_one({ '_id': bet['_id'] }, { '$set': { 'ground_truth': ground_truth } })


def _print_statistic():
    proposed_collection = db['proposed']

    print({
        'totalCount': proposed_collection.count(),
        'totalAvg': proposed_collection.aggregate([ { '$match': { 'ground_truth': { '$ne': None } } }, { '$group': { '_id': None, 'avg': { '$avg': '$value' } } } ]).next()['avg'],
        'positiveAvg': proposed_collection.aggregate([ { '$match': { 'ground_truth': True } }, { '$group': { '_id': None, 'avg': { '$avg': '$value' } } } ]).next()['avg'],
        'positiveRatio': np.round( proposed_collection.find({ 'ground_truth': True }).count() / \
            proposed_collection.find({ 'ground_truth': { '$ne': None } }).count(), 3 ),
        'ROI': np.round( proposed_collection.aggregate([ { '$match': { 'ground_truth': True } }, { '$group': { '_id': None, 'sum': { '$sum': '$value' } } } ]).next()['sum'] / \
            proposed_collection.find({ 'ground_truth': { '$ne': None } }).count() - 1, 3 )
    })


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _check_proposed()
    _print_statistic()
