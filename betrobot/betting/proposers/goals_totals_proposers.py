import numpy as np
from betrobot.betting.proposers.match_proposers import MainMatchProposer


class GoalsTotalsGreaterProposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = (None, 'Тотал', None, 'Бол', total)
            bet_pattern2 = (None, 'Дополнительные тоталы', None, 'Бол', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(total))-i+1,0), n)]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()

            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class GoalsTotalsLesserProposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = (None, 'Тотал', None, 'Мен', total)
            bet_pattern2 = (None, 'Дополнительные тоталы', None, 'Мен', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(total))-i,n))]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()

            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
