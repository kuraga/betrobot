from betrobot.util.pickable import Pickable


class Predictor(Pickable):

    _pick = [ 'fitter' ]


    def __init__(self, fitter):
        super().__init__()

        self.fitter = fitter


    def predict(self, betcity_match, **kwargs):
        if not self.fitter.is_fitted:
            raise RuntimeError('Fitter is not fitted yet')

        return self._predict(betcity_match, **kwargs)


    def _predict(self, betcity_match, **kwargs):
        raise NotImplementedError()
