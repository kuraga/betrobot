import uuid
import pickle
from betrobot.util.pickable import Pickable


class Provider(Pickable):

    _pick = [ 'uuid', 'name', 'description', 'train_sampler', 'fitter', 'predictor', 'proposers_data', 'is_fitted', '_fitted_data' ]


    def __init__(self, name, description, train_sampler=None, fitter=None, fitted_data=None, predictor=None, proposers_data=None):
        if fitter is not None and fitted_data is not None:
            raise ValueError("Pass 'fitter' or 'fitted_data' argument but not not both")

        self.uuid = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.train_sampler = train_sampler
        self.fitter = fitter
        self.predictor = predictor
        self.proposers_data = proposers_data

        if fitted_data is not None:
            self.is_fitted = True
            self._fitted_data = fitted_data
        else:
            self.is_fitted = False
            self._fitted_data = None

        super().__init__()


    def fit(self, force=False):
        if force or not self.is_fitted:
            self._fitted_data = self.fitter.fit(self.train_sampler)
            self.is_fitted = True


    @property
    def fitted_data(self):
        if not self.is_fitted:
           raise RuntimeError('Not fitted yet')

        return self._fitted_data


    def set_fitted_data(self, fitted_data):
        self._fitted_data = fitted_data
        self.is_fitted = True


    def handle(self, betcity_match, whoscored_match=None):
        if not self.is_fitted:
            raise RuntimeError('Not fitted yet')

        prediction = self.predictor.predict(betcity_match, self._fitted_data)

        for proposer_data in self.proposers_data:
            proposer_data['proposer'].handle(betcity_match, prediction, whoscored_match=whoscored_match)


    # TODO: save, load
