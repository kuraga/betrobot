from betrobot.betting.proposer import Proposer


class ResultProposer(Proposer):

    _pick = [ 'min_margin' ]


    # TODO: min_margin - перенести на уровень выше
    def __init__(self, *args, min_margin=1, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_margin = min_margin


    def propose(self, bets, match_header, result_prediction=None, **kwargs):
        if 'data' not in kwargs:
            kwargs['data'] = {}
        kwargs['data']['result_prediction'] = result_prediction

        super().propose(bets, match_header, **kwargs)


    def _get_init_strs(self):
        return [
            'min_margin=%.2f' % (self.min_margin,)
        ]
