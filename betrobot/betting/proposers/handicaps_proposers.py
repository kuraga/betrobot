from betrobot.util.sport_util import get_bets
import numpy as np


class HandicapsHomeProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern1 = ('*', 'Фора', betcity_match['home'], None, '*')
        bet_pattern2 = ('*', 'Дополнительные форы', betcity_match['home'], None, '*')

        bets = get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)
        for bet in bets:
            handicap = bet[4]
            predicted_probability = np.tril(probabilities, k=np.ceil(handicap)-1).sum()

            self.propose(bet, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class HandicapsAwayProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('*', 'Фора', betcity_match['away'], None, '*')
        bet_pattern2 = ('*', 'Дополнительные форы', betcity_match['away'], None, '*')

        bets = get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)
        for bet in bets:
            handicap = bet[4]
            predicted_probability = np.triu(probabilities, k=-(np.ceil(handicap)-1)).sum()

            self.propose(bet, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
