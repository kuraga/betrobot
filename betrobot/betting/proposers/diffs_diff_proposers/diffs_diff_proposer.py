from betrobot.betting.proposer import Proposer


class DiffsDiffProposer(Proposer):

    # TODO: min_diffs_diff_for_win - перенести на уровень выше?
    _pick = [ 'min_diffs_diff_for_win' ]


    def __init__(self, *args, min_diffs_diff_for_win=3, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_diffs_diff_for_win = min_diffs_diff_for_win


    def propose(self, bet, betcity_match, diffs_diff_prediction=None, **kwargs):
        data = kwargs.get('data', {})
        data['diffs_diff_prediction'] = diffs_diff_prediction

        super().propose(bet, betcity_match, data=data, **kwargs)


    def __str__(self):
        strs = []
        if self.min_diffs_diff_for_win is not None:
            strs.append( 'min_diffs_diff_for_win=%.2f' % (self.min_diffs_diff_for_win,) )

        return '%s(%s)' % (self.__class__.__name__, ', '.join(strs))
