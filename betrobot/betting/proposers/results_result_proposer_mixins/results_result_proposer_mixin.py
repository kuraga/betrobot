class ResultsResultProposerMixin(object):

    # TODO: min_diff - перенести на уровень выше?
    _pick = [ 'min_diff' ]


    def __init__(self, *args, min_diff=1, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_diff = min_diff


    def propose(self, bet, betcity_match, result=None, **kwargs):
        data = kwargs.get('data', {})
        data['result'] = result

        super().propose(bet, betcity_match, **kwargs)
