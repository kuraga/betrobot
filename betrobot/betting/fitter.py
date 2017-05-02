from betrobot.util.pickable import Pickable


class Fitter(Pickable):

    _pick = [ 'train_sampler', 'is_fitted' ]


    def __init__(self):
        super().__init__()

        self.clean()


    def clean(self):
        self.is_fitted = False
        self._clean()


    def _clean(self):
        self.train_sampler = None
        self.sample_condition = None
        self.sample = None


    def fit(self, train_sampler, sample_condition, **kwargs):
        self.clean()

        self.train_sampler = train_sampler
        self.sample_condition = sample_condition
        self.sample = self.train_sampler.get_sample(self.sample_condition)

        self._fit(**kwargs)

        self.is_fitted = True


    def _fit(self, **kwargs):
        raise NotImplementedError()


    def __str__(self):
        return '%s()[is_fitted=%s]' % (self.__class__.__name__, str(self.is_fitted))
