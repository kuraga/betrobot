from betrobot.betting.predictor import Predictor
from betrobot.util.sport_util import is_betarch_match_corner, is_betarch_match_main


class MainMatchPredictor(Predictor):

    def predict(self, betcity_match, fitted_data):
        if not is_betarch_match_main(betcity_match):
            return

        return self._predict(betcity_match, fitted_data)


class CornersMatchPredictor(Predictor):

    def predict(self, betcity_match, fitted_data):
        if not is_betarch_match_corner(betcity_match):
            return

        return self._predict(betcity_match, fitted_data)
