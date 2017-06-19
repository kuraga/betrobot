from betrobot.util.pickable_mixin import PickableMixin
from betrobot.util.printable_mixin import PrintableMixin


class RefittersPipe(PickableMixin, PrintableMixin):

    _pick = [ 'base_fitter', 'refitters' ]


    def __init__(self, base_fitter, refitters):
        super().__init__()

        self.base_fitter = base_fitter
        self.refitters = refitters


    def refit(self, betcity_match, **kwargs):
        self.refitters[0].refit(self.base_fitter, betcity_match=betcity_match, **kwargs)
        for i in range(1, len(self.refitters)):
            self.refitters[i].refit(self.refitters[i-1], betcity_match=betcity_match, **kwargs)


    @property
    def fitter(self):
        return self.refitters[-1]


    def _get_init_strs(self):
        return [
            'base_fitter=%s' % (str(self.base_fitter),),
            'refitters=[%s]' % (str(', '.join(map(str, self.refitters))),)
        ]
