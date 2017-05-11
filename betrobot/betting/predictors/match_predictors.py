from betrobot.betting.predictor import Predictor
from betrobot.util.sport_util import is_betarch_match_main, is_betarch_match_corner, is_betarch_match_yellow_card


class MainMatchPredictor(Predictor):

    def _predict(self, fitted, betcity_match):
        if not is_betarch_match_main(betcity_match):
            return None

        return super()._predict(fitted, betcity_match)


class CornersMatchPredictor(Predictor):

    def _predict(self, fitted, betcity_match):
        if not is_betarch_match_corner(betcity_match):
            return None

        return super()._predict(fitted, betcity_match)


class YellowCardsMatchPredictor(Predictor):

    def _predict(self, fitted, betcity_match):
        if not is_betarch_match_yellow_card(betcity_match):
            return None

        return super()._predict(fitted, betcity_match)
