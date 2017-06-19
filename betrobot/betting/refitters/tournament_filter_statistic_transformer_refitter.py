import datetime
from betrobot.betting.refitter import Refitter
from betrobot.util.sport_util import get_teams_tournaments_countries_value


class TournamentFilterStatisticTransformerRefitter(Refitter):

    _pick = [ 'statistic', 'tournament_id' ]


    def _clean(self):
        super()._clean()

        self.statistic = None
        self.tournament_id = None


    def _refit(self, betcity_match):
        self.tournament_id = get_teams_tournaments_countries_value('betcityName', betcity_match['home'], 'whoscoredTournamentId')
        if self.tournament_id is None:
            return None

        statistic = self.previous_fitter.statistic
        transformed_statistic = statistic[ statistic['tournament_id'] == self.tournament_id ]

        self.statistic = transformed_statistic
