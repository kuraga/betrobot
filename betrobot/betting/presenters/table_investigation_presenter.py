import numpy as np
import pandas as pd
from betrobot.betting.presenter import Presenter
from betrobot.util.sport_util import get_standard_investigation


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
        return self._get_investigation_representation(investigation)


    def _get_investigation(self, bets_data, matches_count=None, coef_step=0.1):
        investigation = pd.DataFrame(columns=['min_coef', 'coef_mean', 'matches', 'matches_frequency', 'bets', 'win', 'accuracy', 'roi'])

        for min_coef in np.arange(1.0, bets_data['bet_value'].max(), coef_step):
            bets_data_filtered = bets_data[ bets_data['bet_value'] >= min_coef ]

            investigation_line_dict = get_standard_investigation(bets_data_filtered, matches_count=matches_count)
            if investigation_line_dict is None:
                continue
            investigation_line_dict.update({
                'min_coef': min_coef
            })

            investigation = investigation.append(investigation_line_dict, ignore_index=True)

        return investigation


    def _sort_and_filter_investigation(self, investigation, min_coef=1.0, min_matches_frequency=0.02, min_accuracy=0, min_roi=-np.inf, sort_by=['roi', 'min_coef', 'matches_frequency'], sort_ascending=[False, True, False], nrows=20):
        result = investigation.copy()

        result = result[
            ( result['min_coef'] >= min_coef ) &
            ( result['matches_frequency'] >= min_matches_frequency ) &
            ( result['accuracy'] >= min_accuracy ) &
            ( result['roi'] >= min_roi )
        ]
        result.drop_duplicates(subset=['coef_mean', 'matches'], inplace=True)
        result.sort_values(by=sort_by, ascending=sort_ascending, inplace=True)
        result = result[:nrows]

        return result


    def _get_investigation_representation(self, investigation, **kwargs):
        filtered_and_sorted_investigation = self._sort_and_filter_investigation(investigation, **kwargs)
        if filtered_and_sorted_investigation.shape[0] == 0:
            return '(none)'

        investigation_representation = pd.DataFrame.from_dict({
            'min_coef': filtered_and_sorted_investigation['min_coef'],
            'coef_mean': np.round(filtered_and_sorted_investigation['coef_mean'], 2),
            'matches': filtered_and_sorted_investigation['matches'],
            'matches_frequency': np.round(100 * filtered_and_sorted_investigation['matches_frequency'], 1) if filtered_and_sorted_investigation['matches_frequency'] is not None else None,
            'bets': filtered_and_sorted_investigation['bets'],
            'win': filtered_and_sorted_investigation['win'],
            'accuracy': np.round(100 * filtered_and_sorted_investigation['accuracy'], 1),
            'roi': np.round(100 * filtered_and_sorted_investigation['roi'], 1)
        })[ ['min_coef', 'coef_mean', 'matches', 'matches_frequency', 'bets', 'win', 'accuracy', 'roi'] ].to_string(index=False)

        return investigation_representation


    def __str__(self):
        return '%s(deep=%s)' % (self.__class__.__name__, str(self.deep))
