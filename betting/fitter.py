from util.pickable import Pickable


class Fitter(Pickable):

    _pick = []


    def fit(self, train_sampler, **kwargs):
        return self._fit(train_sampler, **kwargs)


    def _fit(self, train_sampler, **kwargs):
       raise NotImplementedError()
