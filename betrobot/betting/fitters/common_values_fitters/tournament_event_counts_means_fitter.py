from betrobot.betting.fitter import Fitter


class TournamentEventCountsMeansFitter(Fitter):

    _pick = [ 'tournament_event_home_counts_means', 'tournament_event_away_counts_means' ]


    def _clean(self):
        super()._clean()

        self.tournament_event_home_counts_means = None
        self.tournament_event_away_counts_means = None


    def _fit(self, **kwargs):
        statistic = self.previous_fitter.statistic.copy()

        self.tournament_event_home_counts_means = statistic.groupby('tournament_id')['events_home_count'].mean().to_dict()
        self.tournament_event_away_counts_means = statistic.groupby('tournament_id')['events_away_count'].mean().to_dict()


    def _get_runtime_strs(self):
        result = []

        if self.is_fitted:
            result += [
                'tournament_event_home_counts_means=%f' % (tournament_event_home_counts_means,),
                'tournament_event_away_counts_means=%f' % (tournament_event_away_counts_means,)
            ]

        return result
