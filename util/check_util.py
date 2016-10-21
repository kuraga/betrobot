import sys
sys.path.append('./')
sys.path.append('./util')

from sport_util import bet_satisfy, count_events_of_teams, is_goal, is_corner, is_first_period, is_second_period


def _check_goals_result_1(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)
    ground_truth = goals_home_count > goals_away_count
    return ground_truth


def _check_goals_result_2(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)
    ground_truth = goals_home_count < goals_away_count
    return ground_truth


def _check_goals_result_1X(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)
    ground_truth = goals_home_count >= goals_away_count
    return ground_truth


def _check_goals_result_X2(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)
    ground_truth = goals_home_count <= goals_away_count
    return ground_truth


def _check_corners_result_1(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
    ground_truth = corners_home_count > corners_away_count
    return ground_truth


def _check_corners_result_1X(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
    ground_truth = corners_home_count >= corners_away_count
    return ground_truth


def _check_corners_result_X2(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
    ground_truth = corners_home_count <= corners_away_count
    return ground_truth


def _check_corners_result_2(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
    ground_truth = corners_home_count < corners_away_count
    return ground_truth


def _check_goals_first_period_result_1(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(lambda event: is_goal(event) and is_first_period(event), whoscored_match)
    ground_truth = goals_home_count > goals_away_count
    return ground_truth


def _check_goals_first_period_result_2(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(lambda event: is_goal(event) and is_first_period(event), whoscored_match)
    ground_truth = goals_home_count < goals_away_count
    return ground_truth


def _check_goals_first_period_result_1X(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(lambda event: is_goal(event) and is_first_period(event), whoscored_match)
    ground_truth = goals_home_count >= goals_away_count
    return ground_truth


def _check_goals_first_period_result_X2(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(lambda event: is_goal(event) and is_first_period(event), whoscored_match)
    ground_truth = goals_home_count <= goals_away_count
    return ground_truth


def _check_corners_first_period_result_1(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(lambda event: is_corner(event) and is_first_period(event), whoscored_match)
    ground_truth = corners_home_count > corners_away_count
    return ground_truth


def _check_corners_first_period_result_1X(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(lambda event: is_corner(event) and is_first_period(event), whoscored_match)
    ground_truth = corners_home_count >= corners_away_count
    return ground_truth


def _check_corners_first_period_result_X2(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(lambda event: is_corner(event) and is_first_period(event), whoscored_match)
    ground_truth = corners_home_count <= corners_away_count
    return ground_truth


def _check_corners_first_period_result_2(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(lambda event: is_corner(event) and is_first_period(event), whoscored_match)
    ground_truth = corners_home_count < corners_away_count
    return ground_truth


def _check_goals_second_period_result_1(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(lambda event: is_goal(event) and is_second_period(event), whoscored_match)
    ground_truth = goals_home_count > goals_away_count
    return ground_truth


def _check_goals_second_period_result_2(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(lambda event: is_goal(event) and is_second_period(event), whoscored_match)
    ground_truth = goals_home_count < goals_away_count
    return ground_truth


def _check_goals_second_period_result_1X(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(lambda event: is_goal(event) and is_second_period(event), whoscored_match)
    ground_truth = goals_home_count >= goals_away_count
    return ground_truth


def _check_goals_second_period_result_X2(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(lambda event: is_goal(event) and is_second_period(event), whoscored_match)
    ground_truth = goals_home_count <= goals_away_count
    return ground_truth


def _check_corners_second_period_result_1(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(lambda event: is_corner(event) and is_second_period(event), whoscored_match)
    ground_truth = corners_home_count > corners_away_count
    return ground_truth


def _check_corners_second_period_result_1X(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(lambda event: is_corner(event) and is_second_period(event), whoscored_match)
    ground_truth = corners_home_count >= corners_away_count
    return ground_truth


def _check_corners_second_period_result_X2(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(lambda event: is_corner(event) and is_second_period(event), whoscored_match)
    ground_truth = corners_home_count <= corners_away_count
    return ground_truth


def _check_corners_second_period_result_2(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(lambda event: is_corner(event) and is_second_period(event), whoscored_match)
    ground_truth = corners_home_count < corners_away_count
    return ground_truth


def _check_goals_total_greater(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)
    goals_count = goals_home_count + goals_away_count
    ground_truth = goals_count > bet[4]
    return ground_truth


def _check_goals_total_lesser(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)
    goals_count = goals_home_count + goals_away_count
    ground_truth = goals_count < bet[4]
    return ground_truth


def _check_corners_total_greater(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
    corners_count = corners_home_count + corners_away_count
    ground_truth = corners_count > bet[4]
    return ground_truth


def _check_corners_total_lesser(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
    corners_count = corners_home_count + corners_away_count
    ground_truth = corners_count < bet[4]
    return ground_truth


def check_bet(bet, match_special_word, whoscored_match):
    if bet is None or whoscored_match is None:
        return None

    rules = [
        [ None, (None, 'Исход', '', '1', None), _check_goals_result_1 ],
        [ None, (None, 'Исход', '', '1X', None), _check_goals_result_1X ],
        [ None, (None, 'Исход', '', 'X2', None), _check_goals_result_X2 ],
        [ None, (None, 'Исход', '', '2', None), _check_goals_result_2 ],
        [ 'УГЛ', ('УГЛ', 'Исход', '', '1', None), _check_corners_result_1 ],
        [ 'УГЛ', ('УГЛ', 'Исход', '', '1X', None), _check_corners_result_1X ],
        [ 'УГЛ', ('УГЛ', 'Исход', '', 'X2', None), _check_corners_result_X2 ],
        [ 'УГЛ', ('УГЛ', 'Исход', '', '2', None), _check_corners_result_2 ],
        [ None, (None, 'Исходы по таймам (1-й тайм)', '', '1', None), _check_goals_first_period_result_1 ],
        [ None, (None, 'Исходы по таймам (1-й тайм)', '', '1X', None), _check_goals_first_period_result_1X ],
        [ None, (None, 'Исходы по таймам (1-й тайм)', '', 'X2', None), _check_goals_first_period_result_X2 ],
        [ None, (None, 'Исходы по таймам (1-й тайм)', '', '2', None), _check_goals_first_period_result_2 ],
        [ 'УГЛ', (None, 'Исходы по таймам (1-й тайм)', '', '1', None), _check_corners_first_period_result_1 ],
        [ 'УГЛ', (None, 'Исходы по таймам (1-й тайм)', '', '1X', None), _check_corners_first_period_result_1X ],
        [ 'УГЛ', (None, 'Исходы по таймам (1-й тайм)', '', 'X2', None), _check_corners_first_period_result_X2 ],
        [ 'УГЛ', (None, 'Исходы по таймам (1-й тайм)', '', '2', None), _check_corners_first_period_result_2 ],
        [ None, (None, 'Исходы по таймам (2-й тайм)', '', '1', None), _check_goals_second_period_result_1 ],
        [ None, (None, 'Исходы по таймам (2-й тайм)', '', '1X', None), _check_goals_second_period_result_1X ],
        [ None, (None, 'Исходы по таймам (2-й тайм)', '', 'X2', None), _check_goals_second_period_result_X2 ],
        [ None, (None, 'Исходы по таймам (2-й тайм)', '', '2', None), _check_goals_second_period_result_2 ],
        [ 'УГЛ', (None, 'Исходы по таймам (2-й тайм)', '', '1', None), _check_corners_second_period_result_1 ],
        [ 'УГЛ', (None, 'Исходы по таймам (2-й тайм)', '', '1X', None), _check_corners_second_period_result_1X ],
        [ 'УГЛ', (None, 'Исходы по таймам (2-й тайм)', '', 'X2', None), _check_corners_second_period_result_X2 ],
        [ 'УГЛ', (None, 'Исходы по таймам (2-й тайм)', '', '2', None), _check_corners_second_period_result_2 ],
        [ None, ('УГЛ', 'Тотал', '', 'Бол', '*'), _check_goals_total_greater ],
        [ None, ('УГЛ', 'Дополнительные тоталы', '', 'Бол', '*'), _check_goals_total_greater ],
        [ None, ('УГЛ', 'Тотал', '', 'Мен', '*'), _check_goals_total_lesser ],
        [ None, ('УГЛ', 'Дополнительные тоталы', '', 'Мен', '*'), _check_goals_total_lesser ],
        [ 'УГЛ', ('УГЛ', 'Тотал', '', 'Бол', '*'), _check_corners_total_greater ],
        [ 'УГЛ', ('УГЛ', 'Дополнительные тоталы', '', 'Бол', '*'), _check_corners_total_greater ],
        [ 'УГЛ', ('УГЛ', 'Тотал', '', 'Мен', '*'), _check_corners_total_lesser ],
        [ 'УГЛ', ('УГЛ', 'Дополнительные тоталы', '', 'Мен', '*'), _check_corners_total_lesser ]
    ]

    bet_pattern = tuple(bet[0:5])
    for (rule_match_special_word, rule_bet_pattern, rule_lambda) in rules:
        if match_special_word == rule_match_special_word and bet_satisfy(rule_bet_pattern, bet_pattern):
            return rule_lambda(bet, match_special_word, whoscored_match)

    return None
