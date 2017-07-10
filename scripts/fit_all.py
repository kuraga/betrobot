import argparse

from betrobot.betting.samplers.whole_sampler import WholeSampler

from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.goals_statistic_fitters import GoalsStatisticFitter, GoalsFirstPeriodStatisticFitter, GoalsSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.corners_statistic_fitters import CornersStatisticFitter, CornersFirstPeriodStatisticFitter, CornersSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.crosses_statistic_fitters import CrossesStatisticFitter, CrossesFirstPeriodStatisticFitter, CrossesSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.shots_statistic_fitters import ShotsStatisticFitter, ShotsFirstPeriodStatisticFitter, ShotsSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.fouls_statistic_fitters import FoulsStatisticFitter, FoulsFirstPeriodStatisticFitter, FoulsSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.yellow_cards_statistic_fitters import YellowCardsStatisticFitter, YellowCardsFirstPeriodStatisticFitter, YellowCardsSecondPeriodStatisticFitter
from betrobot.betting.fitters.statistic_fitters.teams_based_statistic_fitters.red_cards_statistic_fitters import RedCardsStatisticFitter, RedCardsFirstPeriodStatisticFitter, RedCardsSecondPeriodStatisticFitter

from betrobot.betting.fitters.statistic_fitters.players_based_statistic_fitters.corners_players_based_statistic_fitters import CornersPlayersBasedStatisticFitter, CornersFirstPeriodPlayersBasedStatisticFitter, CornersSecondPeriodPlayersBasedStatisticFitter
from betrobot.betting.fitters.statistic_fitters.players_based_statistic_fitters.crosses_players_based_statistic_fitters import CrossesPlayersBasedStatisticFitter, CrossesFirstPeriodPlayersBasedStatisticFitter, CrossesSecondPeriodPlayersBasedStatisticFitter
from betrobot.betting.fitters.statistic_fitters.players_based_statistic_fitters.shots_players_based_statistic_fitters import ShotsPlayersBasedStatisticFitter, ShotsFirstPeriodPlayersBasedStatisticFitter, ShotsSecondPeriodPlayersBasedStatisticFitter


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


    CornersPlayersBasedStatisticFitter().fit(train_sampler)
    CornersFirstPeriodPlayersBasedStatisticFitter().fit(train_sampler)
    CornersSecondPeriodPlayersBasedStatisticFitter().fit(train_sampler)

    CrossesPlayersBasedStatisticFitter().fit(train_sampler)
    CrossesFirstPeriodPlayersBasedStatisticFitter().fit(train_sampler)
    CrossesSecondPeriodPlayersBasedStatisticFitter().fit(train_sampler)

    ShotsPlayersBasedStatisticFitter().fit(train_sampler)
    ShotsFirstPeriodPlayersBasedStatisticFitter().fit(train_sampler)
    ShotsSecondPeriodPlayersBasedStatisticFitter().fit(train_sampler)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.parse_args()

    _fit_all()
