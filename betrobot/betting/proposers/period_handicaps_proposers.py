import numpy as np
from betrobot.util.sport_util import get_bets


class FirstPeriodHandicapsHomeProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', 'Фора', betcity_match['home'], '*')

        bets = get_bets(bet_pattern, betcity_match)
        for bet in bets:
            handicap = bet[4]
            predicted_probability = np.tril(probabilities, k=np.ceil(handicap)-1).sum()

            if predicted_probability > 0:
                self.propose(bet, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class FirstPeriodHandicapsAwayProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исходы по таймам (1-й тайм)', 'Фора', betcity_match['away'], '*')

        bets = get_bets(bet_pattern, betcity_match)
        for bet in bets:
            handicap = bet[4]
            predicted_probability = np.triu(probabilities, k=-(np.ceil(handicap)-1)).sum()

            if predicted_probability > 0:
                self.propose(bet, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class SecondPeriodHandicapsHomeProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', 'Фора', betcity_match['home'], '*')

        bets = get_bets(bet_pattern, betcity_match)
        for bet in bets:
            handicap = bet[4]
            predicted_probability = np.tril(probabilities, k=np.ceil(handicap)-1).sum()

            if predicted_probability > 0:
                self.propose(bet, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class SecondPeriodHandicapsAwayProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Исходы по таймам (2-й тайм)', 'Фора', betcity_match['away'], '*')

        bets = get_bets(bet_pattern, betcity_match)
        for bet in bets:
            handicap = bet[4]
            predicted_probability = np.triu(probabilities, k=-(np.ceil(handicap)-1)).sum()

            if predicted_probability > 0:
                self.propose(bet, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
