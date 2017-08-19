import datetime
from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.util.logging_util import get_logger
from betrobot.util.common_util import get_value
from betrobot.betting.sport_util import tournaments_data


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

        self.statistic = transformed_statistic.copy()
        get_logger('prediction').info('Отобраны заголовки матчей, произошедших в рамках турнира %s (%u): %u штук',
            get_value(tournaments_data, 'whoscoredTournamentId', self.tournament_id, 'whoscoredTournamentName'), self.tournament_id, self.statistic.shape[0])
