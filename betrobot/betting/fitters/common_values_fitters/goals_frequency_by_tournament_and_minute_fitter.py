import os
import numpy as np
import pandas as pd
import tqdm
from betrobot.betting.fitter import Fitter
from betrobot.betting.sport_util import get_match_headers, get_extended_info, filter_events, is_goal, is_home, is_away


# TODO: Сделать универсальным
class GoalsFrequencyByTournamentAndMinuteFitter(Fitter):

    _pick = [ 'data' ]


    _goals_frequencies_by_tournament_and_minute_file_path = os.path.join('tmp', 'goals_frequencies_by_tournament_and_minute.csv')


    def _clean(self):
        super()._clean()

        self.data = None


    def _update(self):
        self.data = pd.DataFrame(columns=['tournament_id', 'minute', 'count', 'home_count', 'away_count', 'frequency', 'home_frequency', 'away_frequency']).set_index(['tournament_id', 'minute'], drop=False)

        match_headers = self.previous_fitter.match_headers.copy()

        for (match_uuid, match_header) in tqdm.tqdm(match_headers.iterrows(), total=match_headers.shape[0]):
            tournament_id = match_header['tournament_id']

            whoscored_match = get_extended_info(match_uuid)['whoscored']
            if 'matchCentreData' not in whoscored_match:
                continue

            events = whoscored_match['matchCentreData']['events']
            goal_events = filter_events(is_goal, events)
            for event in goal_events:
                minute = event['minute']

                if (tournament_id, minute) not in self.data.index.tolist():
                    self.data.loc[(tournament_id, minute), :] = pd.Series({
                        'tournament_id': tournament_id,
                        'minute': minute,
                        'count': 0,
                        'home_count': 0,
                        'away_count': 0,
                        'frequency': None,
                        'home_frequency': None,
                        'away_frequency': None
                    })

                self.data.at[(tournament_id, minute), 'count'] += 1
                if is_home(event, whoscored_match=whoscored_match):
                    self.data.at[(tournament_id, minute), 'home_count'] += 1
                elif is_away(event, whoscored_match=whoscored_match):
                    self.data.at[(tournament_id, minute), 'away_count'] += 1

        tournament_matches_counts = match_headers.groupby('tournament_id').size()

        self.data['frequency'] = self.data.apply(lambda row, tournament_matches_counts: row['count'] / tournament_matches_counts[ row['tournament_id'] ], args=(tournament_matches_counts,), axis=1)
        self.data['home_frequency'] = self.data.apply(lambda row, tournament_matches_counts: row['home_count'] / tournament_matches_counts[ row['tournament_id'] ], args=(tournament_matches_counts,), axis=1)
        self.data['away_frequency'] = self.data.apply(lambda row, tournament_matches_counts: row['away_count'] / tournament_matches_counts[ row['tournament_id'] ], args=(tournament_matches_counts,), axis=1)

        self.data.to_csv(self._goals_frequencies_by_tournament_and_minute_file_path, encoding='utf-8')


    def _fit(self, force=False, **kwargs):
        if os.path.exists(self._goals_frequencies_by_tournament_and_minute_file_path) and not force:
            self.data = pd.read_csv(self._goals_frequencies_by_tournament_and_minute_file_path, encoding='utf-8').set_index(['tournament_id', 'minute'], drop=False)
        else:
            self._update()
