from betrobot.util.pickable_mixin import PickableMixin
from betrobot.util.printable_mixin import PrintableMixin


class Presenter(PickableMixin, PrintableMixin):

    def present(self, provider, **kwargs):
        raise NotImplementedError()


    def _present_bets_data(self, bets_data):
        raise NotImplementedError()
