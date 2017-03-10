import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./sets/attack_defense')

import numpy as np
import pandas as pd
import scipy
import scipy.stats
from model import Model
from sport_util import collect_events_data, get_whoscored_team_ids_of_betcity_match


class AttackDefenseModel(Model):

    def fit(self, sample, condition=lambda event: True):
        events_data = collect_events_data(condition, sample)
        self._events_home_average = events_data['events_home_count'].mean()
        self._events_away_average = events_data['events_away_count'].mean()

        self._attack_defense = pd.DataFrame(columns=['team', 'home_attack', 'home_defense', 'away_attack', 'away_defense']).set_index('team')

        home_teams = set(events_data['home'])
        for team in home_teams:
            team_home_data = events_data[ events_data['home'] == team ]
            team_home_matches_count = team_home_data.shape[0]

            self._attack_defense.loc[team, 'home_attack'] = (team_home_data['events_home_count'].sum() / team_home_matches_count) / self._events_home_average
            self._attack_defense.loc[team, 'home_defense'] = (team_home_data['events_away_count'].sum() / team_home_matches_count) / self._events_away_average

        away_teams = set(events_data['away'])
        for team in away_teams:
            team_away_data = events_data[ events_data['away'] == team ]
            team_away_matches_count = team_away_data.shape[0]

            self._attack_defense.loc[team, 'away_attack'] = (team_away_data['events_away_count'].sum() / team_away_matches_count) / self._events_away_average
            self._attack_defense.loc[team, 'away_defense'] = (team_away_data['events_home_count'].sum() / team_away_matches_count) / self._events_home_average

        return self


    def predict(self, whoscored_home, whoscored_away):
        teams = self._attack_defense.index.values
        if whoscored_home not in teams or whoscored_away not in teams:
            return None

        mu_home = self._attack_defense.loc[whoscored_home, 'home_attack'] * self._attack_defense.loc[whoscored_away, 'away_defense'] * self._events_home_average
        median_home = scipy.stats.poisson.median(mu_home)
        predicted_home = int(median_home) if not np.isnan(median_home) else 0

        mu_away = self._attack_defense.loc[whoscored_away, 'away_attack'] * self._attack_defense.loc[whoscored_home, 'home_defense'] * self._events_away_average
        median_away = scipy.stats.poisson.median(mu_away)
        predicted_away = int(median_away) if not np.isnan(median_away) else 0

        return (predicted_home, predicted_away)
