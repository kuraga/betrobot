from betrobot.betting.fitter import Fitter


class StatisticFitter(Fitter):

    _pick = [ 'statistic' ]


    def _clean(self):
        super()._clean()

        self.statistic = None
