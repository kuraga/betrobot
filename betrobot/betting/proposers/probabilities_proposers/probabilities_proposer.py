from betrobot.betting.proposer import Proposer


class ProbabilityProposer(Proposer):

    _pick = [ 'predicted_threshold', 'ratio_threshold' ]


    def __init__(self, predicted_threshold=None, ratio_threshold=None, **kwargs):
        super().__init__(**kwargs)

        self.predicted_threshold = predicted_threshold
        self.ratio_threshold = ratio_threshold


    def propose(self, bets, match_header, probability_prediction, **kwargs):
        if probability_prediction <= 0:
            return

        predicted_bet_value = 1 / probability_prediction
        if self.predicted_threshold is not None and predicted_bet_value > self.predicted_threshold:
            return
        if self.ratio_threshold is not None and bet['value'] / predicted_bet_value < self.ratio_threshold:
            return

        super().propose(bets, match_header, **kwargs)


    def _get_init_strs(self):
        result = []

        if self.predicted_threshold is not None:
            result.append( 'predicted_threshold=%f' % (self.predicted_threshold,) )
        if self.ratio_threshold is not None:
            result.append( 'ratio_threshold=%f' % (self.ratio_threshold,) )

        return result
