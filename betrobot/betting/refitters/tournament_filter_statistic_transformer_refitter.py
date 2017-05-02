import datetime
from betrobot.betting.refitter import Refitter
from betrobot.util.sport_util import get_tournament_id_of_betcity_match


class TournamentFilterStatisticTransformerRefitter(Refitter):

    _pick = [ 'statistic', 'tournament_id' ]


    def _clean(self):
        super()._clean()

        self.statistic = None
        self.tournament_id = None


    def _refit(self, betcity_match):
        self.tournament_id = get_tournament_id_of_betcity_match(betcity_match)

        statistic = self.previous_fitter.statistic
        transformed_statistic = statistic[ statistic['tournament_id'] == self.tournament_id ]

        self.statistic = transformed_statistic
