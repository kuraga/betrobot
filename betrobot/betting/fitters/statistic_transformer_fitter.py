from betrobot.betting.fitter import Fitter


class StatisticTransformerFitter(Fitter):

    _pick = [ 'statistic_fitter', 'statistic' ]


    def _clean(self):
        super()._clean()

        self.statistic_fitter = None
        self.statistic = None


    def _prefit(self, statistic_fitter):
        self.statistic_fitter = statistic_fitter
