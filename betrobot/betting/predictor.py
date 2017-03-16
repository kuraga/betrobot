from betrobot.util.pickable import Pickable


class Predictor(Pickable):

    _pick = []


    def predict(self, betcity_match, fitted_datas, **kwargs):
        return self._predict(betcity_match, fitted_datas, **kwargs)


    def _predict(self, betcity_match, fitted_datas, **kwargs):
        raise NotImplementedError()
