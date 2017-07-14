#!/usr/bin/env python3


import datetime
import pickle
import tqdm
import argparse
from betrobot.util.common_util import eve_datetime
from betrobot.betting.provider import Provider
from betrobot.util.database_util import db


def _propose(provider_file_path, output_file_path=None):
    sample_condition = {
       'date': { '$gte': eve_datetime(datetime.datetime.today()) }
    }

    with open(provider_file_path, 'rb') as f:
        provider = pickle.load(f)

    bets_collection = db['bets']
    match_headers_collection = db['match_headers']

    match_headers_sample = match_headers_collection.find(sample_condition, { 'uuid': True })
    for match_header in tqdm.tqdm(match_headers_sample, total=match_headers_sample.count()):
        provider.handle(match_header['uuid'])


    print('**************************************************')
    print('Провайдер %s' % (str(provider),))
    if provider.description is not None:
        print('%s' % (provider.description,))
    print()
    print('Условие выборки: %s' % str(sample_condition))
    print()
    for proposer in provider.proposers:
        print('==================================================')
        print(str(proposer))
        print()
        print( proposer.bets_data.to_string(index=False) )
        print()
        print('==================================================')
        print()
    print()
    print('**************************************************')

    proposed_collection = db['proposed']
    for proposer in provider.proposers:
        proposer.flush(proposed_collection)

    if output_file_path is not None:
        with open(output_file_path, 'wb') as f:
            pickle.dump(provider, f)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('provider_file_path', help='provider file path')
    argument_parser.add_argument('-o', '--output-file', help='file Provider will be saved')
    args = argument_parser.parse_args()

    _propose(args.provider_file_path, args.output_file)
