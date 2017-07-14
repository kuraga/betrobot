import datetime
from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.betting.sport_util import get_teams_tournaments_countries_value


class TournamentFilterStatisticTransformerFitter(StatisticFitter):

    _pick = [ 'tournament_id' ]


    def _clean(self):
        super()._clean()

        self.statistic = None
        self.tournament_id = None


    def _fit(self, match_header, **kwargs):
        statistic = self.previous_fitter.statistic.copy()
        if statistic.shape[0] == 0:
            self.statistic = statistic
            return

        self.tournament_id = match_header['tournamentId']

        transformed_statistic = statistic[ statistic['tournament_id'] == self.tournament_id ]

        self.statistic = transformed_statistic
