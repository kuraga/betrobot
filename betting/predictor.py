from util.pickable import Pickable


class Predictor(Pickable):

    _pick = []


    def __init__(self):
        pass


    def predict(self, betcity_match, **kwargs):
        raise NotImplementedError()
