import numpy as np
import pandas as pd
from betrobot.betting.presenter import Presenter
from betrobot.betting.sport_util import get_standard_investigation


class TableSummaryPresenter(Presenter):

    def present(self, provider):
        investigation = self._get_investigation(provider, matches_count=provider.matches_count)
        return self._get_investigation_representation(investigation)


    def _get_investigation(self, provider, matches_count=None):
        investigation = pd.DataFrame(columns=['proposer', 'value_mean', 'matches', 'matches_frequency', 'bets', 'win', 'accuracy', 'roi'])

        for proposer in provider.proposers:
            bets_data = proposer.bets_data

            investigation_line_dict = get_standard_investigation(bets_data, matches_count=matches_count)
            if investigation_line_dict is None:
                continue
            investigation_line_dict.update({
                'proposer': str(proposer),
                'value_mean': bets_data['value'].mean()
            })

            investigation = investigation.append(investigation_line_dict, ignore_index=True)

        return investigation


    def _get_investigation_representation(self, investigation):
        if investigation.shape[0] == 0:
            return '(none)'

        investigation_representation = pd.DataFrame.from_dict({
            'proposer': investigation['proposer'],
            'value_mean': np.round(investigation['value_mean'], 2),
            'matches': investigation['matches'],
            'matches_frequency': np.round(100 * investigation['matches_frequency'], 1) if investigation['matches_frequency'] is not np.nan else np.nan,
            'bets': investigation['bets'],
            'win': investigation['win'],
            'accuracy': np.round(100 * investigation['accuracy'], 1),
            'roi': np.round(100 * investigation['roi'], 1),
            'profit': investigation['profit']
        })[ ['proposer', 'value_mean', 'matches', 'matches_frequency', 'bets', 'win', 'accuracy', 'roi', 'profit'] ].to_string(index=False)

        return investigation_representation
