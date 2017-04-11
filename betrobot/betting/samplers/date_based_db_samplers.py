import datetime
from betrobot.betting.samplers.db_sampler import DbSampler


class HistoricalDbSampler(DbSampler):

    _pick = [ '_sample_condition' ]


    def __init__(self, *args, last_datetime=None, **kwargs):
        super().__init__(*args, **kwargs)

        if last_datetime is not None:
           self.last_datetime = last_datetime
        else:
           self.last_datetime = datetime.datetime.today()
        self._sample_condition = { 'date': { '$lte': self.last_datetime } }


    def get_sample(self, additional_sample_condition=None):
        if additional_sample_condition is None:
            additional_sample_condition = {}

        sample_condition = self._sample_condition.copy()
        sample_condition.update(additional_sample_condition)

        sample = self._matches_collection.find(sample_condition)

        return sample


class EveDbSampler(DbSampler):

    _pick = [ '_sample_condition' ]


    def __init__(self, *args, last_datetime=None, delta_days=None, first_datetime=None, **kwargs):
        super().__init__(*args, **kwargs)

        if last_datetime is not None:
           self.last_datetime = last_datetime
        else:
           self.last_datetime = datetime.datetime.today()
        if delta_days is not None:
            self.delta_days = delta_days
        else:
            self.delta_days = 100
        if first_datetime is not None:
           self.first_datetime = first_datetime
        else:
           self.first_datetime = self.last_datetime - datetime.timedelta(days=self.delta_days)
        self._sample_condition = { 'date': { '$lte': self.last_datetime, '$gte': self.first_datetime } }


    def get_sample(self, additional_sample_condition=None):
        if additional_sample_condition is None:
            additional_sample_condition = {}

        sample_condition = self._sample_condition.copy()
        sample_condition.update(additional_sample_condition)

        sample = self._matches_collection.find(sample_condition)

        return sample
