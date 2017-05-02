from betrobot.util.pickable import Pickable


class Refitter(Pickable):

    _pick = [ 'previous_fitter', 'is_fitted' ]


    def __init__(self):
        super().__init__()

        self.clean()


    def clean(self):
        self.is_fitted = False
        self._clean()


    def _clean(self):
        self.previous_fitter = None


    def refit(self, previous_fitter, **kwargs):
        self.clean()

        self.previous_fitter = previous_fitter
        self._refit(**kwargs)

        self.is_fitted = True


    def _refit(self, **kwargs):
        raise NotImplementedError()


    def __str__(self):
        return '%s()[is_fitted=%s]' % (self.__class__.__name__, str(self.is_fitted))
