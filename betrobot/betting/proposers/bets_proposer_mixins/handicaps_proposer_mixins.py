from betrobot.betting.sport_util import get_bets


class HandicapsHomeProposerMixin:

    def _get_bets(self, betcity_match):
        bet_pattern1 = ('*', 'Фора', betcity_match['home'], None, '*')
        bet_pattern2 = ('*', 'Дополнительные форы', betcity_match['home'], None, '*')
        return get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)


class HandicapsAwayProposerMixin:

    def _get_bets(self, betcity_match):
        bet_pattern1 = ('*', 'Фора', betcity_match['away'], None, '*')
        bet_pattern2 = ('*', 'Дополнительные форы', betcity_match['away'], None, '*')
        return get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)
