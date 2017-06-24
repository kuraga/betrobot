import pymongo
import sys
import pickle
import argparse
from betrobot.betting.provider import Provider


def _propose(file_path, proposed_collection_name=None, output_file_path=None):
    db_name = 'betrobot'
    betting_matches_collection_name = 'bets'
    sample_condition = {}


    print('Loading...')
    client = pymongo.MongoClient()
    db = client[db_name]

    with open(file_path, 'rb') as f:
        provider = pickle.load(f)


    print('Betting...')
    bets_collection = db[betting_matches_collection_name]
    sample = bets_collection.find(sample_condition)
    for betcity_match in sample:
        provider.handle(betcity_match)

    print('==================================================')
    print('%s: %s' % (provider.uuid, provider.description))
    print()
    for proposer_data in provider.proposers_data:
        bets_data = proposer_data['proposer'].get_bets_data().to_string(index=False)

        print(proposer_data['name'])
        print(bets_data)
        print()
    print('==================================================')
    print()
    print()


    if proposed_collection_name is not None:
        print('Flushing...')
        proposed_collection = db[proposed_collection_name]
        for proposer_data in provider.proposers_data:
            proposer_data['proposer'].flush(proposed_collection)

    if output_file_path is not None:
        print('Saving...')
        with open(output_file_path, 'wb') as f:
            pickle.dump(provider, f)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('provider_file_path', help='provider file path')
    argument_parser.add_argument('-c', '--output-collection', help='collection proposed bets will be saved')
    argument_parser.add_argument('-o', '--output-file', help='file Provider will be saved')
    args = argument_parser.parse_args()

    _propose(args['provider_file_path'], proposed_collection_name=args['output_collection'], output_file_path=['output_file'])
