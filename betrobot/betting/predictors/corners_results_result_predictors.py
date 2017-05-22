from betrobot.betting.predictor import Predictor
from betrobot.betting.predictors.match_predictor_mixins import CornersMatchPredictorMixin
from betrobot.betting.predictors.results_result_predictor import ResultsResultPredictor


class CornersResultsResultPredictor(CornersMatchPredictorMixin, Predictor):

    _pick = [ '_corners_results_predictor' ]


    def __init__(self):
         super().__init__()

         self._corners_results_predictor = ResultsResultPredictor()


    def _predict(self, fitteds, betcity_match):
         [ corners_results_fitted ] = fitteds

         corners_result_prediction = self._corners_results_predictor._predict([ corners_results_fitted ], betcity_match)
 
         return corners_result_prediction


class CornersViaPassesResultsResultPredictor(CornersMatchPredictorMixin, Predictor):

    _pick = [ '_crosses_results_predictor', '_saved_shots_results_predictor' ]


    def __init__(self):
         super().__init__()

         self._crosses_results_predictor = ResultsResultPredictor()
         self._saved_shots_results_predictor = ResultsResultPredictor()


    def _predict(self, fitteds, betcity_match):
         [ crosses_results_fitted, saved_shots_results_fitted ] = fitteds

         crosses_result_prediction = self._crosses_results_predictor._predict([ crosses_results_fitted ], betcity_match)
         if crosses_result_prediction is None:
             return None
         saved_shots_result_prediction = self._saved_shots_results_predictor._predict([ saved_shots_results_fitted ], betcity_match)
         if saved_shots_result_prediction is None:
             return None

         (crosses_home_count_prediction, crosses_away_count_prediction) = crosses_result_prediction
         (saved_shots_home_count_prediction, saved_shots_away_count_prediction) = saved_shots_result_prediction

         # Формула:
         # corners = 0.167*crosses + 0.224*saved_shots + 0.9
         crosses_coef = 0.167
         saved_shots_coef = 0.224
         intercept = 0.9

         corners_home_count_prediction = crosses_coef * crosses_home_count_prediction + saved_shots_coef * saved_shots_home_count_prediction + intercept
         corners_away_count_prediction = crosses_coef * crosses_away_count_prediction + saved_shots_coef * saved_shots_away_count_prediction + intercept
         corners_result_prediction = (corners_home_count_prediction, corners_away_count_prediction)

         return corners_result_prediction
