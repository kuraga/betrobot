from betrobot.util.pickable_mixin import PickableMixin
from betrobot.util.printable_mixin import PrintableMixin


class Fitter(PickableMixin, PrintableMixin):

    _pick = [ 'previous_fitter', 'is_fitted' ]


    def __init__(self, do_prefit=False, do_fit=True):
        super().__init__()

        self.do_prefit = do_prefit
        self.do_fit = do_fit

        self.clean()


    def prefit(self, previous_fitter, **kwargs):
        self.is_prefitted = False

        self.previous_fitter = previous_fitter

        if not self.do_prefit:
            return

        self._fit(**kwargs)
        self.is_fitted = True


    def clean(self):
        self._clean()


    def _clean(self):
        pass


    def fit(self, **kwargs):
        self.is_fitted = False

        if not self.do_fit:
            return

        self.clean()
        self._fit(**kwargs)
        self.is_fitted = True


    def _fit(self, **kwargs):
        pass


    def _get_init_strs(self):
        return [
            'do_prefit=%s' % (str(self.do_prefit),),
            'do_fit=%s' % (str(self.do_fit),)
        ]


    def _get_runtime_strs(self):
        return [
            'is_fitted=%s' % (str(self.is_fitted),)
        ]
