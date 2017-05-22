from betrobot.betting.predictor import Predictor


class MatchRefittingPredictor(Predictor):

    _pick = [ 'predictor' ]


    def __init__(self, predictor):
        super().__init__()

        self.predictor = predictor


    def predict(self, refitters_pipe, betcity_match, **kwargs):
        if not refitters_pipe.is_fitted:
            refitters_pipe.refit(betcity_match, **kwargs)

        return self.predictor.predict(refitters_pipe.fitter, betcity_match, **kwargs)


    def _get_init_strs(self):
        return [
            'predictor=%s' % (str(self.predictor),)
        ]
