import numpy as np
from betrobot.betting.predictor import Predictor
from betrobot.betting.predictors.match_predictor_mixins import CornersMatchPredictorMixin
from betrobot.betting.predictors.attack_defense_predictor import AttackDefensePredictor


class CornersAttackDefenseResultPredictor(CornersMatchPredictorMixin, Predictor):

    _pick = [ '_corners_attack_defense_predictor' ]


    def __init__(self, *args, **kwargs):
         super().__init__()

         self._corners_attack_defense_predictor = AttackDefensePredictor(*args, **kwargs)


    def _predict(self, fitteds, betcity_match):
        [ corners_events_mean_fitted, corners_matches_data_fitted ] = fitteds

        corners_prediction = self._corners_attack_defense_predictor.predict([ corners_events_mean_fitted, corners_matches_data_fitted ], betcity_match)

        return corners_prediction


    def _get_runtime_strs(self):
        return [
            '_corners_attack_defense_predictor=%s' % (str(self._corners_attack_defense_predictor),)
        ]


class CornersViaPassesAttackDefenseResultPredictor(CornersMatchPredictorMixin, Predictor):

    _pick = [ '_crosses_attack_defense_predictor', '_saved_shots_attack_defense_predictor' ]


    def __init__(self, *args, **kwargs):
         super().__init__()

         self._crosses_attack_defense_predictor = AttackDefensePredictor(*args, **kwargs)
         self._saved_shots_attack_defense_predictor = AttackDefensePredictor(*args, **kwargs)


    def _predict(self, fitteds, betcity_match):
         [ crosses_events_mean_fitted, crosses_matches_data_fitted, saved_shots_events_mean_fitted, saved_shots_matches_data_fitted ] = fitteds

         crosses_prediction = self._crosses_attack_defense_predictor._predict([ crosses_events_mean_fitted, crosses_matches_data_fitted ], betcity_match)
         if crosses_prediction is None:
             return
         (crosses_home_prediction, crosses_away_prediction) = crosses_prediction

         saved_shots_prediction = self._saved_shots_attack_defense_predictor._predict([ saved_shots_events_mean_fitted, saved_shots_matches_data_fitted ], betcity_match)
         if saved_shots_prediction is None:
             return
         (saved_shots_home_prediction, saved_shots_away_prediction) = saved_shots_prediction

         # Формула:
         # corners = 0.167*crosses + 0.224*saved_shots + 0.9
         corners_home_prediction = 0.167*crosses_home_prediction + 0.224*saved_shots_home_prediction + 0.9
         corners_away_prediction = 0.167*crosses_away_prediction + 0.224*saved_shots_away_prediction + 0.9
         corners_prediction = (corners_home_prediction, corners_away_prediction)

         return corners_prediction


    def _get_runtime_strs(self):
        return [
            '_crosses_attack_defense_predictor=%s' % (str(self._crosses_attack_defense_predictor),),
            '_saved_shots_attack_defense_predictor=%s' % (str(self._saved_shots_attack_defense_predictor),)
        ]
