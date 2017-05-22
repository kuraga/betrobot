from betrobot.util.sport_util import get_bets


class FirstPeriodResults1ProposerMixin(object):

    def _get_bets(self, betcity_match):
        bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', None, '1', None)
        return get_bets(bet_pattern, betcity_match)


class FirstPeriodResults1XProposerMixin(object):

    def _get_bets(self, betcity_match):
        bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', None, '1X', None)
        return get_bets(bet_pattern, betcity_match)


class FirstPeriodResultsX2ProposerMixin(object):

    def _get_bets(self, betcity_match):
        bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', None, 'X2', None)
        return get_bets(bet_pattern, betcity_match)


class FirstPeriodResults2ProposerMixin(object):

    def _get_bets(self, betcity_match):
        bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', None, '2', None)
        return get_bets(bet_pattern, betcity_match)


class SecondPeriodResults1ProposerMixin(object):

    def _get_bets(self, betcity_match):
        bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', None, '1', None)
        return get_bets(bet_pattern, betcity_match)


class SecondPeriodResults1XProposerMixin(object):

    def _get_bets(self, betcity_match):
        bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', None, '1X', None)
        return get_bets(bet_pattern, betcity_match)


class SecondPeriodResultsX2ProposerMixin(object):

    def _get_bets(self, betcity_match):
        bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', None, 'X2', None)
        return get_bets(bet_pattern, betcity_match)


class SecondPeriodResults2ProposerMixin(object):

    def _get_bets(self, betcity_match):
        bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', None, '2', None)
        return get_bets(bet_pattern, betcity_match)
