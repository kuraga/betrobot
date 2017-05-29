import os
import pickle
import tqdm
import pandas as pd
from betrobot.betting.fitter import Fitter


class StatisticFitter(Fitter):

    _pick = [ 'statistic', '_statistic_file_path' ]


    def _clean(self):
        super()._clean()

        self.statistic = None
        self._statistic_file_path = None


    def _fit(self, force=False):
        # FIXME: Подумать об именах
        self._statistic_file_path = os.path.join('data', 'statistics', 'statistic-%s-%s.pkl' % (self.__class__.__name__, self.train_sampler.__class__.__name__))

        if not force and os.path.exists(self._statistic_file_path):
            print('Use already saved statistic %s' % (self._statistic_file_path,))
            with open(self._statistic_file_path, 'rb') as f:
                self.statistic = pickle.load(f)

        else:
            print('Evaluating statistic %s...' % (self._statistic_file_path,))
            self.statistic = self._evaluate_statistic()


    def _evaluate_statistic(self):
        statistic = pd.DataFrame(columns=['uuid', 'date', 'tournament_id', 'home', 'away', 'events_home_count', 'events_away_count']).set_index('uuid', drop=False)

        for data in tqdm.tqdm(self.sample, total=self.sample.count()):
            match_uuid = data['uuid']

            whoscored_match = data['whoscored'][0]

            match_statistic = {
                'uuid': data['uuid'],
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

        # TODO: Подумать, как избежать дубликатов
        statistic.drop_duplicates(subset=['uuid'], keep='last', inplace=True)

        return statistic


    def _get_match_statistic_data(self, whoscored_match):
        return {}
