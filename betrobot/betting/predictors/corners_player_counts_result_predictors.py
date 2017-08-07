from betrobot.betting.predictor import Predictor
from betrobot.betting.predictors.player_counts_result_predictor import PlayerCountsResultPredictor


class CornersPlayerCountsResultPredictor(Predictor):

    _pick = [ '_corners_player_counts_result_predictor' ]


    def __init__(self, *args, **kwargs):
         super().__init__()

         self._corners_player_counts_result_predictor = PlayerCountsResultPredictor(*args, **kwargs)


    def _predict(self, fitteds, match_header, **kwargs):
         [ corners_player_counts_fitted ] = fitteds

         corners_result_prediction = self._corners_player_counts_result_predictor._predict([ corners_player_counts_fitted ], match_header, **kwargs)
 
         return corners_result_prediction


    def _get_runtime_strs(self):
        return [
            '_corners_player_counts_result_predictor=%s' % (str(self._corners_player_counts_result_predictor),)
        ]


class CornersViaPassesPlayerCountsResultPredictor(Predictor):

    _pick = [ '_crosses_player_counts_result_predictor', '_shots_player_counts_result_predictor' ]


    def __init__(self, *args, **kwargs):
         super().__init__()

         self._crosses_player_counts_result_predictor = PlayerCountsResultPredictor(*args, **kwargs)
         self._shots_player_counts_result_predictor = PlayerCountsResultPredictor(*args, **kwargs)


    def _predict(self, fitteds, match_header, **kwargs):
         [ crosses_player_counts_fitted, shots_player_counts_fitted ] = fitteds

         crosses_result_prediction = self._crosses_player_counts_result_predictor._predict([ crosses_player_counts_fitted ], match_header, **kwargs)
         if crosses_result_prediction is None:
             return None
         shots_result_prediction = self._shots_player_counts_result_predictor._predict([ shots_player_counts_fitted ], match_header, **kwargs)
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
            '_crosses_player_counts_result_predictor=%s' % (str(self._crosses_player_counts_result_predictor),),
            '_shots_player_counts_result_predictor=%s' % (str(self._shots_player_counts_result_predictor),)
        ]
