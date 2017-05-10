import numpy as np
import pandas as pd
from betrobot.betting.presenter import Presenter
from betrobot.util.sport_util import get_standard_investigation, filter_bets_data_by_thresholds


class TableSummaryPresenter(Presenter):

    _pick = [ 'value_threshold', 'predicted_threshold', 'ratio_threshold' ]


    def __init__(self, value_threshold=1.8, predicted_threshold=1.7, ratio_threshold=1.25):
        super().__init__()

        self.value_threshold = value_threshold
        self.predicted_threshold = predicted_threshold
        self.ratio_threshold = ratio_threshold


    def present(self, provider):
        investigation = self._get_investigation(provider, matches_count=provider.matches_count)
        return self._get_investigation_representation(investigation)


    def _get_investigation(self, provider, matches_count=None):
        investigation = pd.DataFrame(columns=['proposer', 'coef_mean', 'matches_count', 'matches_frequency', 'bets_count', 'win_count', 'accuracy', 'roi'])

        for proposer in provider.proposers:
            bets_data = proposer.get_bets_data()
            filtered_bets_data = filter_bets_data_by_thresholds(bets_data, value_threshold=self.value_threshold, predicted_threshold=self.predicted_threshold, ratio_threshold=self.ratio_threshold)

            investigation_line_dict = get_standard_investigation(filtered_bets_data, matches_count=matches_count)
            if investigation_line_dict is None:
                continue
            investigation_line_dict.update({
                'proposer': str(proposer)
            })

            investigation = investigation.append(investigation_line_dict, ignore_index=True)

        return investigation


    def _get_investigation_representation(self, investigation):
        if investigation.shape[0] == 0:
            return '(none)'

        investigation_representation = pd.DataFrame.from_dict({
            'proposer': investigation['proposer'],
            'coef_mean': np.round(investigation['coef_mean'], 2),
            'matches': investigation['matches'],
            'matches_frequency': np.round(100 * investigation['matches_frequency'], 1) if investigation['matches_frequency'] is not np.nan else np.nan,
            'bets': investigation['bets'],
            'win': investigation['win'],
            'accuracy': np.round(100 * investigation['accuracy'], 1),
            'roi': np.round(100 * investigation['roi'], 1)
        })[ ['proposer', 'coef_mean', 'matches', 'matches_frequency', 'bets', 'win', 'accuracy', 'roi'] ].to_string(index=False)

        return investigation_representation


    def __str__(self):
        return '%s(value_threshold=%.2f, predicted_threshold=%.2f, ratio_threshold=%.2f)' % (self.__class__.__name__, self.value_threshold, self.predicted_threshold, self.ratio_threshold)
