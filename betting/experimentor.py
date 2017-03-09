import pymongo
import numpy as np
import pandas as pd
from util.pickable import Pickable


class Experimentor(Pickable):

    _pick = [ 'provider', '_db_name', '_matches_collection_name', '_sample_condition', '_is_trained' ]


    def __init__(self, provider, db_name='betrobot', matches_collection_name='matches', sample_condition={}):
        self.provider = provider
        self._db_name = db_name
        self._matches_collection_name = matches_collection_name
        self._sample_condition = sample_condition

        self._is_trained = False

        self._init_collection()

        super().__init__()


    def _on_unpickle(self):
        self._init_collection()


    def _init_collection(self):
        self._client = pymongo.MongoClient()
        self._db = self._client[self._db_name]
        self._matches_collection = self._db[self._matches_collection_name]


    def train(self):
        self.provider.fit()

        self._is_trained = True


    def test(self):
        if not self._is_trained:
           raise RuntimeError('Not trained yet')

        sample = self._matches_collection.find(self._sample_condition)
        self._matches_count = sample.count()
        for data in sample:
            whoscored_match = data['whoscored'][0]
            if whoscored_match is None:
                continue

            for betarch_match in data['betarch']:
                self.provider.handle(betarch_match, whoscored_match=whoscored_match)


    def get_investigation(self):
        result = ''

        result += '\n=================================================='
        result += '\n%s: %s' % (self.provider.uuid, self.provider.description)
        result += '\n'

        result += '\nКоллекция тестовой выборки: %s' % repr(self._matches_collection_name)
        result += '\nУсловие тестовой выборки: %s' % repr(self._sample_condition)
        result += '\nВсего матчей обработано: %u' % self._matches_count

        for proposer_data in self.provider.proposers_data:
            proposer_investigation = self._get_proposer_investigation(proposer_data['proposer'], matches_count=self._matches_count)

            result += '\n'
            result += '\n' + proposer_data['name']
            result += '\n' + self._get_investigation_represantation(proposer_investigation, matches_count=self._matches_count)

        result += '\n=================================================='

        return result


    def _get_proposer_investigation(self, proposer, matches_count=None, koef_step=0.1):
        investigation = pd.DataFrame(columns=['min_koef', 'koef_mean', 'matches', 'bets', 'win', 'accurancy', 'roi'])

        bets_data = proposer.get_bets_data()
        for min_koef in np.arange(1.0, bets_data['bet_value'].max(), koef_step):
            bets = bets_data[ bets_data['ground_truth'].notnull() & (bets_data['bet_value'] > min_koef) ]
            bets_count = bets.shape[0]
            if bets_count == 0:
                continue

            koef_mean = bets['bet_value'].mean()
            matches_count = bets['match_uuid'].nunique()
            bets_successful = bets[ bets['ground_truth'] ]
            bets_successful_count = bets_successful.shape[0]
            accurancy = bets_successful_count / bets_count
            roi = bets_successful['bet_value'].sum() / bets_count - 1

            investigation = investigation.append({
               'min_koef': min_koef,
               'koef_mean': koef_mean,
               'matches': matches_count,
               'bets': bets_count,
               'win': bets_successful_count,
               'accurancy': accurancy,
               'roi': roi
            }, ignore_index=True)

        return investigation


    # TODO: Выводить в ячейках осмысленный текст, а не просто числа
    def _get_investigation_represantation(self, investigation, matches_count=None, min_koef=1.7, min_matches_freq=0.02, min_accurancy=0, min_roi=-np.inf, sort_by=['roi', 'min_koef'], sort_ascending=[False, True], nrows=10):
        t = investigation[
            ( investigation['min_koef'] > min_koef ) &
            ( investigation['accurancy'] > min_accurancy ) &
            ( investigation['roi'] > min_roi )
        ]
        if matches_count is not None:
            t = t[ np.divide(t['matches'], matches_count) > min_matches_freq ]
        t.drop_duplicates(subset=['koef_mean', 'matches'], inplace=True)
        filtered_and_sorted_investigation = t.sort_values(by=sort_by, ascending=sort_ascending)[:nrows]

        investigation_represantation = pd.DataFrame.from_dict({
            'min_koef': filtered_and_sorted_investigation['min_koef'],
            'koef_mean': filtered_and_sorted_investigation['koef_mean'].round(2),
            'matches_freq': (100 * filtered_and_sorted_investigation['matches'].astype(np.int) / matches_count).round(1) if matches_count is not None else None,
            'accurancy': (100 * filtered_and_sorted_investigation['accurancy']).round(1),
            'roi': (100 * filtered_and_sorted_investigation['roi']).round(1)
        }).to_string(index=False)

        return investigation_represantation
