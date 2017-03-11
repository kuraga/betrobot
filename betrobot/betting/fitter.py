from betrobot.util.pickable import Pickable


class Fitter(Pickable):

    _pick = []


    def fit(self, train_sampler, *args, **kwargs):
        return self._fit(train_sampler, *args, **kwargs)


    def _fit(self, train_sampler, *args, **kwargs):
       raise NotImplementedError()
