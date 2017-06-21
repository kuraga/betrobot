from betrobot.betting.proposer import Proposer


class ResultProposer(Proposer):

    _pick = [ 'min_margin' ]


    # TODO: min_margin - перенести на уровень выше
    def __init__(self, *args, min_margin=1, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_margin = min_margin


    def propose(self, bet, betcity_match, result_prediction=None, **kwargs):
        data = kwargs.get('data', {})
        data['result_prediction'] = result_prediction

        super().propose(bet, betcity_match, data=data, **kwargs)


    def _get_init_strs(self):
        result = []
        if self.min_margin is not None:
            result.append( 'min_margin=%.2f' % (self.min_margin,) )
        return result
