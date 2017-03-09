from util.pickable import Pickable


class Predictor(Pickable):

    _pick = []


    def predict(self, betcity_match, **kwargs):
        return self._predict(betcity_match, **kwargs)


    def _predict(self, betcity_match, **kwargs):
        raise NotImplementedError()
