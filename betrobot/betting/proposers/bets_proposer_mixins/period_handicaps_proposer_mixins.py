from betrobot.util.sport_util import get_bets


class FirstPeriodHandicapsHomeProposerMixin(object):

    def _get_bets(self, betcity_match):
        bet_pattern1 = ('*', 'Исходы по таймам (1-й тайм)', 'Фора', betcity_match['home'], '*')
        bet_pattern2 = ('*', 'Исходы по таймам (1-й тайм)', 'Дополнительные форы', betcity_match['home'], '*')
        return get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)


class FirstPeriodHandicapsAwayProposerMixin(object):

    def _get_bets(self, betcity_match):
        bet_pattern1 = ('*', 'Исходы по таймам (1-й тайм)', 'Фора', betcity_match['away'], '*')
        bet_pattern2 = ('*', 'Исходы по таймам (1-й тайм)', 'Дополнительные форы', betcity_match['away'], '*')
        return get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)


class SecondPeriodHandicapsHomeProposerMixin(object):

    def _get_bets(self, betcity_match):
        bet_pattern1 = ('*', 'Исходы по таймам (2-й тайм)', 'Фора', betcity_match['home'], '*')
        bet_pattern2 = ('*', 'Исходы по таймам (2-й тайм)', 'Дополнительные форы', betcity_match['home'], '*')
        return get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)


class SecondPeriodHandicapsAwayProposerMixin(object):

    def _get_bets(self, betcity_match):
        bet_pattern1 = ('*', 'Исходы по таймам (2-й тайм)', 'Фора', betcity_match['away'], '*')
        bet_pattern2 = ('*', 'Исходы по таймам (2-й тайм)', 'Дополнительные форы', betcity_match['away'], '*')
        return get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)
