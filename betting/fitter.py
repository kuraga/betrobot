from util.pickable import Pickable


class Fitter(Pickable):

    _pick = []


    def fit(self, train_sampler):
       raise NotImplementedError()
