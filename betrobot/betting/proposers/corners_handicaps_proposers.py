import numpy as np
from betrobot.betting.proposers.match_proposers import CornersMatchProposer
from betrobot.util.sport_util import get_bets


class CornersHandicapsHomeProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('УГЛ', 'Фора', betcity_match['home'], None, '*')

        bets = get_bets(bet_pattern, betcity_match)
        for bet in bets:
            handicap = bet[4]
            predicted_probability = np.tril(probabilities, k=np.ceil(handicap)-1).sum()

            self.propose(bet, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersHandicapsAwayProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        bet_pattern = ('УГЛ', 'Фора', betcity_match['away'], None, '*')

        bets = get_bets(bet_pattern, betcity_match)
        for bet in bets:
            handicap = bet[4]
            predicted_probability = np.triu(probabilities, k=-(np.ceil(handicap)-1)).sum()

            self.propose(bet, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
