import numpy as np
import pandas as pd
from betrobot.betting.presenter import Presenter
from betrobot.betting.sport_util import get_standard_investigation, filter_and_sort_investigation


class ThresholdsVariationPresenter(Presenter):

    @staticmethod
    def filter_bets_data_by_thresholds(bets_data, value_threshold=None, predicted_threshold=None, ratio_threshold=None, max_value=None):
        filtered_bets_data = bets_data.copy()

        if value_threshold is not None:
            filtered_bets_data = filtered_bets_data[ filtered_bets_data['bet_value'] >= value_threshold ]

        if predicted_threshold is not None:
            try:
                # WARNING: Если selecting пустой, то возникает исключение: ValueError: Cannot index with multidimensional key
                filtered_bets_data = filtered_bets_data.loc[ filtered_bets_data.apply(lambda row: row['data'].get('probability_prediction', None) is None or 1.0/row['data']['probability_prediction'] <= predicted_threshold, axis='columns'), :]
            except ValueError:
                pass

        if ratio_threshold is not None:
            try:
                # WARNING: Если selecting пустой, то возникает исключение: ValueError: Cannot index with multidimensional key
                filtered_bets_data = filtered_bets_data.loc[ filtered_bets_data.apply(lambda row: row['data'].get('probability_prediction', None) is None or row['bet_value'] * row['data']['probability_prediction'] >= ratio_threshold, axis='columns'), :]
            except ValueError:
                pass

        if max_value is not None:
            filtered_bets_data = filtered_bets_data[ filtered_bets_data['bet_value'] <= max_value ]

        return filtered_bets_data


    _pick = [ 'thresholds_sets', 'filter_and_sort_investigation_kwargs' ]


    def __init__(self, thresholds_sets, filter_and_sort_investigation_kwargs=None):
        super().__init__()

        self.thresholds_sets = thresholds_sets
        if filter_and_sort_investigation_kwargs is not None:
            self.filter_and_sort_investigation_kwargs = filter_and_sort_investigation_kwargs
        else:
            self.filter_and_sort_investigation_kwargs = {}


    def present(self, provider):
        investigation_representation = ''

        for proposer in provider.proposers:
            investigation_representation += '\n'
            investigation_representation += '\nПропозер %s' % (str(proposer),)
            investigation = self._get_investigation(proposer, matches_count=provider.matches_count)
            investigation_representation += '\n' + self._get_investigation_representation(investigation)
            investigation_representation += '\n'

        return investigation_representation


    def _get_investigation(self, proposer, matches_count=None):
        investigation = pd.DataFrame(columns=['value_threshold', 'predicted_threshold', 'ratio_threshold', 'max_value', 'matches', 'matches_frequency', 'bets', 'win', 'accuracy', 'roi'])

        for thresholds in self.thresholds_sets:
            bets_data = proposer.get_bets_data()
            filtered_bets_data = self.__class__.filter_bets_data_by_thresholds(bets_data, **thresholds)

            investigation_line_dict = get_standard_investigation(filtered_bets_data, matches_count=matches_count)
            if investigation_line_dict is None:
                continue
            investigation_line_dict.update({
                'value_threshold': thresholds.get('value_threshold', None),
                'predicted_threshold': thresholds.get('predicted_threshold', None),
                'ratio_threshold': thresholds.get('ratio_threshold', None),
                'max_value': thresholds.get('max_value', None)
            })

            investigation = investigation.append(investigation_line_dict, ignore_index=True)

        return investigation


    def _get_investigation_representation(self, investigation):
        filtered_and_sorted_investigation = filter_and_sort_investigation(investigation, **self.filter_and_sort_investigation_kwargs)
        if filtered_and_sorted_investigation.shape[0] == 0:
            return '(none)'

        investigation_representation = pd.DataFrame.from_dict({
            'value_threshold': filtered_and_sorted_investigation['value_threshold'],
            'predicted_threshold': filtered_and_sorted_investigation['predicted_threshold'],
            'ratio_threshold': filtered_and_sorted_investigation['ratio_threshold'],
            'matches': filtered_and_sorted_investigation['matches'],
            'matches_frequency': np.round(100 * filtered_and_sorted_investigation['matches_frequency'], 1) if filtered_and_sorted_investigation['matches_frequency'] is not None else None,
            'bets': filtered_and_sorted_investigation['bets'],
            'win': filtered_and_sorted_investigation['win'],
            'accuracy': np.round(100 * filtered_and_sorted_investigation['accuracy'], 1),
            'roi': np.round(100 * filtered_and_sorted_investigation['roi'], 1),
            'profit': investigation['profit']
        })[ ['value_threshold', 'predicted_threshold', 'ratio_threshold', 'matches', 'matches_frequency', 'bets', 'win', 'accuracy', 'roi', 'profit'] ].to_string(index=False)

        return investigation_representation


    def _get_init_strs(self):
        return [
            'thresholds_sets=[<%d elements>])' % (len(self.thresholds_sets),)
        ]
