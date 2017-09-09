import numpy as np
from betrobot.betting.proposers.probabilities_proposers.probabilities_proposer import ProbabilityProposer


class HandicapsHomeProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, probabilities_prediction, match_header, **kwargs):
        handicap = bet[4]

        probability_prediction = np.tril(probabilities_prediction, k=np.ceil(handicap)-1).sum()

        self.propose(bet, match_header, **kwargs)


class HandicapsAwayProbabilityProposer(ProbabilityProposer):

    def _handle_bet(self, bet, probabilities_prediction, match_header, **kwargs):
        handicap = bet[4]

        probability_prediction = np.triu(probabilities_prediction, k=-(np.ceil(handicap)-1)).sum()

        self.propose(bet, match_header, **kwargs)
