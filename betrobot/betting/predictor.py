from betrobot.util.pickable import Pickable
from betrobot.util.printable import Printable


class Predictor(Pickable, Printable):

    def predict(self, fitted, betcity_match, **kwargs):
        return self._predict(fitted, betcity_match, **kwargs)


    def _predict(self, fitter, betcity_match, **kwargs):
        raise NotImplementedError()
