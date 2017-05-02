import pymongo
from betrobot.util.pickable import Pickable


class Sampler(Pickable):

    _pick = [ 'db_name', 'collection_name' ]


    def __init__(self, db_name='betrobot', collection_name='matchesCleaned'):
        super().__init__()

        self.db_name = db_name
        self.collection_name = collection_name

        self._init_collection()


    def get_sample(self):
        raise NotImplementedError()


    def _on_unpickle(self):
        super()._on_unpickle()

        self._init_collection()


    def _init_collection(self):
        self._client = pymongo.MongoClient()
        self._db = self._client[self.db_name]
        self._matches_collection = self._db[self.collection_name]


    def __str__(self):
        return '%s(db_name="%s", collection_name="%s")' % (self.__class__.__name__, self.db_name, self.collection_name)
