from betrobot.betting.proposer import Proposer


class ProbabilityProposer(Proposer):

    _pick = [ 'predicted_threshold', 'ratio_threshold' ]


    def __init__(self, *args, predicted_threshold=None, ratio_threshold=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.predicted_threshold = predicted_threshold
        self.ratio_threshold = ratio_threshold


    def propose(self, bet, betcity_match, predicted_probability=None, **kwargs):
        if predicted_probability is None or predicted_probability <= 0:
            return
        data = kwargs.get('data', {})
        data['predicted_probability'] = predicted_probability

        predicted_bet_value = 1 / predicted_probability
        if self.predicted_threshold is not None and predicted_bet_value > self.predicted_threshold:
            return
        if self.ratio_threshold is not None and bet_value / predicted_bet_value < self.ratio_threshold:
            return

        super().propose(bet, betcity_match, data=data, **kwargs)
