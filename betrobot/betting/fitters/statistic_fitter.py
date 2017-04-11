import os
import pickle
import pandas as pd
from betrobot.betting.fitter import Fitter


class StatisticFitter(Fitter):

    _pick = [ 'train_sampler', 'statistic', '_statistic_file_path' ]


    def _clean(self):
        super()._clean()

        self.train_sampler = None
        self.statistic = None
        self._statistic_file_path = None


    def _fit(self, train_sampler):
        self.train_sampler = train_sampler

        # FIXME: Подумать об именах
        self._statistic_file_path = os.path.join('data', 'statistics', 'statistic-%s-%s.pkl' % (self.__class__.__name__, self.train_sampler.__class__.__name__))

        if os.path.exists(self._statistic_file_path):
            with open(self._statistic_file_path, 'rb') as f:
                self.statistic = pickle.load(f)

        else:
            self.statistic = self._evaluate_statistic(train_sampler)


    def _evaluate_statistic(self, train_sampler):
        sample = train_sampler.get_sample()

        statistic = pd.DataFrame(columns=['uuid', 'date', 'tournament_id', 'home', 'away', 'events_home_count', 'events_away_count']).set_index('uuid')
        for data in sample:
            match_uuid = data['uuid']
            print(match_uuid)

            whoscored_match = data['whoscored'][0]

            match_statistic = {
                'date': data['date'],
                'tournament_id': data['tournamentId'],
                'home': whoscored_match['home'],
                'away': whoscored_match['away'],
            }
            match_statistic_data = self._get_match_statistic_data(whoscored_match)
            match_statistic.update(match_statistic_data)
            statistic.loc[match_uuid] = match_statistic

        with open(self._statistic_file_path, 'wb') as f_out:
            pickle.dump(statistic, f_out)

        return statistic


    def _get_match_statistic_data(self, whoscored_match):
        return {}
