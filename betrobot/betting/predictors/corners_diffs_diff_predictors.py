from betrobot.betting.predictor import Predictor
from betrobot.betting.predictors.match_predictor_mixins import CornersMatchPredictorMixin
from betrobot.betting.predictors.diffs_diff_predictor import DiffsDiffPredictor


class CornersDiffsDiffPredictor(CornersMatchPredictorMixin, Predictor):

    _pick = [ '_corners_diffs_diff_predictor' ]


    def __init__(self, *args, **kwargs):
         super().__init__()

         self._corners_diffs_diff_predictor = DiffsDiffPredictor(*args, **kwargs)


    def _predict(self, fitteds, betcity_match):
         [ corners_diffs_diff_fitted ] = fitteds

         corners_diffs_diff_prediction = self._corners_diffs_diff_predictor._predict([ corners_diffs_diff_fitted ], betcity_match)
 
         return corners_diffs_diff_prediction


    def _get_runtime_strs(self):
        return [
            '_corners_diffs_diff_predictor=%s' % (str(self._corners_diffs_diff_predictor),)
        ]


class CornersViaPassesDiffsDiffPredictor(CornersMatchPredictorMixin, Predictor):

    _pick = [ '_crosses_diffs_diff_predictor', '_shots_diffs_diff_predictor' ]


    def __init__(self, *args, **kwargs):
         super().__init__()

         self._crosses_diffs_diff_predictor = DiffsDiffPredictor(*args, **kwargs)
         self._shots_diffs_diff_predictor = DiffsDiffPredictor(*args, **kwargs)


    def _predict(self, fitteds, betcity_match):
         [ crosses_diffs_diff_fitted, shots_diffs_diff_fitted ] = fitteds

         crosses_diffs_diff_prediction = self._crosses_diffs_diff_predictor._predict([ crosses_diffs_diff_fitted ], betcity_match)
         if crosses_diffs_diff_prediction is None:
             return None
         shots_diffs_diff_prediction = self._shots_diffs_diff_predictor._predict([ shots_diffs_diff_fitted ], betcity_match)
         if shots_diffs_diff_prediction is None:
             return None

         # Формула:
         # corners = 0.187*crosses + 0.119*shots - 0.24
         crosses_coef = 0.187
         shots_coef = 0.119

         corners_diffs_diff_prediction = crosses_coef * crosses_diffs_diff_prediction + shots_coef * shots_diffs_diff_prediction
 
         return corners_diffs_diff_prediction


    def _get_runtime_strs(self):
        return [
            '_crosses_diffs_diff_predictor=%s' % (str(self._crosses_diffs_diff_predictor),),
            '_shots_diffs_diff_predictor=%s' % (str(self._shots_diffs_diff_predictor),)
        ]
