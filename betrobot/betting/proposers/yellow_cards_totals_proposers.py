import numpy as np
from betrobot.betting.proposers.match_proposers import YellowCardsMatchProposer


class YellowCardsTotalsGreaterProposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        (m, n) = probabilities.shape
        for total in np.arange(0, 10.5, 0.5):
            bet_pattern1 = ('ЖК', 'Тотал', None, 'Бол', total)
            bet_pattern2 = ('ЖК', 'Дополнительные тоталы', None, 'Бол', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(total))-i+1,0), n)]
            if probabilities[tuple(zip(*correct_results))].sum() / probabilities.sum() > confidence_level:
                self.propose(bet_pattern1, betcity_match, whoscored_match=whoscored_match)
                self.propose(bet_pattern2, betcity_match, whoscored_match=whoscored_match)


class YellowCardsTotalsLesserProposer(YellowCardsMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        (m, n) = probabilities.shape
        for total in np.arange(0, 10.5, 0.5):
            bet_pattern1 = ('ЖК', 'Тотал', None, 'Мен', total)
            bet_pattern2 = ('ЖК', 'Дополнительные тоталы', None, 'Мен', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(total))-i,n))]
            if probabilities[tuple(zip(*correct_results))].sum() / probabilities.sum() > confidence_level:
                self.propose(bet_pattern1, betcity_match, whoscored_match=whoscored_match)
                self.propose(bet_pattern2, betcity_match, whoscored_match=whoscored_match)
