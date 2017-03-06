import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./betting/providers')


from provider import Provider


class SampleFitPredictProposeProvider(Provider):
    def __init__(self, train_sampler, fitter, predictor, proposer):
        self._train_sampler = train_sampler
        self._fitter = fitter
        self._predictor = predictor
        self._proposer = proposer

        Provider.__init__(self)


    def prepare(self):
       self._fitted_data = self._fitter.fit(self._train_sampler)


    def handle(self, betcity_match, whoscored_match=None):
       prediction = self._predictor.predict(betcity_match, self._fitted_data)
       self._proposer.handle(betcity_match, prediction, whoscored_match=whoscored_match)
