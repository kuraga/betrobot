import sys
sys.path.append('./')
sys.path.append('./util')


import numpy as np
import pandas as pd


# TODO: Выводить текст, а не числа
def get_investigation_representation(proposer, matches_count=None, nrows=10, min_matches_freq=0.02):
    investigation = proposer.get_investigation()

    filtered_and_sorted_investigation = investigation.sort_values(by=['roi', 'min_koef'], ascending=[False, True])[:nrows]
    investigation_represantation = pd.DataFrame.from_dict({
        'min_koef': filtered_and_sorted_investigation['min_koef'],
        'koef_mean': filtered_and_sorted_investigation['koef_mean'].round(2),
        'matches': (100 * filtered_and_sorted_investigation['matches'].astype(np.int) / matches_count).round(1) if matches_count is not None else None,
        'roi': (100 * filtered_and_sorted_investigation['roi']).round(1),
        'accurancy': (100 * filtered_and_sorted_investigation['accurancy']).round(1)
    })
    investigation_represantation = investigation_represantation[investigation_represantation['matches'] > 100*min_matches_freq]

    return investigation_represantation


def print_investigation_representation(proposer_data, matches_count=None, nrows=10, min_matches_freq=0.02):
    print(proposer_data['name'])
    if proposer_data.get('description') is not None:
        print(proposer_data['description'])
    print()

    proposer_invetigation_representation = get_investigation_representation(proposer_data['proposer'], matches_count=matches_count, nrows=nrows, min_matches_freq=min_matches_freq)
    print(proposer_invetigation_representation.to_string(index=False))


def print_bets_data(proposer_data):
    print(proposer_data['name'])
    if proposer_data.get('description') is not None:
        print(proposer_data['description'])
    print()

    proposer_bets_data = proposer_data['proposer'].get_bets_data()
    print(proposer_bets_data.to_string(index=False))
