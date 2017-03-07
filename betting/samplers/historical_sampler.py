from betting.sampler import Sampler


class HistoricalSampler(Sampler):
    def __init__(self, db_name='betrobot', matches_collection_name='matchesCleaned'):
        self._sample_condition = { 'date': { '$regex': '^2016-10|^2016-11|^2016-12|^2017-01|^2017-02' } }

        Sampler.__init__(self, db_name, matches_collection_name)


    def sample(self, additional_sample_condition={}):
        sample_condition = self._sample_condition.copy()
        sample_condition.update(additional_sample_condition)
        sample = self._matches_collection.find(sample_condition)

        return sample
