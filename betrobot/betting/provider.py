import uuid
import os
import pickle
from betrobot.util.pickable import Pickable


class Provider(Pickable):

    _pick = [ 'uuid', 'description', 'fitter', 'refitters', 'predictor', 'proposers', 'matches_count' ]


    def __init__(self, fitter, refitters, predictor, proposers, description=None):
        super().__init__()

        self.description = description
        self.fitter = fitter
        self.refitters = refitters
        self.predictor = predictor
        self.proposers = proposers

        self.uuid = str(uuid.uuid4())
        self.matches_count = 0


    def handle(self, betcity_match, whoscored_match=None, predict_kwargs=None, handle_kwargs=None):
        if predict_kwargs is None:
            predict_kwargs = {}
        if handle_kwargs is None:
            handle_kwargs = {}

        if self.refitters is None:
            prediction = self.predictor.predict(self.fitter, betcity_match, **predict_kwargs)
        else:
            self.refitters[0].refit(self.fitter, betcity_match=betcity_match)
            for i in range(1, len(self.refitters)):
                self.refitters[i].refit(self.refitters[i-1], betcity_match=betcity_match)
            prediction = self.predictor.predict(self.refitters[-1], betcity_match, **predict_kwargs)

        for proposer in self.proposers:
            proposer.handle(betcity_match, prediction, whoscored_match=whoscored_match, **handle_kwargs)

        self.matches_count += 1


    # TODO: load


    def save(self):
        file_name = 'provider-%s.pkl' % (self.uuid,)
        file_path = os.path.join('data', 'providers', file_name)
        with open(file_path, 'wb') as f_out:
            pickle.dump(self, f_out)


    def clear_proposers(self):
        for proposer in self.proposers:
            proposer.clear()


    def __str__(self):
        return '%s(fitter=%s, refitters=%s, predictor=%s, proposers=%s)[uuid=%s]' % (self.__class__.__name__, str(self.fitter), str(', '.join(map(str, self.refitters))), str(self.predictor), str(', '.join(map(str, self.proposers))), self.uuid)
