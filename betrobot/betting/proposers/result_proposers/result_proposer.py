from betrobot.betting.proposer import Proposer


class ResultProposer(Proposer):

    _pick = [ 'min_margin' ]


    # TODO: min_margin - перенести на уровень выше
    def __init__(self, min_margin=1, **kwargs):
        super().__init__(**kwargs)

        self.min_margin = min_margin


    def _get_init_strs(self):
        return [
            'min_margin=%f' % (self.min_margin,)
        ]
