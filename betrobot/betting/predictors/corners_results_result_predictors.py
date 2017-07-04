from betrobot.betting.predictor import Predictor
from betrobot.betting.predictors.match_predictor_mixins import CornersMatchPredictorMixin
from betrobot.betting.predictors.results_result_predictor import ResultsResultPredictor


class CornersResultsResultsResultPredictor(CornersMatchPredictorMixin, Predictor):

    _pick = [ '_corners_results_result_predictor' ]


    def __init__(self):
         super().__init__()

         self._corners_results_result_predictor = ResultsResultPredictor()


    def _predict(self, fitteds, betcity_match, **kwargs):
         [ corners_results_fitted ] = fitteds

         corners_result_prediction = self._corners_results_result_predictor._predict([ corners_results_fitted ], betcity_match, **kwargs)
 
         return corners_result_prediction


    def _get_runtime_strs(self):
        return [
            '_corners_results_result_predictor=%s' % (str(self._corners_results_result_predictor),)
        ]


class CornersViaPassesResultsResultsResultPredictor(CornersMatchPredictorMixin, Predictor):

    _pick = [ '_crosses_results_result_predictor', '_shots_results_result_predictor' ]


    def __init__(self):
         super().__init__()

         self._crosses_results_result_predictor = ResultsResultPredictor()
         self._shots_results_result_predictor = ResultsResultPredictor()


    def _predict(self, fitteds, betcity_match, **kwargs):
         [ crosses_results_fitted, shots_results_fitted ] = fitteds

         crosses_result_prediction = self._crosses_results_result_predictor._predict([ crosses_results_fitted ], betcity_match, **kwargs)
         if crosses_result_prediction is None:
             return None
         shots_result_prediction = self._shots_results_result_predictor._predict([ shots_results_fitted ], betcity_match, **kwargs)
         if shots_result_prediction is None:
             return None

         (crosses_home_count_prediction, crosses_away_count_prediction) = crosses_result_prediction
         (shots_home_count_prediction, shots_away_count_prediction) = shots_result_prediction

         # Формула:
         # corners = 0.187*crosses + 0.119*shots - 0.24
         crosses_coef = 0.187
         shots_coef = 0.119
         intercept = -0.24

         corners_home_count_prediction = crosses_coef * crosses_home_count_prediction + shots_coef * shots_home_count_prediction + intercept
         corners_away_count_prediction = crosses_coef * crosses_away_count_prediction + shots_coef * shots_away_count_prediction + intercept
         corners_result_prediction = (corners_home_count_prediction, corners_away_count_prediction)

         return corners_result_prediction


    def _get_runtime_strs(self):
        return [
            '_crosses_results_result_predictor=%s' % (str(self._crosses_results_result_predictor),),
            '_shots_results_result_predictor=%s' % (str(self._shots_results_result_predictor),)
        ]
