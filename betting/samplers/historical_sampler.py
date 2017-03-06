import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./betting/samplers')


from sampler import Sampler


class HistoricalSampler(Sampler):
    def __init__(self):
        self._sample_condition = { 'date': { '$regex': '^2016-10|^2016-11|^2016-12|^2017-01|^2017-02' } }

        Sampler.__init__(self)


    def sample(self, additional_sample_condition={}):
        sample_condition = self._sample_condition.copy()
        sample_condition.update(additional_sample_condition)
        sample = self._matches_collection.find(sample_condition)

        return sample
