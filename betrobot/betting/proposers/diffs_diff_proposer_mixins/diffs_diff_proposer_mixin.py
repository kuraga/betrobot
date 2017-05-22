class DiffsDiffProposerMixin(object):

    # TODO: min_diff - перенести на уровень выше?
    _pick = [ 'min_diff' ]


    def __init__(self, *args, min_diff=3, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_diff = min_diff


    def propose(self, bet, betcity_match, diff=None, **kwargs):
        data = kwargs.get('data', {})
        data['diff'] = diff

        super().propose(bet, betcity_match, data=data, **kwargs)
