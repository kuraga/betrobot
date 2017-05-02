import numpy as np
import pandas as pd
from betrobot.betting.presenter import Presenter


class TableSummaryPresenter(Presenter):

    _pick = [ 'value_threshold', 'predicted_threshold', 'ratio_threshold' ]


    def __init__(self, value_threshold=1.8, predicted_threshold=1.7, ratio_threshold=1.25):
        super().__init__()

        self.value_threshold = value_threshold
        self.predicted_threshold = predicted_threshold
        self.ratio_threshold = ratio_threshold


    # TODO: Выводить в ячейках осмысленный текст, а не просто числа
    # TODO: Выводить руссифицированные имена столбцов
    def present(self, provider):
        investigation = pd.DataFrame(columns=['proposer', 'coef_mean', 'matches_count', 'matches_frequency', 'bets_count', 'win_count', 'accuracy', 'roi'])

        for proposer in provider.proposers:
            bets_data = proposer.get_bets_data()

            bets_data = bets_data[ bets_data['ground_truth'].notnull() ]
            bets_data = bets_data[ bets_data['bet_value'] >= self.value_threshold ]
            # WARNING: Без этой строки, в следующей строке возникает исключение: ValueError: Cannot index with multidimensional key
            if bets_data.shape[0] == 0:
                continue
            bets_data = bets_data.loc[ bets_data.apply(lambda row: row['data']['predicted_bet_value'] <= self.predicted_threshold, axis='columns'), :]
            bets_data = bets_data.loc[ bets_data.apply(lambda row: row['bet_value'] / row['data']['predicted_bet_value'] >= self.ratio_threshold, axis='columns'), :]

            bets_count = bets_data.shape[0]
            if bets_count == 0:
                continue

            coef_mean = bets_data['bet_value'].mean()
            matches_frequency = bets_data['match_uuid'].nunique() / provider.matches_count if provider.matches_count != 0 else 0
            bets_successful = bets_data[ bets_data['ground_truth'] ]
            bets_successful_count = bets_successful.shape[0]
            accuracy = bets_successful_count / bets_count
            roi = bets_successful['bet_value'].sum() / bets_count - 1

            investigation = investigation.append({
               'proposer': str(proposer),
               'coef_mean': np.round(coef_mean, 2),
               'matches_count': provider.matches_count,
               'matches_frequency': np.round(100 * matches_frequency, 2),
               'bets_count': bets_count,
               'win_count': bets_successful_count,
               'accuracy': np.round(100 * accuracy, 1),
               'roi': np.round(100 * roi, 1)
            }, ignore_index=True)

        return investigation.to_string(index=False)


    def __str__(self):
        return '%s(value_threshold=%.2f, predicted_threshold=%.2f, ratio_threshold=%.2f)' % (self.__class__.__name__, self.value_threshold, self.predicted_threshold, self.ratio_threshold)
