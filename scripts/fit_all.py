import argparse

from betrobot.betting.samplers.whole_sampler import WholeSampler

from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.goals_statistic_fitters import GoalsStatisticFitter, GoalsFirstPeriodStatisticFitter, GoalsSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.corners_statistic_fitters import CornersStatisticFitter, CornersFirstPeriodStatisticFitter, CornersSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.crosses_statistic_fitters import CrossesStatisticFitter, CrossesFirstPeriodStatisticFitter, CrossesSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.shots_statistic_fitters import ShotsStatisticFitter, ShotsFirstPeriodStatisticFitter, ShotsSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.fouls_statistic_fitters import FoulsStatisticFitter, FoulsFirstPeriodStatisticFitter, FoulsSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.yellow_cards_statistic_fitters import YellowCardsStatisticFitter, YellowCardsFirstPeriodStatisticFitter, YellowCardsSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.red_cards_statistic_fitters import RedCardsStatisticFitter, RedCardsFirstPeriodStatisticFitter, RedCardsSecondPeriodStatisticFitter


def _fit_all():
    db_name = 'betrobot'
    collection_name = 'matches'
    train_sampler = WholeSampler(db_name, collection_name)

    GoalsStatisticFitter().fit(train_sampler)
    GoalsFirstPeriodStatisticFitter().fit(train_sampler)
    GoalsSecondPeriodStatisticFitter().fit(train_sampler)

    CornersStatisticFitter().fit(train_sampler)
    CornersFirstPeriodStatisticFitter().fit(train_sampler)
    CornersSecondPeriodStatisticFitter().fit(train_sampler)

    CrossesStatisticFitter().fit(train_sampler)
    CrossesFirstPeriodStatisticFitter().fit(train_sampler)
    CrossesSecondPeriodStatisticFitter().fit(train_sampler)

    ShotsStatisticFitter().fit(train_sampler)
    ShotsFirstPeriodStatisticFitter().fit(train_sampler)
    ShotsSecondPeriodStatisticFitter().fit(train_sampler)

    FoulsStatisticFitter().fit(train_sampler)
    FoulsFirstPeriodStatisticFitter().fit(train_sampler)
    FoulsSecondPeriodStatisticFitter().fit(train_sampler)

    RedCardsStatisticFitter().fit(train_sampler)
    RedCardsFirstPeriodStatisticFitter().fit(train_sampler)
    RedCardsSecondPeriodStatisticFitter().fit(train_sampler)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _fit_all()
