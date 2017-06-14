from betrobot.betting.fitters.statistic_fitter import StatisticFitter
from betrobot.util.sport_util import count_events_of_teams, is_yellow_card, is_first_period, is_second_period
from betrobot.util.common_util import conjunction


class YellowCardsStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

        match_statistic_data = {
            'events_home_count': yellow_cards_home_count,
            'events_away_count': yellow_cards_away_count
        }

        return match_statistic_data


class YellowCardsFirstPeriodStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (yellow_cards_first_period_home_count, yellow_cards_first_period_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_first_period), whoscored_match)

        match_statistic_data = {
            'events_home_count': yellow_cards_first_period_home_count,
            'events_away_count': yellow_cards_first_period_away_count
        }

        return match_statistic_data


class YellowCardsSecondPeriodStatisticFitter(StatisticFitter):

    def _get_match_statistic_data(self, whoscored_match):
        (yellow_cards_second_period_home_count, yellow_cards_second_period_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_second_period), whoscored_match)

        match_statistic_data = {
            'events_home_count': yellow_cards_second_period_home_count,
            'events_away_count': yellow_cards_second_period_away_count
        }

        return match_statistic_data
