import numpy as np
import pandas as pd
from betrobot.betting.presenter import Presenter
from betrobot.betting.sport_util import get_standard_investigation, filter_and_sort_investigation


class TableInvestigationPresenter(Presenter):

    _pick = [ 'deep', 'filter_and_sort_investigation_kwargs' ]


    def __init__(self, deep=False, filter_and_sort_investigation_kwargs=None):
        super().__init__()

        self.deep = deep
        if filter_and_sort_investigation_kwargs is None:
            self.filter_and_sort_investigation_kwargs = {}
        else:
            self.filter_and_sort_investigation_kwargs = filter_and_sort_investigation_kwargs


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


    def _get_investigation(self, bets_data, matches_count=None, value_step=0.1):
        investigation = pd.DataFrame(columns=['value_threshold', 'value_mean', 'matches', 'matches_frequency', 'bets', 'win', 'accuracy', 'roi'])

        for value_threshold in np.arange(1.0, bets_data['bet_value'].max(), value_step):
            filtered_bets_data = bets_data[ bets_data['bet_value'] >= value_threshold ]

            investigation_line_dict = get_standard_investigation(filtered_bets_data, matches_count=matches_count)
            if investigation_line_dict is None:
                continue
            investigation_line_dict.update({
                'value_threshold': value_threshold,
                'value_mean': filtered_bets_data['bet_value'].mean()
            })

            investigation = investigation.append(investigation_line_dict, ignore_index=True)

        return investigation


    def _get_investigation_representation(self, investigation):
        filtered_and_sorted_investigation = filter_and_sort_investigation(investigation, **self.filter_and_sort_investigation_kwargs)
        if filtered_and_sorted_investigation.shape[0] == 0:
            return '(none)'
        filtered_and_sorted_investigation.drop_duplicates(subset=['value_mean', 'matches'], inplace=True)
        filtered_and_sorted_investigation.sort_values(by='value_threshold', ascending=True, inplace=True)
        filtered_and_sorted_investigation = filtered_and_sorted_investigation[:20]

        investigation_representation = pd.DataFrame.from_dict({
            'value_threshold': filtered_and_sorted_investigation['value_threshold'],
            'value_mean': np.round(filtered_and_sorted_investigation['value_mean'], 2),
            'matches': filtered_and_sorted_investigation['matches'],
            'matches_frequency': np.round(100 * filtered_and_sorted_investigation['matches_frequency'], 1) if filtered_and_sorted_investigation['matches_frequency'] is not None else None,
            'bets': filtered_and_sorted_investigation['bets'],
            'win': filtered_and_sorted_investigation['win'],
            'accuracy': np.round(100 * filtered_and_sorted_investigation['accuracy'], 1),
            'roi': np.round(100 * filtered_and_sorted_investigation['roi'], 1),
            'profit': investigation['profit']
        })[ ['value_threshold', 'value_mean', 'matches', 'matches_frequency', 'bets', 'win', 'accuracy', 'roi', 'profit'] ].to_string(index=False)

        return investigation_representation


    def _get_init_strs(self):
        return [
            'deep=%s' % (str(self.deep),),
            'filter_and_sort_investigation_kwargs=%s' % (str(filter_and_sort_investigation_kwargs),)
        ]
