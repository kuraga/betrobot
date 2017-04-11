from betrobot.util.pickable import Pickable


class Fitter(Pickable):

    _pick = [ 'is_fitted' ]


    def __init__(self):
        super().__init__()

        self.clean()


    def clean(self):
        self.is_fitted = False
        self._clean()


    def _clean(self):
        pass


    def fit(self, **kwargs):
        self.clean()

        self._fit(**kwargs)

        self.is_fitted = True


    def _fit(self, **kwargs):
        raise NotImplementedError()
