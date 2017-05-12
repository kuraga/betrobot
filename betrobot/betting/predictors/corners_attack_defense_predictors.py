import numpy as np
import scipy
import scipy.signal
from betrobot.betting.predictors.match_predictors import CornersMatchPredictor
from betrobot.betting.predictors.attack_defense_predictor import AttackDefensePredictor


class CornersResultProbabilitiesAttackDefensePredictor(CornersMatchPredictor):

    _pick = [ '_corners_attack_defense_predictor' ]


    def __init__(self):
         super().__init__()

         self._corners_attack_defense_predictor = AttackDefensePredictor()


    def _predict(self, fitteds, betcity_match):
         return self._corners_attack_defense_predictor._predict(fitteds, betcity_match)


class CornersViaPassesResultProbabilitiesAttackDefensePredictor(CornersMatchPredictor):

    _pick = [ '_crosses_attack_defense_predictor', '_saved_shots_attack_defense_predictor' ]


    def __init__(self):
         super().__init__()

         self._crosses_attack_defense_predictor = AttackDefensePredictor()
         self._saved_shots_attack_defense_predictor = AttackDefensePredictor()


    def _predict(self, fitteds, betcity_match):
         [ crosses_attack_defense_fitted, saved_shots_attack_defense_fitted ] = fitteds

         crosses_prediction = self._crosses_attack_defense_predictor._predict([ crosses_attack_defense_fitted ], betcity_match)
         saved_shots_prediction = self._saved_shots_attack_defense_predictor._predict([ saved_shots_attack_defense_fitted ], betcity_match)
         if crosses_prediction is None or saved_shots_prediction is None:
             return
  
         if crosses_prediction.shape != saved_shots_prediction.shape:
             raise RuntimeError('Shapes of prediction matrices have to be the same!')
 
         crosses_prediction_vector = crosses_prediction.flatten()
         saved_shots_prediction_vector = saved_shots_prediction.flatten()
         domain = np.arange(0, len(crosses_prediction_vector))
         crosses_prediction_pdf = scipy.interpolate.interp1d(domain, crosses_prediction_vector, bounds_error=False, fill_value=0)
         saved_shots_prediction_pdf = scipy.interpolate.interp1d(domain, saved_shots_prediction_vector, bounds_error=False, fill_value=0)
 
         # Формула:
         # corners = 0.167*crosses + 0.224*saved_shots + 0.9
         crosses_coef = 0.167
         saved_shots_coef = 0.224
         intercept = 0.9
 
         corners_prediction_vector = scipy.signal.convolve(crosses_prediction_vector, crosses_prediction_pdf( (domain-intercept-crosses_coef*crosses_prediction_vector)/saved_shots_coef ), mode='same')
         corners_prediction_vector = corners_prediction_vector / corners_prediction_vector.sum()
 
         corners_prediction = corners_prediction_vector.reshape(crosses_prediction.shape)
 
         return corners_prediction
