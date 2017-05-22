from betrobot.util.pickable_mixin import PickableMixin
from betrobot.util.printable_mixin import PrintableMixin


class Predictor(PickableMixin, PrintableMixin):

    def predict(self, fitted, betcity_match, **kwargs):
        return self._predict(fitted, betcity_match, **kwargs)


    def _predict(self, fitter, betcity_match, **kwargs):
        raise NotImplementedError()
