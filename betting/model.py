import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')

import os
import pickle


class Model(object):
    _models = {}

    @classmethod
    def get(cls, model_name):
        if model_name not in cls._models:
            model_file_path = os.path.join('models', '%s.bin' % (model_name,))
            if not os.path.exists(model_file_path):
                return None
            with open(model_file_path, 'rb') as f_in:
                cls._models[model_name] = pickle.load(f_in)

        return cls._models[model_name]


    def __init__(self, name):
        self._name = name


    def save(self):
        model_file_path = os.path.join('models', '%s.bin' % (self._name,))
        with open(model_file_path, 'wb') as f_out:
            pickle.dump(self, f_out)
