import numpy as np
import pandas as pd
from betrobot.betting.presenter import Presenter
from betrobot.util.sport_util import get_standard_investigation, filter_bets_data_by_thresholds


class ThresholdsVariationPresenter(Presenter):

    _pick = [ 'thresholds_sets' ]


    def __init__(self, thresholds_sets):
        super().__init__()

        self.thresholds_sets = thresholds_sets


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
        investigation = pd.DataFrame(columns=['value_threshold', 'predicted_threshold', 'ratio_threshold', 'matches_count', 'matches_frequency', 'bets_count', 'win_count', 'accuracy', 'roi'])

        for thresholds in self.thresholds_sets:
            bets_data = proposer.get_bets_data()
            filtered_bets_data = filter_bets_data_by_thresholds(bets_data, value_threshold=thresholds['value_threshold'], predicted_threshold=thresholds['predicted_threshold'], ratio_threshold=thresholds['ratio_threshold'])

            investigation_line_dict = get_standard_investigation(filtered_bets_data, matches_count=matches_count)
            if investigation_line_dict is None:
                continue
            investigation_line_dict.update({
                'value_threshold': thresholds['value_threshold'],
                'predicted_threshold': thresholds['predicted_threshold'],
                'ratio_threshold': thresholds['ratio_threshold']
            })

            investigation = investigation.append(investigation_line_dict, ignore_index=True)

        return investigation


    def _sort_and_filter_investigation(self, investigation, min_matches_frequency=0.02, min_accuracy=0, min_roi=-np.inf, sort_by=['roi', 'matches_frequency'], sort_ascending=[False, False]):
        result = investigation.copy()

        result = result[
            ( result['accuracy'] >= min_accuracy ) &
            ( result['matches_frequency'] >= min_matches_frequency ) &
            ( result['accuracy'] >= min_accuracy ) &
            ( result['roi'] >= min_roi )
        ]
        result.sort_values(by=sort_by, ascending=sort_ascending, inplace=True)

        return result


    def _get_investigation_representation(self, investigation, **kwargs):
        filtered_and_sorted_investigation = self._sort_and_filter_investigation(investigation, **kwargs)
        if filtered_and_sorted_investigation.shape[0] == 0:
            return '(none)'

        investigation_representation = pd.DataFrame.from_dict({
            'value_threshold': filtered_and_sorted_investigation['value_threshold'],
            'predicted_threshold': filtered_and_sorted_investigation['predicted_threshold'],
            'ratio_threshold': filtered_and_sorted_investigation['ratio_threshold'],
            'coef_mean': np.round(filtered_and_sorted_investigation['coef_mean'], 2),
            'matches': filtered_and_sorted_investigation['matches'],
            'matches_frequency': np.round(100 * filtered_and_sorted_investigation['matches_frequency'], 1) if filtered_and_sorted_investigation['matches_frequency'] is not None else None,
            'bets': filtered_and_sorted_investigation['bets'],
            'win': filtered_and_sorted_investigation['win'],
            'accuracy': np.round(100 * filtered_and_sorted_investigation['accuracy'], 1),
            'roi': np.round(100 * filtered_and_sorted_investigation['roi'], 1)
        })[ ['value_threshold', 'predicted_threshold', 'ratio_threshold', 'coef_mean', 'matches', 'matches_frequency', 'bets', 'win', 'accuracy', 'roi'] ].to_string(index=False)

        return investigation_representation


    def __str__(self):
        return '%s(thresholds_sets=[ <%d elements> ])' % (self.__class__.__name__, len(self.thresholds_sets))
