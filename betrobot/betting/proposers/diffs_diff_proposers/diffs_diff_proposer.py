from betrobot.betting.proposer import Proposer


class DiffsDiffProposer(Proposer):

    _pick = [ 'min_margin' ]


    # TODO: min_margin - перенести на уровень выше
    def __init__(self, *args, min_margin=3, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_margin = min_margin


    def propose(self, bets, match_header, diffs_diff_prediction, **kwargs):
        if 'data' not in kwargs:
            kwargs['data'] = {}
        kwargs['data']['diffs_diff_prediction'] = diffs_diff_prediction

        super().propose(bets, match_header, data=data, **kwargs)


    def _get_init_strs(self):
        return [
            'min_margin=%.2f' % (self.min_margin,)
        ]
