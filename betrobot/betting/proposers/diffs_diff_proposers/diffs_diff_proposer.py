from betrobot.betting.proposer import Proposer


class DiffsDiffProposer(Proposer):

    _pick = [ 'min_margin' ]


    # TODO: min_margin - перенести на уровень выше
    def __init__(self, *args, min_margin=3, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_margin = min_margin


    def _get_init_strs(self):
        return [
            'min_margin=%.2f' % (self.min_margin,)
        ]
