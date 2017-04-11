from betrobot.betting.sampler import Sampler


class WholeSampler(Sampler):

    def get_sample(self, sample_condition=None):
        if sample_condition is None:
           sample_condition = {}

        sample = self._matches_collection.find(sample_condition)

        return sample
