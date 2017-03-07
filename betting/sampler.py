import pymongo


class Sampler(object):
    def __init__(self, db_name='betrobot', matches_collection_name='matchesCleaned'):
        self._client = pymongo.MongoClient()
        self._db = self._client[db_name]
        self._matches_collection = self._db[matches_collection_name]


    def sample(self):
       raise NotImplementedError()
