from betrobot.util.sport_util import is_betarch_match_corner


class CornersMatchPredictorMixin(object):

    def _predict(self, fitted, betcity_match):
        if not is_betarch_match_corner(betcity_match):
            return None

        return super()._predict(fitted, betcity_match)
