import numpy as np
from betrobot.betting.proposers.probability_proposers.probability_proposer import ProbabilityProposer


class FirstPeriodHandicapsHomeProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        handicap = bet[4]

        predicted_probability = np.tril(probabilities, k=np.ceil(handicap)-1).sum()

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class FirstPeriodHandicapsAwayProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        handicap = bet[4]

        predicted_probability = np.triu(probabilities, k=-(np.ceil(handicap)-1)).sum()

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class SecondPeriodHandicapsHomeProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        handicap = bet[4]

        predicted_probability = np.tril(probabilities, k=np.ceil(handicap)-1).sum()

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)


class SecondPeriodHandicapsAwayProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, betcity_match, probabilities, **kwargs):
        handicap = bet[4]

        predicted_probability = np.triu(probabilities, k=-(np.ceil(handicap)-1)).sum()

        self.propose(bet, betcity_match, predicted_probability=predicted_probability, **kwargs)
