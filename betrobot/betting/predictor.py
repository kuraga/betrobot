from betrobot.util.pickable import Pickable


class Predictor(Pickable):

    _pick = []


    def predict(self, betcity_match, *args, **kwargs):
        return self._predict(betcity_match, **kwargs)


    def _predict(self, betcity_match, *args, **kwargs):
        raise NotImplementedError()
