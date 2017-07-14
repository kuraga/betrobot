from betrobot.betting.fitter import Fitter
from betrobot.betting.sport_util import get_teams_tournaments_countries_value


class DiffsFitter(Fitter):

    _pick = [ 'home', 'away', 'events_home_diffs', 'events_away_diffs' ]


    def _clean(self):
        super()._clean()

        self.home = None
        self.away = None
        self.events_home_diffs = None
        self.events_away_diffs = None


    def _fit(self, match_header, **kwargs):
        statistic = self.previous_fitter.statistic
        if statistic.shape[0] == 0:
            return

        self.home = get_teams_tournaments_countries_value('betcityName', match_header['home'], 'whoscoredName')
        self.away = get_teams_tournaments_countries_value('betcityName', match_header['away'], 'whoscoredName')
        if self.home is None or self.away is None:
            return

        # Статистика матчей, где match_header['home'] тоже была хозяйкой
        home_data = statistic[ statistic['home'] == self.home ].sort_values('date', ascending=False)
        if home_data.shape[0] == 0:
            return
        # Статистика матчей, где match_header['away'] тоже была гостьей
        away_data = statistic[ statistic['away'] == self.away ].sort_values('date', ascending=False)
        if away_data.shape[0] == 0:
            return

        self.events_home_diffs = (home_data['events_home_count'] - home_data['events_away_count']).values
        self.events_away_diffs = (away_data['events_home_count'] - away_data['events_away_count']).values
