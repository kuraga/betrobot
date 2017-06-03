from betrobot.betting.predictor import Predictor
from betrobot.betting.predictors.match_predictor_mixins import CornersMatchPredictorMixin
from betrobot.betting.predictors.diffs_diff2_predictor import DiffsDiff2Predictor


class CornersDiffsDiff2Predictor(CornersMatchPredictorMixin, Predictor):

    _pick = [ '_corners_diffs2_predictor' ]


    def __init__(self, *args, **kwargs):
         super().__init__()

         self._corners_diffs2_predictor = DiffsDiff2Predictor(*args, **kwargs)


    def _predict(self, fitteds, betcity_match):
         [ corners_diffs_fitted ] = fitteds

         corners_diff2_prediction = self._corners_diffs2_predictor._predict([ corners_diffs_fitted ], betcity_match)
 
         return corners_diff2_prediction


    def _get_runtime_strs(self):
        return [
            '_corners_diffs2_predictor=%s' % (str(self._corners_diffs2_predictor),)
        ]
