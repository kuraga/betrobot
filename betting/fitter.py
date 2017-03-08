from util.pickable import Pickable


class Fitter(Pickable):

    _pick = []


    def __init__(self):
        pass


    def fit(self, train_sampler):
       raise NotImplementedError()
