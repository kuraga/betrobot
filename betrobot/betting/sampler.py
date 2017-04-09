import pymongo
from betrobot.util.pickable import Pickable


class Sampler(Pickable):

    def get_sample(self):
        raise NotImplementedError()
