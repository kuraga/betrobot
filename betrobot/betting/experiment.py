import pymongo
import numpy as np
import pandas as pd
from betrobot.util.pickable import Pickable


class Experiment(Pickable):

    _pick = [ 'provider', '_db_name', '_matches_collection_name', '_sample_condition', '_is_trained' ]


    def __init__(self, provider, db_name='betrobot', matches_collection_name='matches', sample_condition=None):
        super().__init__()

        if sample_condition is None:
            sample_condition = {}

        self.provider = provider
        self._db_name = db_name
        self._matches_collection_name = matches_collection_name
        self._sample_condition = sample_condition

        self._is_trained = False

        self._init_collection()


    def _on_unpickle(self):
        super()._on_unpickle()

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

        # for proposer_data in self.provider.proposers_data:
        #    proposer_data['proposer'].flush(self._db['proposed'])


    def clear(self):
        self.provider.clear_proposers()


    def get_investigation(self):
        result = ''

        result += '\n=================================================='
        result += '\n%s (%s):\n%s' % (self.provider.name, self.provider.uuid, self.provider.description)
        result += '\n'

        result += '\nКоллекция тестовой выборки: %s' % repr(self._matches_collection_name)
        result += '\nУсловие тестовой выборки: %s' % repr(self._sample_condition)
        result += '\nВсего матчей обработано: %u' % self._matches_count

        for proposer_data in self.provider.proposers_data:
            proposer_investigation = self._get_proposer_investigation(proposer_data['proposer'], matches_count=self._matches_count)
            proposer_value_threshold = proposer_data['proposer'].value_threshold

            result += '\n'
            result += '\n%s (порог: %s)' % (proposer_data['name'], str(proposer_value_threshold) if proposer_value_threshold is not None else 'не ставится')
            result += '\n' + self._get_investigation_represantation(proposer_investigation, matches_count=self._matches_count)

        result += '\n=================================================='

        return result


    def _get_proposer_investigation(self, proposer, matches_count=None, coef_step=0.1):
        investigation = pd.DataFrame(columns=['min_coef', 'coef_mean', 'matches', 'bets', 'win', 'accuracy', 'roi'])

        bets_data = proposer.get_bets_data()
        for min_coef in np.arange(1.0, bets_data['bet_value'].max(), coef_step):
            bets = bets_data[ bets_data['ground_truth'].notnull() & (bets_data['bet_value'] >= min_coef) ]
            bets_count = bets.shape[0]
            if bets_count == 0:
                continue

            coef_mean = bets['bet_value'].mean()
            matches_count = bets['match_uuid'].nunique()
            bets_successful = bets[ bets['ground_truth'] ]
            bets_successful_count = bets_successful.shape[0]
            accuracy = bets_successful_count / bets_count
            roi = bets_successful['bet_value'].sum() / bets_count - 1

            investigation = investigation.append({
               'min_coef': min_coef,
               'coef_mean': coef_mean,
               'matches': matches_count,
               'bets': bets_count,
               'win': bets_successful_count,
               'accuracy': accuracy,
               'roi': roi
            }, ignore_index=True)

        return investigation


    # TODO: Выводить в ячейках осмысленный текст, а не просто числа
    # TODO: Выводить руссифицированные имена столбцов
    def _get_investigation_represantation(self, investigation, matches_count=None, min_coef=1.0, min_matches_freq=0.02, min_accuracy=0, min_roi=-np.inf, sort_by=['roi', 'min_coef'], sort_ascending=[False, True], nrows=20):
        t = investigation[
            ( investigation['min_coef'] >= min_coef ) &
            ( investigation['accuracy'] >= min_accuracy ) &
            ( investigation['roi'] >= min_roi )
        ]
        if matches_count is not None:
            t = t[ np.divide(t['matches'], matches_count) > min_matches_freq ]
        t.drop_duplicates(subset=['coef_mean', 'matches'], inplace=True)
        if t.shape[0] == 0:
            return '(none)'
        filtered_and_sorted_investigation = t.sort_values(by=sort_by, ascending=sort_ascending)[:nrows]

        investigation_represantation = pd.DataFrame.from_dict({
            'matches_count': filtered_and_sorted_investigation['matches'],
            'bets_count': filtered_and_sorted_investigation['bets'],
            'min_coef': filtered_and_sorted_investigation['min_coef'],
            'coef_mean': filtered_and_sorted_investigation['coef_mean'].round(2),
            'matches_freq': (100 * filtered_and_sorted_investigation['matches'].astype(np.int) / matches_count).round(1) if matches_count is not None else None,
            'accuracy': (100 * filtered_and_sorted_investigation['accuracy']).round(1),
            'roi': (100 * filtered_and_sorted_investigation['roi']).round(1)
        }).to_string(index=False)

        return investigation_represantation
