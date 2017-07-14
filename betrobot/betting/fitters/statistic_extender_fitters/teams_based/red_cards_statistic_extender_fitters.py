from betrobot.betting.fitters.statistic_extender_fitter import StatisticExtenderFitter
from betrobot.betting.sport_util import count_events_of_teams_by_match_uuid, is_red_card, is_first_period, is_second_period
from betrobot.util.common_util import conjunct


class RedCardsStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        (red_cards_home_count, red_cards_away_count) = count_events_of_teams_by_match_uuid(is_red_card, match_header['uuid'])

        match_statistic_data = {
            'events_home_count': red_cards_home_count,
            'events_away_count': red_cards_away_count
        }

        return match_statistic_data


class RedCardsFirstPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        (red_cards_first_period_home_count, red_cards_first_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_red_card, is_first_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': red_cards_first_period_home_count,
            'events_away_count': red_cards_first_period_away_count
        }

        return match_statistic_data


class RedCardsSecondPeriodStatisticExtenderFitter(StatisticExtenderFitter):

    def _get_match_statistic_data(self, match_header):
        (red_cards_second_period_home_count, red_cards_second_period_away_count) = count_events_of_teams_by_match_uuid(conjunct(is_red_card, is_second_period), match_header['uuid'])

        match_statistic_data = {
            'events_home_count': red_cards_second_period_home_count,
            'events_away_count': red_cards_second_period_away_count
        }

        return match_statistic_data
