import numpy as np
from betrobot.betting.proposers.match_proposers import MainMatchProposer


class GoalsFirstPeriodIndividualTotalsHomeGreaterProposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        (m, n) = probabilities.shape
        for total in np.arange(0, 10.5, 0.5):
            bet_pattern1 = (None, 'Индивидуальный тотал 1-й тайм', betcity_match['home'], 'Бол', total)
            bet_pattern2 = (None, 'Индивидуальный тотал 1-й тайм', '1', 'Бол', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(total))-i+1,0), n)]
            if probabilities[tuple(zip(*correct_results))].sum() / probabilities.sum() > confidence_level:
                self.propose(bet_pattern1, betcity_match, whoscored_match=whoscored_match)
                self.propose(bet_pattern2, betcity_match, whoscored_match=whoscored_match)


class GoalsFirstPeriodIndividualTotalsHomeLesserProposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        (m, n) = probabilities.shape
        for total in np.arange(0, 10.5, 0.5):
            bet_pattern1 = (None, 'Индивидуальный тотал 1-й тайм', betcity_match['home'], 'Мен', total)
            bet_pattern2 = (None, 'Индивидуальный тотал 1-й тайм', '1', 'Мен', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(total))-i,n))]
            if probabilities[tuple(zip(*correct_results))].sum() / probabilities.sum() > confidence_level:
                self.propose(bet_pattern1, betcity_match, whoscored_match=whoscored_match)
                self.propose(bet_pattern2, betcity_match, whoscored_match=whoscored_match)


class GoalsFirstPeriodIndividualTotalsAwayGreaterProposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        (m, n) = probabilities.shape
        for total in np.arange(0, 10.5, 0.5):
            bet_pattern1 = (None, 'Индивидуальный тотал 1-й тайм', betcity_match['away'], 'Бол', total)
            bet_pattern2 = (None, 'Индивидуальный тотал 1-й тайм', '2', 'Бол', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(total))-i+1,0), n)]
            if probabilities[tuple(zip(*correct_results))].sum() / probabilities.sum() > confidence_level:
                self.propose(bet_pattern1, betcity_match, whoscored_match=whoscored_match)
                self.propose(bet_pattern2, betcity_match, whoscored_match=whoscored_match)


class GoalsFirstPeriodIndividualTotalsAwayLesserProposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        (m, n) = probabilities.shape
        for total in np.arange(0, 10.5, 0.5):
            bet_pattern1 = (None, 'Индивидуальный тотал 1-й тайм', betcity_match['away'], 'Мен', total)
            bet_pattern2 = (None, 'Индивидуальный тотал 1-й тайм', '2', 'Мен', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(total))-i,n))]
            if probabilities[tuple(zip(*correct_results))].sum() / probabilities.sum() > confidence_level:
                self.propose(bet_pattern1, betcity_match, whoscored_match=whoscored_match)
                self.propose(bet_pattern2, betcity_match, whoscored_match=whoscored_match)


class GoalsSecondPeriodIndividualTotalsHomeGreaterProposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        (m, n) = probabilities.shape
        for total in np.arange(0, 10.5, 0.5):
            bet_pattern1 = (None, 'Индивидуальный тотал 2-й тайм', betcity_match['home'], 'Бол', total)
            bet_pattern2 = (None, 'Индивидуальный тотал 2-й тайм', '1', 'Бол', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(total))-i+1,0), n)]
            if probabilities[tuple(zip(*correct_results))].sum() / probabilities.sum() > confidence_level:
                self.propose(bet_pattern1, betcity_match, whoscored_match=whoscored_match)
                self.propose(bet_pattern2, betcity_match, whoscored_match=whoscored_match)


class GoalsSecondPeriodIndividualTotalsHomeLesserProposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        (m, n) = probabilities.shape
        for total in np.arange(0, 10.5, 0.5):
            bet_pattern1 = (None, 'Индивидуальный тотал 2-й тайм', betcity_match['home'], 'Мен', total)
            bet_pattern2 = (None, 'Индивидуальный тотал 2-й тайм', '1', 'Мен', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(total))-i,n))]
            if probabilities[tuple(zip(*correct_results))].sum() / probabilities.sum() > confidence_level:
                self.propose(bet_pattern1, betcity_match, whoscored_match=whoscored_match)
                self.propose(bet_pattern2, betcity_match, whoscored_match=whoscored_match)


class GoalsSecondPeriodIndividualTotalsAwayGreaterProposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        (m, n) = probabilities.shape
        for total in np.arange(0, 10.5, 0.5):
            bet_pattern1 = (None, 'Индивидуальный тотал 2-й тайм', betcity_match['away'], 'Бол', total)
            bet_pattern2 = (None, 'Индивидуальный тотал 2-й тайм', '2', 'Бол', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(max(int(np.ceil(total))-i+1,0), n)]
            if probabilities[tuple(zip(*correct_results))].sum() / probabilities.sum() > confidence_level:
                self.propose(bet_pattern1, betcity_match, whoscored_match=whoscored_match)
                self.propose(bet_pattern2, betcity_match, whoscored_match=whoscored_match)


class GoalsSecondPeriodIndividualTotalsAwayLesserProposer(MainMatchProposer):

    def _handle(self, betcity_match, probabilities, whoscored_match=None, confidence_level=0.6):
        (m, n) = probabilities.shape
        for total in np.arange(0, 10.5, 0.5):
            bet_pattern1 = (None, 'Индивидуальный тотал 2-й тайм', betcity_match['away'], 'Мен', total)
            bet_pattern2 = (None, 'Индивидуальный тотал 2-й тайм', '2', 'Мен', total)

            correct_results = [(i,j) for i in range(0, m) for j in range(0, min(int(np.floor(total))-i,n))]
            if probabilities[tuple(zip(*correct_results))].sum() / probabilities.sum() > confidence_level:
                self.propose(bet_pattern1, betcity_match, whoscored_match=whoscored_match)
                self.propose(bet_pattern2, betcity_match, whoscored_match=whoscored_match)
