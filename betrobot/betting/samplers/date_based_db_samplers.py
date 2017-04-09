from betrobot.betting.samplers.db_sampler import DbSampler


# TODO: Параметризовать выбор дат
class HistoricalDbSampler(DbSampler):

    _pick = [ '_sample_condition' ]


    # TODO: Разобраться с аргументами
    def __init__(self, *args, date_condition=None, **kwargs):
        super().__init__(*args, **kwargs)

        if date_condition is None:
           date_condition = { '$regex': '^2014|^2015|^2016|^2017-01' }
        self._sample_condition = { 'date': date_condition }


    def sample(self, additional_sample_condition={}):
        sample_condition = self._sample_condition.copy()
        sample_condition.update(additional_sample_condition)
        sample = self._matches_collection.find(sample_condition)

        return sample


# TODO: Параметризовать выбор дат
class EveDbSampler(DbSampler):

    _pick = [ '_sample_condition' ]


    # TODO: Разобраться с аргументами
    def __init__(self, *args, date_condition=None, **kwargs):
        super().__init__(*args, **kwargs)

        if date_condition is None:
           date_condition = { '$regex': '^2016-12|^2017-01' }
        self._sample_condition = { 'date': date_condition }


    def sample(self, additional_sample_condition={}):
        sample_condition = self._sample_condition.copy()
        sample_condition.update(additional_sample_condition)
        sample = self._matches_collection.find(sample_condition)

        return sample
