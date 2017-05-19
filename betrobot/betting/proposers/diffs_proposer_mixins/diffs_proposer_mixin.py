class DiffsProposerMixin(object):

    _pick = [ 'min_diff' ]


    def __init__(self, *args, min_diff=1, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_diff = min_diff
