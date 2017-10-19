import numpy as np
import scipy
import scipy.stats
from betrobot.betting.predictor import Predictor


class ProbabilitiesViaResultPredictor(Predictor):

    _pick = [ 'result_predictor' ]


    def __init__(self, result_predictor, **kwargs):
         super().__init__(**kwargs)

         self.result_predictor = result_predictor


    def _predict(self, fitteds, match_header, **kwargs):
        result_prediction = self.result_predictor._predict(fitteds, match_header, **kwargs)
        if result_prediction is None:
            return None

        (events_home_count_prediction, events_away_count_prediction) = result_prediction

        # TODO: Параметризовать
        x = np.arange(0, 20)
        pmf_home = scipy.stats.poisson(events_home_count_prediction).pmf(x)
        pmf_away = scipy.stats.poisson(events_away_count_prediction).pmf(x)
        probabilities_prediction = np.outer(pmf_home, pmf_away)

        return probabilities_prediction


    def _get_init_strs(self):
        return [
            'result_predictor=%s' % (str(self.result_predictor),)
        ]
