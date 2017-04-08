import pymongo
from betrobot.util.pickable import Pickable


class Sampler(Pickable):

    def sample(self):
        raise NotImplementedError()
