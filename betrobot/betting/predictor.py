from betrobot.util.pickable import Pickable


class Predictor(Pickable):

    def predict(self, fitter, betcity_match, **kwargs):
        if not fitter.is_fitted:
            raise RuntimeError('Fitter is not fitted yet')

        return self._predict(fitter, betcity_match, **kwargs)


    def _predict(self, fitter, betcity_match, **kwargs):
        raise NotImplementedError()


    def __str__(self):
        return '%s()' % (self.__class__.__name__,)
