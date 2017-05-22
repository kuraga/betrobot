from betrobot.util.pickable_mixin import PickableMixin
from betrobot.util.printable_mixin import PrintableMixin


class Refitter(PickableMixin, PrintableMixin):

    _pick = [ 'previous_fitter', 'is_fitted' ]


    def __init__(self):
        super().__init__()

        self.clean()


    def clean(self):
        self.is_fitted = False
        self._clean()


    def _clean(self):
        self.previous_fitter = None


    def refit(self, previous_fitter, **kwargs):
        self.clean()

        self.previous_fitter = previous_fitter
        self._refit(**kwargs)

        self.is_fitted = True


    def _refit(self, **kwargs):
        raise NotImplementedError()


    def _get_runtime_strs(self):
        return [
            'is_fitted=%s' % (str(self.is_fitted),)
        ]
