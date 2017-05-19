import numpy as np
import scipy
import scipy.signal
from betrobot.betting.predictors.match_predictors import CornersMatchPredictor
from betrobot.betting.predictors.diffs_predictor import DiffsPredictor


class CornersViaPassesDiffsPredictor(CornersMatchPredictor):

    _pick = [ '_crosses_diffs_predictor', '_saved_shots_diffs_predictor' ]


    def __init__(self):
         super().__init__()

         self._crosses_diffs_predictor = DiffsPredictor()
         self._saved_shots_diffs_predictor = DiffsPredictor()


    def _predict(self, fitteds, betcity_match):
         [ crosses_diffs_fitted, saved_shots_diffs_fitted ] = fitteds

         crosses_prediction = self._crosses_diffs_predictor._predict([ crosses_diffs_fitted ], betcity_match)
         saved_shots_prediction = self._saved_shots_diffs_predictor._predict([ saved_shots_diffs_fitted ], betcity_match)
         if crosses_prediction is None or saved_shots_prediction is None:
             return
  
         # Формула:
         # corners = 0.167*crosses + 0.224*saved_shots + 0.9
         crosses_coef = 0.167
         saved_shots_coef = 0.224

         corners_diff_prediction = crosses_coef * crosses_prediction + saved_shots_coef * saved_shots_prediction
         # print(corners_diff_prediction, crosses_prediction, saved_shots_prediction)
 
         return corners_diff_prediction
