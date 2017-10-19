from betrobot.betting.predictor import Predictor
from betrobot.betting.predictors.diffs_diff_predictor import DiffsDiffPredictor
from betrobot.util.logging_util import get_logger


class CornersDiffsDiffPredictor(Predictor):

    _pick = [ '_corners_diffs_diff_predictor' ]


    def __init__(self, **kwargs):
         super().__init__()

         self._corners_diffs_diff_predictor = DiffsDiffPredictor(**kwargs)


    def _predict(self, fitteds, match_header, **kwargs):
         [ corners_diffs_diff_fitted ] = fitteds

         get_logger('prediction').info('Предсказываем разницу угловых...')
         corners_diffs_diff_prediction = self._corners_diffs_diff_predictor._predict([ corners_diffs_diff_fitted ], match_header, **kwargs)
         if corners_diffs_diff_prediction is None:
            get_logger('prediction').info('Алгоритм не выдал предсказание')
            return None
         get_logger('prediction').info('Предсказание разницы угловых: %.1f', corners_diffs_diff_prediction)

         return corners_diffs_diff_prediction


    def _get_runtime_strs(self):
        return [
            '_corners_diffs_diff_predictor=%s' % (str(self._corners_diffs_diff_predictor),)
        ]


class CornersViaPassesDiffsDiffPredictor(Predictor):

    _pick = [ '_crosses_diffs_diff_predictor', '_shots_diffs_diff_predictor' ]


    def __init__(self, **kwargs):
         super().__init__()

         self._crosses_diffs_diff_predictor = DiffsDiffPredictor(**kwargs)
         self._shots_diffs_diff_predictor = DiffsDiffPredictor(**kwargs)


    def _predict(self, fitteds, match_header, **kwargs):
         [ crosses_diffs_diff_fitted, shots_diffs_diff_fitted ] = fitteds

         crosses_diffs_diff_prediction = self._crosses_diffs_diff_predictor._predict([ crosses_diffs_diff_fitted ], match_header, **kwargs)
         if crosses_diffs_diff_prediction is None:
             return None

         shots_diffs_diff_prediction = self._shots_diffs_diff_predictor._predict([ shots_diffs_diff_fitted ], match_header, **kwargs)
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
