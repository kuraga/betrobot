from betrobot.util.pickable import Pickable


class Predictor(Pickable):

    def predict(self, fitted, betcity_match, **kwargs):
        return self._predict(fitted, betcity_match, **kwargs)


    def _predict(self, fitter, betcity_match, **kwargs):
        raise NotImplementedError()


    def __str__(self):
        return '%s()' % (self.__class__.__name__,)
