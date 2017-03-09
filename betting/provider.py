import uuid
import pickle
from util.pickable import Pickable


class Provider(Pickable):

    _pick = [ 'uuid', 'description', 'train_sampler', 'fitter', 'predictor', 'proposers_data', '_is_fitted', '_fitted_data' ]


    def __init__(self, description, train_sampler, fitter, predictor, proposers_data):
        self.uuid = str(uuid.uuid4())
        self.description = description
        self.train_sampler = train_sampler
        self.fitter = fitter
        self.predictor = predictor
        self.proposers_data = proposers_data

        self._is_fitted = False
        self._fitted_data = None

        super().__init__()


    def fit(self):
        self._fitted_data = self.fitter.fit(self.train_sampler)

        self._is_fitted = True


    def handle(self, betcity_match, whoscored_match=None):
       if not self._is_fitted:
           raise RuntimeError('Not fitted yet')

       prediction = self.predictor.predict(betcity_match, self._fitted_data)

       for proposer_data in self.proposers_data:
           proposer_data['proposer'].handle(betcity_match, prediction, whoscored_match=whoscored_match)
