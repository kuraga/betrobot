from betrobot.betting.proposer import Proposer


class DiffsDiffProposer(Proposer):

    # TODO: min_margin - перенести на уровень выше?
    _pick = [ 'min_margin' ]


    def __init__(self, *args, min_margin=3, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_margin = min_margin


    def propose(self, bet, betcity_match, diffs_diff_prediction=None, **kwargs):
        data = kwargs.get('data', {})
        data['diffs_diff_prediction'] = diffs_diff_prediction

        super().propose(bet, betcity_match, data=data, **kwargs)


    def _get_init_strs(self):
        return [
            'min_margin=%.2f' % (self.min_margin,)
        ]
