from abc import ABCMeta, abstractmethod
from betrobot.util.pickable_mixin import PickableMixin
from betrobot.util.printable_mixin import PrintableMixin


class Predictor(PickableMixin, PrintableMixin, metaclass=ABCMeta):

    def predict(self, fitted, match_header, **kwargs):
        # TODO: Проверка обученности fitted

        return self._predict(fitted, match_header, **kwargs)


    @abstractmethod
    def _predict(self, fitter, match_header, **kwargs):
        raise NotImplementedError()
