import pickle
from betrobot.betting.sampler import Sampler


class StatisticsSampler(Sampler):

    def __init__(self, statistics_file_path=None):
        super().__init__()

        if statistics_file_path is not None:
            self.statistics_file_path = statistics_file_path
        else:
            self.statistics_file_path = os.path.join('data', 'statistics.pkl')


    def _get_statistics(self):
        with open(self.statistics_file_path, 'rb') as f:
            return pickle.load(f)
