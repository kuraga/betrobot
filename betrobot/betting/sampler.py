from abc import ABCMeta, abstractmethod
import pymongo
from betrobot.util.pickable_mixin import PickableMixin
from betrobot.util.printable_mixin import PrintableMixin


class Sampler(PickableMixin, PrintableMixin, metaclass=ABCMeta):

    _pick = [ 'db_name', 'collection_name' ]


    def __init__(self, db_name='betrobot', collection_name='matches'):
        super().__init__()

        self.db_name = db_name
        self.collection_name = collection_name

        self._init_collection()


    @abstractmethod
    def get_sample(self):
        raise NotImplementedError()


    def _on_unpickle(self):
        super()._on_unpickle()

        self._init_collection()


    def _init_collection(self):
        self._client = pymongo.MongoClient()
        self._db = self._client[self.db_name]
        self._matches_collection = self._db[self.collection_name]


    def _get_runtime_strs(self):
        return [
            'db_name=%s' % (self.db_name,),
            'collection_name=%s' % (self.collection_name,)
        ]
