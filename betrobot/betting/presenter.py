from betrobot.util.pickable import Pickable
from betrobot.util.printable import Printable


class Presenter(Pickable, Printable):

    def present(self, provider, **kwargs):
        raise NotImplementedError()


    def _present_bets_data(self, bets_data):
        raise NotImplementedError()
