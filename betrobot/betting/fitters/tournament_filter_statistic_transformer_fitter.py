import datetime
from betrobot.betting.fitters.statistic_transformer_fitter import StatisticTransformerFitter


class TournamentFilterStatisticTransformerFitter(StatisticTransformerFitter):

    _pick = [ 'tournament_id' ]


    def _clean(self):
        super()._clean()

        self.tournament_id = None


    def _fit(self, statistic_fitter, tournament_id):
        self._prefit(statistic_fitter)

        self.tournament_id = tournament_id

        statistic = self.statistic_fitter.statistic
        transformed_statistic = statistic[ statistic['tournament_id'] == self.tournament_id ]

        self.statistic = transformed_statistic
