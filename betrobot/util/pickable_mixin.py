from abc import ABCMeta
import os
import pickle
import uuid


class PickableMixin(metaclass=ABCMeta):

    _pick = [ 'uuid' ]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.uuid = str(uuid.uuid4())


    def __getstate__(self):
        self._on_pickle()

        pick_names = set()
        for class_ in self.__class__.__mro__:
            class_pick_names = getattr(class_, '_pick', [])
            pick_names.update(class_pick_names)

        state = { pick_name: getattr(self, pick_name) for pick_name in pick_names }

        return state


    def __setstate__(self, state):
        for name, value in state.items():
            setattr(self, name, value)

        self._on_unpickle()


    def _on_pickle(self):
        pass


    def _on_unpickle(self):
        pass


    @property
    def _pick_path(self):
        return os.path.join('data', 'pickables', self.__class__.__name__)


    @property
    def _pick_name(self):
        return self.uuid


    @property
    def _pick_file_path(self):
        return os.path.join(self._pick_path, '%s.pkl' % (self._pick_name,))


    @classmethod
    def load(cls):
        with open(self._pick_file_path, 'rb') as f_in:
            return pickle.load(f_in)


    def save(self):
        os.makedirs(self._pick_path, exist_ok=True)
        with open(self._pick_file_path, 'wb') as f_out:
            pickle.dump(self, f_out)
