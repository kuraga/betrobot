from betting.provider import Provider


class SampleFitPredictProposeProvider(Provider):

    def __init__(self, train_sampler, fitter, predictor, proposers_data):
        self.train_sampler = train_sampler
        self.fitter = fitter
        self.predictor = predictor
        self.proposers_data = proposers_data

        Provider.__init__(self)


    def prepare(self):
       self._fitted_data = self.fitter.fit(self.train_sampler)


    def handle(self, betcity_match, whoscored_match=None):
       prediction = self.predictor.predict(betcity_match, self._fitted_data)
       for proposer_data in self.proposers_data:
           proposer_data['proposer'].handle(betcity_match, prediction, whoscored_match=whoscored_match)
