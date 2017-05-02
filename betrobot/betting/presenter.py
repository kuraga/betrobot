from betrobot.util.pickable import Pickable


class Presenter(Pickable):

    def present(self, provider, **kwargs):
        raise NotImplementedError()


    def _present_bets_data(self, bets_data):
        raise NotImplementedError()


    def __str__(self):
        return '%s()' % (self.__class__.__name__,)
