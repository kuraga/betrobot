import pymongo
from betrobot.util.pickable import Pickable


class Sampler(Pickable):

    _pick = [ '_db_name', '_matches_collection_name' ]


    def __init__(self, db_name='betrobot', matches_collection_name='matchesCleaned'):
        super().__init__()

        self._db_name = db_name
        self._matches_collection_name = matches_collection_name

        self._init_collection()


    def get_sample(self):
        raise NotImplementedError()


    def _on_unpickle(self):
        super()._on_unpickle()

        self._init_collection()


    def _init_collection(self):
        self._client = pymongo.MongoClient()
        self._db = self._client[self._db_name]
        self._matches_collection = self._db[self._matches_collection_name]
