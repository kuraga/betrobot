import pandas as pd
from betrobot.betting.fitters.statistic_fitter import StatisticFitter


class StatisticExtenderFitter(StatisticFitter):

    def _fit(self, **kwargs):
        statistic = self.previous_fitter.statistic.copy()
        if statistic.shape[0] == 0:
            self.statistic = statistic
            return

        extended_statistic_data = []
        for (_match_uuid, match_header) in statistic.iterrows():
            try:
                match_extended_statistic_data = self._get_match_statistic_data(match_header.to_dict())
                if match_extended_statistic_data is None:
                    # TODO: В этом случае все равно нужно добавлять None-овые колонки
                    continue
            except TypeError:
                # TODO: В этом случае все равно нужно добавлять None-овые колонки
                continue

            match_extended_statistic_data['uuid'] = _match_uuid
            extended_statistic_data.append(match_extended_statistic_data)

        extended_statistic = pd.DataFrame(extended_statistic_data)
        # WARNING: Необходимо из-за TypeError выше
        if extended_statistic.shape[0] > 0:
            extended_statistic = extended_statistic.set_index('uuid')

        transformed_statistic = statistic.join(extended_statistic)

        self.statistic = transformed_statistic


    def _get_match_statistic_data(self, match_header):
        return {}
