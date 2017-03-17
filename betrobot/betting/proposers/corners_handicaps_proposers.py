import numpy as np
from betrobot.betting.proposers.match_proposers import CornersMatchProposer
from betrobot.util.sport_util import get_bets


class CornersHandicapsHomeProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        bet_pattern = ('УГЛ', 'Фора', betcity_match['home'], None, '*')
        bets = get_bets(bet_pattern, betcity_match)
        for bet in bets:
            handicap = bet[4]
            if np.tril(probabilities, k=np.ceil(handicap)-1).sum() / probabilities.sum() > confidence_level:
                self.propose(bet, betcity_match, whoscored_match=whoscored_match)


class CornersHandicapsAwayProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        bet_pattern = ('УГЛ', 'Фора', betcity_match['away'], None, '*')
        bets = get_bets(bet_pattern, betcity_match)
        for bet in bets:
            handicap = bet[4]
            if np.triu(probabilities, k=np.floor(handicap)-1).sum() / probabilities.sum() > confidence_level:
                self.propose(bet, betcity_match, whoscored_match=whoscored_match)
