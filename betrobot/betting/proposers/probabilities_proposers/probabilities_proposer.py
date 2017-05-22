from betrobot.betting.proposer import Proposer


class ProbabilityProposer(Proposer):

    _pick = [ 'predicted_threshold', 'ratio_threshold' ]


    def __init__(self, *args, predicted_threshold=None, ratio_threshold=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.predicted_threshold = predicted_threshold
        self.ratio_threshold = ratio_threshold


    def propose(self, bet, betcity_match, probability_prediction=None, **kwargs):
        if probability_prediction is None or probability_prediction <= 0:
            return
        data = kwargs.get('data', {})
        data['probability_prediction'] = probability_prediction

        predicted_bet_value = 1 / probability_prediction
        if self.predicted_threshold is not None and predicted_bet_value > self.predicted_threshold:
            return
        if self.ratio_threshold is not None and bet_value / predicted_bet_value < self.ratio_threshold:
            return

        super().propose(bet, betcity_match, data=data, **kwargs)


    def _get_init_strs(self):
        result = []
        if self.predicted_threshold is not None:
            strs.append( 'predicted_threshold=%.2f' % (self.predicted_threshold,) )
        if self.ratio_threshold is not None:
            strs.append( 'ratio_threshold=%.2f' % (self.ratio_threshold,) )
        return result
