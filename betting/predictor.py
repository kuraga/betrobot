from util.pickable import Pickable


class Predictor(Pickable):

    _pick = []


    def predict(self, betcity_match, **kwargs):
        raise NotImplementedError()
