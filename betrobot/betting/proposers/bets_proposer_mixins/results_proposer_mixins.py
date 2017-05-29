from betrobot.util.sport_util import get_bets


class Results1ProposerMixin:

    def _get_bets(self, betcity_match):
        bet_pattern = ('*', 'Исход', None, '1', None)
        return get_bets(bet_pattern, betcity_match)


class Results1XProposerMixin:

    def _get_bets(self, betcity_match):
        bet_pattern = ('*', 'Исход', None, '1X', None)
        return get_bets(bet_pattern, betcity_match)


class ResultsX2ProposerMixin:

    def _get_bets(self, betcity_match):
        bet_pattern = ('*', 'Исход', None, 'X2', None)
        return get_bets(bet_pattern, betcity_match)


class Results2ProposerMixin:

    def _get_bets(self, betcity_match):
        bet_pattern = ('*', 'Исход', None, '2', None)
        return get_bets(bet_pattern, betcity_match)
