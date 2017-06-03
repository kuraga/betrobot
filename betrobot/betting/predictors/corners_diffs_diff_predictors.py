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

    _pick = [ '_crosses_diffs_diff_predictor', '_saved_shots_diffs_diff_predictor' ]


    def __init__(self, *args, **kwargs):
         super().__init__()

         self._crosses_diffs_diff_predictor = DiffsDiffPredictor(*args, **kwargs)
         self._saved_shots_diffs_diff_predictor = DiffsDiffPredictor(*args, **kwargs)


    def _predict(self, fitteds, betcity_match):
         [ crosses_diffs_diff_fitted, saved_shots_diffs_diff_fitted ] = fitteds

         crosses_diffs_diff_prediction = self._crosses_diffs_diff_predictor._predict([ crosses_diffs_diff_fitted ], betcity_match)
         if crosses_diffs_diff_prediction is None:
             return None
         saved_shots_diffs_diff_prediction = self._saved_shots_diffs_diff_predictor._predict([ saved_shots_diffs_diff_fitted ], betcity_match)
         if saved_shots_diffs_diff_prediction is None:
             return None

         # Формула:
         # corners = 0.167*crosses + 0.224*saved_shots + 0.9
         crosses_coef = 0.167
         saved_shots_coef = 0.224

         corners_diffs_diff_prediction = crosses_coef * crosses_diffs_diff_prediction + saved_shots_coef * saved_shots_diffs_diff_prediction
 
         return corners_diffs_diff_prediction


    def _get_runtime_strs(self):
        return [
            '_crosses_diffs_diff_predictor=%s' % (str(self._crosses_diffs_diff_predictor),),
            '_saved_shots_diffs_diff_predictor=%s' % (str(self._saved_shots_diffs_diff_predictor),)
        ]
