import numpy as np
import pandas as pd
from betrobot.betting.presenter import Presenter


class TableInvestigationPresenter(Presenter):

    _pick = [ 'deep' ]


    def __init__(self, deep=False):
        super().__init__()

        self.deep = deep


    def present(self, provider):
        result = ''

        if self.deep:
            for proposer in provider.proposers:
                result += self._present_proposer(proposer, matches_count=provider.matches_count)
                result += '\n'
        else:
            bets_data = pd.concat([ proposer.get_bets_data() for proposer in provider.proposers ])
            result += self._present_bets_data(bets_data, matches_count=provider.matches_count)

        return result


    def _present_proposer(self, proposer, matches_count=None):
        bets_data = proposer.get_bets_data()

        result = ''

        result += '\n%s' % (str(proposer),)
        result += '\n' + self._present_bets_data(bets_data, matches_count=matches_count)

        return result


    def _present_bets_data(self, bets_data, matches_count=None):
        investigation = self._get_investigation(bets_data, matches_count=matches_count)
        return self._get_investigation_representation(investigation, matches_count=matches_count)


    def _get_investigation(self, bets_data, matches_count=None, coef_step=0.1):
        investigation = pd.DataFrame(columns=['min_coef', 'coef_mean', 'matches', 'bets', 'win', 'accuracy', 'roi'])

        for min_coef in np.arange(1.0, bets_data['bet_value'].max(), coef_step):
            bets_data_ = bets_data.copy()

            bets_data_ = bets_data_[ bets_data_['ground_truth'].notnull() ]
            bets_data_ = bets_data_[ bets_data_['bet_value'] >= min_coef ]

            bets_count = bets_data_.shape[0]
            if bets_count == 0:
                continue

            coef_mean = bets_data_['bet_value'].mean()
            matches_count = bets_data_['match_uuid'].nunique()
            bets_successful = bets_data_[ bets_data_['ground_truth'] ]
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
    def _get_investigation_representation(self, investigation, matches_count=None, min_coef=1.0, min_matches_frequency=0.02, min_accuracy=0, min_roi=-np.inf, sort_by=['roi', 'min_coef'], sort_ascending=[False, True], nrows=20):
        t = investigation[
            ( investigation['min_coef'] >= min_coef ) &
            ( investigation['accuracy'] >= min_accuracy ) &
            ( investigation['roi'] >= min_roi )
        ]
        if matches_count is not None:
            t = t[ np.divide(t['matches'], matches_count) > min_matches_frequency ]
        t.drop_duplicates(subset=['coef_mean', 'matches'], inplace=True)
        if t.shape[0] == 0:
            return '(none)'
        filtered_and_sorted_investigation = t.sort_values(by=sort_by, ascending=sort_ascending)[:nrows]

        # TODO: Выводить дисперсию ROI
        investigation_representation = pd.DataFrame(columns=['min_coef', 'coef_mean', 'matches_count', 'matches_frequency', 'bets_count', 'win_count', 'accuracy', 'roi']).append(pd.DataFrame.from_dict({
            'min_coef': filtered_and_sorted_investigation['min_coef'],
            'coef_mean': np.round(filtered_and_sorted_investigation['coef_mean'], 2),
            'matches_count': filtered_and_sorted_investigation['matches'],
            'matches_frequency': np.round(100 * filtered_and_sorted_investigation['matches'] / matches_count, 1) if matches_count is not None else None,
            'bets_count': filtered_and_sorted_investigation['bets'],
            'win_count': filtered_and_sorted_investigation['win'],
            'accuracy': np.round(100 * filtered_and_sorted_investigation['accuracy'], 1),
            'roi': np.round(100 * filtered_and_sorted_investigation['roi'], 1)
        }), ignore_index=True).to_string(index=False)

        return investigation_representation


    def __str__(self):
        return '%s(deep=%s)' % (self.__class__.__name__, str(self.deep))
