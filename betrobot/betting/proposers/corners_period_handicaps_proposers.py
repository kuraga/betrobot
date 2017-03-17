import numpy as np
from betrobot.betting.proposers.match_proposers import CornersMatchProposer
from betrobot.util.sport_util import get_bets


class CornersFirstPeriodHandicapsHomeProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        bet_pattern1 = (None, 'Исходы по таймам (1-й тайм)', 'Фора', betcity_match['home'], '*')
        bet_pattern2 = (None, 'Исходы по таймам (1-й тайм)', 'Фора', '1', '*')
        bets = get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)
        for bet in bets:
            handicap = bet[4]
            if np.tril(probabilities, k=np.ceil(handicap)-1).sum() / probabilities.sum() > confidence_level:
                self.propose(bet, betcity_match, whoscored_match=whoscored_match)


class CornersFirstPeriodHandicapsAwayProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        bet_pattern1 = (None, 'Исходы по таймам (1-й тайм)', 'Фора', betcity_match['away'], '*')
        bet_pattern2 = (None, 'Исходы по таймам (1-й тайм)', 'Фора', '2', '*')
        bets = get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)
        for bet in bets:
            handicap = bet[4]
            if np.triu(probabilities, k=np.floor(handicap)-1).sum() / probabilities.sum() > confidence_level:
                self.propose(bet, betcity_match, whoscored_match=whoscored_match)


class CornersSecondPeriodHandicapsHomeProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        bet_pattern1 = (None, 'Исходы по таймам (2-й тайм)', 'Фора', betcity_match['home'], '*')
        bet_pattern2 = (None, 'Исходы по таймам (2-й тайм)', 'Фора', '1', '*')
        bets = get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)
        for bet in bets:
            handicap = bet[4]
            if np.tril(probabilities, k=np.ceil(handicap)-1).sum() / probabilities.sum() > confidence_level:
                self.propose(bet, betcity_match, whoscored_match=whoscored_match)


class CornersSecondPeriodHandicapsAwayProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        bet_pattern1 = (None, 'Исходы по таймам (2-й тайм)', 'Фора', betcity_match['away'], '*')
        bet_pattern2 = (None, 'Исходы по таймам (2-й тайм)', 'Фора', '2', '*')
        bets = get_bets(bet_pattern1, betcity_match) + get_bets(bet_pattern2, betcity_match)
        for bet in bets:
            handicap = bet[4]
            if np.triu(probabilities, k=np.floor(handicap)-1).sum() / probabilities.sum() > confidence_level:
                self.propose(bet, betcity_match, whoscored_match=whoscored_match)
