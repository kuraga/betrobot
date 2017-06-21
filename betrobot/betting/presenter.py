from abc import ABCMeta, abstractmethod
from betrobot.util.pickable_mixin import PickableMixin
from betrobot.util.printable_mixin import PrintableMixin


class Presenter(PickableMixin, PrintableMixin, metaclass=ABCMeta):

    @abstractmethod
    def present(self, provider, **kwargs):
        raise NotImplementedError()
