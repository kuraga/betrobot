from abc import ABCMeta, abstractmethod
from betrobot.util.pickable_mixin import PickableMixin
from betrobot.util.printable_mixin import PrintableMixin


class Fitter(PickableMixin, PrintableMixin, metaclass=ABCMeta):

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


    @abstractmethod
    def _fit(self, **kwargs):
        raise NotImplementedError()


    def _get_runtime_strs(self):
        return [
            'is_fitted=%s' % (str(self.is_fitted),)
        ]
