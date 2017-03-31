import numpy as np
from betrobot.betting.proposers.match_proposers import CornersMatchProposer


class CornersFirstPeriodIndividualTotalsHomeGreaterProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('УГЛ', 'Индивидуальный тотал 1-й тайм', betcity_match['home'], 'Бол', total)
            bet_pattern2 = ('УГЛ', 'Индивидуальный тотал 1-й тайм', '1', 'Бол', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(total))-i+1,0), n)]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()
            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersFirstPeriodIndividualTotalsHomeLesserProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('УГЛ', 'Индивидуальный тотал 1-й тайм', betcity_match['home'], 'Мен', total)
            bet_pattern2 = ('УГЛ', 'Индивидуальный тотал 1-й тайм', '1', 'Мен', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(total))-i,n))]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()
            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersFirstPeriodIndividualTotalsAwayGreaterProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('УГЛ', 'Индивидуальный тотал 1-й тайм', betcity_match['away'], 'Бол', total)
            bet_pattern2 = ('УГЛ', 'Индивидуальный тотал 1-й тайм', '2', 'Бол', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(total))-i+1,0), n)]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()
            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersFirstPeriodIndividualTotalsAwayLesserProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('УГЛ', 'Индивидуальный тотал 1-й тайм', betcity_match['away'], 'Мен', total)
            bet_pattern2 = ('УГЛ', 'Индивидуальный тотал 1-й тайм', '2', 'Мен', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(total))-i,n))]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()
            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersSecondPeriodIndividualTotalsHomeGreaterProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('УГЛ', 'Индивидуальный тотал 2-й тайм', betcity_match['home'], 'Бол', total)
            bet_pattern2 = ('УГЛ', 'Индивидуальный тотал 2-й тайм', '1', 'Бол', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(total))-i+1,0), n)]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()
            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersSecondPeriodIndividualTotalsHomeLesserProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('УГЛ', 'Индивидуальный тотал 2-й тайм', betcity_match['home'], 'Мен', total)
            bet_pattern2 = ('УГЛ', 'Индивидуальный тотал 2-й тайм', '1', 'Мен', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(total))-i,n))]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()

            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersSecondPeriodIndividualTotalsAwayGreaterProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('УГЛ', 'Индивидуальный тотал 2-й тайм', betcity_match['away'], 'Бол', total)
            bet_pattern2 = ('УГЛ', 'Индивидуальный тотал 2-й тайм', '2', 'Бол', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(total))-i+1,0), n)]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()

            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class CornersSecondPeriodIndividualTotalsAwayLesserProposer(CornersMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('УГЛ', 'Индивидуальный тотал 2-й тайм', betcity_match['away'], 'Мен', total)
            bet_pattern2 = ('УГЛ', 'Индивидуальный тотал 2-й тайм', '2', 'Мен', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(total))-i,n))]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()

            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
