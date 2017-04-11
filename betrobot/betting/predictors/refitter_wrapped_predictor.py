from betrobot.betting.predictor import Predictor


class RefitterWrappedPredictor(Predictor):

    _pick = [ 'fitter', 'predictor' ]


    def __init__(self, fitter, predictor_class):
        super().__init__(fitter)

        self.predictor = predictor_class(self.fitter)


    def predict(self, betcity_match, **kwargs):
        self.fitter.fit(betcity_match=betcity_match)

        return self.predictor.predict(betcity_match, **kwargs)
