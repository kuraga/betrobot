import numpy as np


class FirstPeriodIndividualTotalsHomeGreaterProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['home'], 'Бол', individual_total)
            bet_pattern2 = ('*', 'Индивидуальный тотал 1-й тайм', '1', 'Бол', individual_total)

            correct_results = [(i,j) for i in range(int(np.ceil(individual_total)), m) for j in range(0, n)]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()

            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class FirstPeriodIndividualTotalsHomeLesserProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['home'], 'Мен', individual_total)
            bet_pattern2 = ('*', 'Индивидуальный тотал 1-й тайм', '1', 'Мен', individual_total)

            correct_results = [(i,j) for i in range(0, int(np.floor(individual_total))) for j in range(0, n)]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()

            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class FirstPeriodIndividualTotalsAwayGreaterProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['away'], 'Бол', individual_total)
            bet_pattern2 = ('*', 'Индивидуальный тотал 1-й тайм', '2', 'Бол', individual_total)

            correct_results = [(i,j) for i in range(0, m) for j in range(int(np.ceil(individual_total)), n)]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()

            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class FirstPeriodIndividualTotalsAwayLesserProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['away'], 'Мен', individual_total)
            bet_pattern2 = ('*', 'Индивидуальный тотал 1-й тайм', '2', 'Мен', individual_total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, int(np.floor(individual_total)))]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()

            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class SecondPeriodIndividualTotalsHomeGreaterProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['home'], 'Бол', individual_total)
            bet_pattern2 = ('*', 'Индивидуальный тотал 2-й тайм', '1', 'Бол', individual_total)

            correct_results = [(i,j) for i in range(int(np.ceil(individual_total)), m) for j in range(0, n)]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()

            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class SecondPeriodIndividualTotalsHomeLesserProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['home'], 'Мен', individual_total)
            bet_pattern2 = ('*', 'Индивидуальный тотал 2-й тайм', '1', 'Мен', individual_total)

            correct_results = [(i,j) for i in range(0, int(np.floor(individual_total))) for j in range(0, n)]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()

            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class SecondPeriodIndividualTotalsAwayGreaterProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['away'], 'Бол', individual_total)
            bet_pattern2 = ('*', 'Индивидуальный тотал 2-й тайм', '2', 'Бол', individual_total)

            correct_results = [(i,j) for i in range(0, m) for j in range(int(np.ceil(individual_total)), n)]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()

            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)


class SecondPeriodIndividualTotalsAwayLesserProposer(object):

    def _handle(self, betcity_match, probabilities, whoscored_match=None):
        (m, n) = probabilities.shape
        for individual_total in np.arange(0, 20.5, 0.5):
            bet_pattern1 = ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['away'], 'Мен', individual_total)
            bet_pattern2 = ('*', 'Индивидуальный тотал 2-й тайм', '2', 'Мен', individual_total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, int(np.floor(individual_total)))]
            predicted_probability = probabilities[tuple(zip(*correct_results))].sum()

            self.propose(bet_pattern1, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
            self.propose(bet_pattern2, betcity_match, 1/predicted_probability, whoscored_match=whoscored_match)
