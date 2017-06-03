import numpy as np
import scipy
import scipy.signal
from betrobot.betting.predictors.match_predictor_mixins import CornersMatchPredictorMixin
from betrobot.betting.predictor import Predictor
from betrobot.betting.predictors.attack_defense_predictor import AttackDefensePredictor
from betrobot.betting.predictors.probabilities_via_result_predictor import ProbabilitiesViaResultPredictor


class CornersAttackDefenseProbabilitiesPredictor(CornersMatchPredictorMixin, Predictor):

    def __init__(self, *args, **kwargs):
        super().__init__()

        corners_attack_defense_predictor = AttackDefensePredictor(*args, **kwargs)
        self._corners_probabilities_attack_defense_predictor = ProbabilitiesViaResultPredictor(corners_attack_defense_predictor)


    def _predict(self, fitteds, betcity_match):
        [ corners_events_mean_fitted, corners_matches_data_fitted ] = fitteds

        corners_probabilities_prediction = self._corners_probabilities_attack_defense_predictor.predict([ corners_events_mean_fitted, corners_matches_data_fitted ], betcity_match)

        return corners_probabilities_prediction


    def _get_runtime_strs(self):
        return [
            '_corners_probabilities_attack_defense_predictor=%s' % (str(self._corners_probabilities_attack_defense_predictor),)
        ]


class CornersViaPassesAttackDefenseProbabilitiesPredictor(CornersMatchPredictorMixin, Predictor):

    _pick = [ '_crosses_probabilities_attack_defense_predictor', '_saved_shots_probabilities_attack_defense_predictor' ]


    def __init__(self, *args, **kwargs):
         super().__init__()

         crosses_attack_defense_predictor = AttackDefensePredictor(*args, **kwargs)
         self._crosses_probabilities_attack_defense_predictor = ProbabilitiesViaResultPredictor(crosses_attack_defense_predictor)
         saved_shots_attack_defense_predictor = AttackDefensePredictor(*args, **kwargs)
         self._saved_shots_probabilities_attack_defense_predictor = ProbabilitiesViaResultPredictor(saved_shots_attack_defense_predictor)


    def _predict(self, fitteds, betcity_match):
         [ crosses_events_mean_fitted, crosses_matches_data_fitted, saved_shots_events_mean_fitted, saved_shots_matches_data_fitted ] = fitteds

         crosses_prediction = self._crosses_probabilities_attack_defense_predictor._predict([ crosses_events_mean_fitted, crosses_matches_data_fitted ], betcity_match)
         if crosses_prediction is None:
             return None

         saved_shots_prediction = self._saved_shots_probabilities_attack_defense_predictor._predict([ saved_shots_events_mean_fitted, saved_shots_matches_data_fitted ], betcity_match)
         if saved_shots_prediction is None:
             return None

         # TODO: Заменить на аналитический рассчет

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


    def _get_runtime_strs(self):
        return [
            '_crosses_probabilities_attack_defense_predictor=%s' % (str(self._crosses_probabilities_attack_defense_predictor),),
            '_saved_shots_probabilities_attack_defense_predictor=%s' % (str(self._saved_shots_probabilities_attack_defense_predictor),)
        ]
