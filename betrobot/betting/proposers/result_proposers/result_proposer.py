from betrobot.betting.proposer import Proposer


class ResultProposer(Proposer):

    # TODO: min_events_count_diff_for_win - перенести на уровень выше?
    _pick = [ 'min_events_count_diff_for_win' ]


    def __init__(self, *args, min_events_count_diff_for_win=1, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_events_count_diff_for_win = min_events_count_diff_for_win


    def propose(self, bet, betcity_match, result_prediction=None, **kwargs):
        data = kwargs.get('data', {})
        data['result_prediction'] = result_prediction

        super().propose(bet, betcity_match, data=data, **kwargs)


    def _get_init_strs(self):
        result = []
        if self.min_events_count_diff_for_win is not None:
            strs.append( 'min_events_count_diff_for_win=%.2f' % (self.min_events_count_diff_for_win,) )
        return result
