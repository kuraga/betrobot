import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')


import pickle


class Provider(object):

    def __init__(self):
        pass


    def prepare(self):
        raise NotImplementedError()


    def handle(self, betcity_match, whoscored_match=None):
        raise NotImplementedError()


    @property
    def betting_sessions(self):
        return self._proposer.betting_sessions


    # TODO: Доработать
    def to_string(self):
        return self._proposer.to_string()
