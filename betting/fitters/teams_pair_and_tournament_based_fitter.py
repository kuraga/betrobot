import pandas as pd
from betting.fitter import Fitter
from util.sport_util import tournaments, collect_events_data


class TeamsPairAndTournamentBasedFitter(Fitter):
    def __init__(self, events_condition):
       self._events_condition = events_condition

       Fitter.__init__(self)


    def fit(self, train_sampler):
        tournaments_fitted_data = {}

        for tournament_id in tournaments:
            tournament_id = int(tournament_id)
            print(tournament_id)

            tournament_sample_condition = { 'tournamentId': tournament_id }
            sample = train_sampler.sample(tournament_sample_condition)

            tournaments_fitted_data[tournament_id] = self._fit_on_sample(sample)

        return tournaments_fitted_data


    # TODO: Использовать mean
    def _fit_on_sample(self, sample):
        events_data = collect_events_data(self._events_condition, sample)
        events_home_average = events_data['events_home_count'].mean()
        events_away_average = events_data['events_away_count'].mean()

        teams_attack_defense = pd.DataFrame(columns=['team', 'home_attack', 'home_defense', 'away_attack', 'away_defense']).set_index('team')

        home_teams = set(events_data['home'])
        for team in home_teams:
            team_home_data = events_data[ events_data['home'] == team ]
            team_home_matches_count = team_home_data.shape[0]

            teams_attack_defense.loc[team, 'home_attack'] = (team_home_data['events_home_count'].sum() / team_home_matches_count) / events_home_average
            teams_attack_defense.loc[team, 'home_defense'] = (team_home_data['events_away_count'].sum() / team_home_matches_count) / events_away_average

        away_teams = set(events_data['away'])
        for team in away_teams:
            team_away_data = events_data[ events_data['away'] == team ]
            team_away_matches_count = team_away_data.shape[0]

            teams_attack_defense.loc[team, 'away_attack'] = (team_away_data['events_away_count'].sum() / team_away_matches_count) / events_away_average
            teams_attack_defense.loc[team, 'away_defense'] = (team_away_data['events_home_count'].sum() / team_away_matches_count) / events_home_average

        fitted_data = {
            'teams_attack_defense': teams_attack_defense,
            'events_home_average': events_home_average,
            'events_away_average': events_away_average
        }

        return fitted_data
