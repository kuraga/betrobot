from betrobot.util.pickable import Pickable


class RefittersPipe(Pickable):

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


    def __str__(self):
        return '%s(base_fitter=%s, refitters=%s)' % (self.__class__.__name__, str(self.base_fitter), str(', '.join(map(str, self.refitters))))
