from betrobot.betting.samplers.statistics_sampler import StatisticsSampler


class WholeStatisticsSampler(StatisticsSampler):

    def sample(self):
        statistics = self._get_statistics()

        return statistics
