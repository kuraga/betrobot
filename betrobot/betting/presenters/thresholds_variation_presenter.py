import numpy as np
import pandas as pd
from betrobot.betting.presenter import Presenter
from betrobot.util.sport_util import get_standard_investigation, filter_bets_data_by_thresholds, filter_and_sort_investigation


# TODO: Сделать универсальным: преобразовать в ParametrsGridPresenter
class ThresholdsVariationPresenter(Presenter):

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
            filtered_bets_data = filter_bets_data_by_thresholds(bets_data, **thresholds)

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
            'roi': np.round(100 * filtered_and_sorted_investigation['roi'], 1)
        })[ ['value_threshold', 'predicted_threshold', 'ratio_threshold', 'matches', 'matches_frequency', 'bets', 'win', 'accuracy', 'roi'] ].to_string(index=False)

        return investigation_representation


    def _get_init_strs(self):
        return [
            'thresholds_sets=[<%d elements>])' % (len(self.thresholds_sets),)
        ]
