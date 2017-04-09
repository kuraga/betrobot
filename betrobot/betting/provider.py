import uuid
import pickle
from betrobot.util.pickable import Pickable
from betrobot.util.common_util import list_wrap


class Provider(Pickable):

    _pick = [ 'uuid', 'name', 'description', 'train_sampler', 'fitters', 'predictor', 'proposers_data', 'is_fitted', '_fitted_datas' ]


    def __init__(self, name, description, train_sampler=None, fitters=None, fitted_datas=None, predictor=None, proposers_data=None):
        super().__init__()

        if fitters is not None and fitted_datas is not None:
            raise ValueError("Pass 'fitters' or 'fitted_datas' argument but not not both")

        self.uuid = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.train_sampler = train_sampler
        self.fitters = list_wrap(fitters)
        self.predictor = predictor
        self.proposers_data = proposers_data

        if fitted_datas is not None:
            self.is_fitted = True
            self._fitted_datas = list_wrap(fitted_datas)
        else:
            self.is_fitted = False
            self._fitted_datas = None


    def fit(self, force=False):
        if force or not self.is_fitted:
            self._fitted_datas = [ self.fitter.fit(self.train_sampler) for fitter in self.fitters ]
            self.is_fitted = True


    @property
    def fitted_datas(self):
        if not self.is_fitted:
           raise RuntimeError('Not fitted yet')

        return self._fitted_datas


    def set_fitted_datas(self, fitted_datas):
        self._fitted_datas = list_wrap(fitted_datas)
        self.is_fitted = True


    def handle(self, betcity_match, whoscored_match=None):
        if not self.is_fitted:
            raise RuntimeError('Not fitted yet')

        prediction = self.predictor.predict(betcity_match, self._fitted_datas)

        for proposer_data in self.proposers_data:
            proposer_data['proposer'].handle(betcity_match, prediction, whoscored_match=whoscored_match)


    # TODO: save, load


    def clear_proposers(self):
        for proposer_data in self.proposers_data:
            proposer_data['proposer'].clear()
