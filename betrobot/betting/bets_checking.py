from betrobot.util.common_util import conjunct
from betrobot.betting.sport_util import get_extended_info, bet_satisfy, count_events_of_teams, is_goal, is_corner, is_yellow_card, is_first_period, is_second_period




def _check_goals_result_1(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    return goals_home_count > goals_away_count


def _check_goals_result_1X(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    return goals_home_count >= goals_away_count


def _check_goals_result_X2(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    return goals_home_count <= goals_away_count


def _check_goals_result_2(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    return goals_home_count < goals_away_count


def _check_goals_result_12(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    return goals_home_count != goals_away_count


def _check_goals_result_X(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    return goals_home_count == goals_away_count


def _check_goals_first_period_result_1(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)

    return goals_home_count > goals_away_count


def _check_goals_first_period_result_1X(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)

    return goals_home_count >= goals_away_count


def _check_goals_first_period_result_X2(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)

    return goals_home_count <= goals_away_count


def _check_goals_first_period_result_2(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)

    return goals_home_count < goals_away_count


def _check_goals_first_period_result_12(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)

    return goals_home_count != goals_away_count


def _check_goals_first_period_result_X(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)

    return goals_home_count == goals_away_count


def _check_goals_second_period_result_1(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)

    return goals_home_count > goals_away_count


def _check_goals_second_period_result_1X(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)

    return goals_home_count >= goals_away_count


def _check_goals_second_period_result_X2(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)

    return goals_home_count <= goals_away_count


def _check_goals_second_period_result_2(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)

    return goals_home_count < goals_away_count


def _check_goals_second_period_result_12(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)

    return goals_home_count != goals_away_count


def _check_goals_second_period_result_X(bet_pattern, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)

    return goals_home_count == goals_away_count


def _check_goals_handicap_home(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    if goals_home_count + handicap == goals_away_count:
        return None
    else:
        return goals_home_count + handicap > goals_away_count


def _check_goals_handicap_away(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    if goals_home_count == goals_away_count + handicap:
        return None
    else:
        return goals_home_count < goals_away_count + handicap


def _check_goals_first_period_handicap_home(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)

    if goals_home_count + handicap == goals_away_count:
        return None
    else:
        return goals_home_count + handicap > goals_away_count


def _check_goals_first_period_handicap_away(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)

    if goals_home_count == goals_away_count + handicap:
        return None
    else:
        return goals_home_count < goals_away_count + handicap


def _check_goals_second_period_handicap_home(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)

    if goals_home_count + handicap == goals_away_count:
        return None
    else:
        return goals_home_count + handicap > goals_away_count


def _check_goals_second_period_handicap_away(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)

    if goals_home_count < goals_away_count + handicap:
        return None
    else:
        return goals_home_count < goals_away_count + handicap


def _check_goals_total_greater(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)
    goals_count = goals_home_count + goals_away_count

    if goals_count == total:
         return None
    else:
         return goals_count > total


def _check_goals_total_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)
    goals_count = goals_home_count + goals_away_count

    if goals_count == total:
         return None
    else:
         return goals_count < total


def _check_goals_first_period_total_greater(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)
    goals_count = goals_home_count + goals_away_count

    if goals_count == total:
         return None
    else:
         return goals_count > total


def _check_goals_first_period_total_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)
    goals_count = goals_home_count + goals_away_count

    if goals_count == total:
         return None
    else:
         return goals_count < total


def _check_goals_second_period_total_greater(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)
    goals_count = goals_home_count + goals_away_count

    if goals_count == total:
         return None
    else:
         return goals_count > total


def _check_goals_second_period_total_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)
    goals_count = goals_home_count + goals_away_count

    if goals_count == total:
         return None
    else:
         return goals_count < total


def _check_goals_individual_total_home_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    if goals_home_count == total:
         return None
    else:
         return goals_home_count > total


def _check_goals_individual_total_away_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    if goals_away_count == total:
         return None
    else:
         return goals_away_count > total


def _check_goals_individual_total_home_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    if goals_home_count == total:
         return None
    else:
         return goals_home_count < total


def _check_goals_individual_total_away_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    if goals_away_count == total:
         return None
    else:
         return goals_away_count < total


def _check_goals_first_period_individual_total_home_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)

    if goals_home_count == total:
         return None
    else:
         return goals_home_count > total


def _check_goals_first_period_individual_total_away_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)

    if goals_away_count == total:
         return None
    else:
         return goals_away_count > total


def _check_goals_first_period_individual_total_home_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)

    if goals_home_count == total:
         return None
    else:
         return goals_home_count < total


def _check_goals_first_period_individual_total_away_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_first_period), whoscored_match)

    if goals_away_count == total:
         return None
    else:
         return goals_away_count < total


def _check_goals_second_period_individual_total_home_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)

    if goals_home_count == total:
         return None
    else:
         return goals_home_count > total


def _check_goals_second_period_individual_total_away_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)

    if goals_away_count == total:
         return None
    else:
         return goals_away_count > total


def _check_goals_second_period_individual_total_home_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)

    if goals_home_count == total:
         return None
    else:
         return goals_home_count < total


def _check_goals_second_period_individual_total_away_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunct(is_goal, is_second_period), whoscored_match)

    if goals_away_count == total:
         return None
    else:
         return goals_away_count < total




def _check_corners_result_1(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    return corners_home_count > corners_away_count


def _check_corners_result_1X(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    return corners_home_count >= corners_away_count


def _check_corners_result_X2(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    return corners_home_count <= corners_away_count


def _check_corners_result_2(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    return corners_home_count < corners_away_count


def _check_corners_result_12(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    return corners_home_count != corners_away_count


def _check_corners_result_X(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    return corners_home_count == corners_away_count


def _check_corners_first_period_result_1(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)

    return corners_home_count > corners_away_count


def _check_corners_first_period_result_1X(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)

    return corners_home_count >= corners_away_count


def _check_corners_first_period_result_X2(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)

    return corners_home_count <= corners_away_count


def _check_corners_first_period_result_2(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)

    return corners_home_count < corners_away_count


def _check_corners_first_period_result_12(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)

    return corners_home_count != corners_away_count


def _check_corners_first_period_result_X(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)

    return corners_home_count == corners_away_count


def _check_corners_second_period_result_1(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)

    return corners_home_count > corners_away_count


def _check_corners_second_period_result_1X(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)

    return corners_home_count >= corners_away_count


def _check_corners_second_period_result_X2(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)

    return corners_home_count <= corners_away_count


def _check_corners_second_period_result_2(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)

    return corners_home_count < corners_away_count


def _check_corners_second_period_result_12(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)

    return corners_home_count != corners_away_count


def _check_corners_second_period_result_X(bet_pattern, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)

    return corners_home_count == corners_away_count


def _check_corners_handicap_home(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    if corners_home_count + handicap == corners_away_count:
        return None
    else:
        return corners_home_count + handicap > corners_away_count


def _check_corners_handicap_away(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    if corners_home_count == corners_away_count + handicap:
        return None
    else:
        return corners_home_count < corners_away_count + handicap


def _check_corners_first_period_handicap_home(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)

    if corners_home_count + handicap == corners_away_count:
        return None
    else:
        return corners_home_count + handicap > corners_away_count


def _check_corners_first_period_handicap_away(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)

    if corners_home_count == corners_away_count + handicap:
        return None
    else:
        return corners_home_count < corners_away_count + handicap


def _check_corners_second_period_handicap_home(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)

    if corners_home_count + handicap == corners_away_count:
        return None
    else:
        return corners_home_count + handicap > corners_away_count


def _check_corners_second_period_handicap_away(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)

    if corners_home_count < corners_away_count + handicap:
        return None
    else:
        return corners_home_count < corners_away_count + handicap


def _check_corners_total_greater(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
    corners_count = corners_home_count + corners_away_count

    if corners_count == total:
         return None
    else:
         return corners_count > total


def _check_corners_total_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
    corners_count = corners_home_count + corners_away_count

    if corners_count == total:
         return None
    else:
         return corners_count < total


def _check_corners_first_period_total_greater(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)
    corners_count = corners_home_count + corners_away_count

    if corners_count == total:
         return None
    else:
         return corners_count > total


def _check_corners_first_period_total_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)
    corners_count = corners_home_count + corners_away_count

    if corners_count == total:
         return None
    else:
         return corners_count < total


def _check_corners_second_period_total_greater(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)
    corners_count = corners_home_count + corners_away_count

    if corners_count == total:
         return None
    else:
         return corners_count > total


def _check_corners_second_period_total_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)
    corners_count = corners_home_count + corners_away_count

    if corners_count == total:
         return None
    else:
         return corners_count < total


def _check_corners_individual_total_home_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    if corners_home_count == total:
         return None
    else:
         return corners_home_count > total


def _check_corners_individual_total_away_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    if corners_away_count == total:
         return None
    else:
         return corners_away_count > total


def _check_corners_individual_total_home_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    if corners_home_count == total:
         return None
    else:
         return corners_home_count < total


def _check_corners_individual_total_away_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    if corners_away_count == total:
         return None
    else:
         return corners_away_count < total


def _check_corners_first_period_individual_total_home_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)

    if corners_home_count == total:
         return None
    else:
         return corners_home_count > total


def _check_corners_first_period_individual_total_away_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)

    if corners_away_count == total:
         return None
    else:
         return corners_away_count > total


def _check_corners_first_period_individual_total_home_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)

    if corners_home_count == total:
         return None
    else:
         return corners_home_count < total


def _check_corners_first_period_individual_total_away_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_first_period), whoscored_match)

    if corners_away_count == total:
         return None
    else:
         return corners_away_count < total


def _check_corners_second_period_individual_total_home_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)

    if corners_home_count == total:
         return None
    else:
         return corners_home_count > total


def _check_corners_second_period_individual_total_away_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)

    if corners_away_count == total:
         return None
    else:
         return corners_away_count > total


def _check_corners_second_period_individual_total_home_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)

    if corners_home_count == total:
         return None
    else:
         return corners_home_count < total


def _check_corners_second_period_individual_total_away_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunct(is_corner, is_second_period), whoscored_match)

    if corners_away_count == total:
         return None
    else:
         return corners_away_count < total




def _check_yellow_cards_result_1(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    return yellow_cards_home_count > yellow_cards_away_count


def _check_yellow_cards_result_1X(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    return yellow_cards_home_count >= yellow_cards_away_count


def _check_yellow_cards_result_X2(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    return yellow_cards_home_count <= yellow_cards_away_count


def _check_yellow_cards_result_2(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    return yellow_cards_home_count < yellow_cards_away_count


def _check_yellow_cards_result_12(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    return yellow_cards_home_count != yellow_cards_away_count


def _check_yellow_cards_result_X(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    return yellow_cards_home_count == yellow_cards_away_count


def _check_yellow_cards_first_period_result_1(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)

    return yellow_cards_home_count > yellow_cards_away_count


def _check_yellow_cards_first_period_result_1X(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)

    return yellow_cards_home_count >= yellow_cards_away_count


def _check_yellow_cards_first_period_result_X2(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)

    return yellow_cards_home_count <= yellow_cards_away_count


def _check_yellow_cards_first_period_result_2(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)

    return yellow_cards_home_count < yellow_cards_away_count


def _check_yellow_cards_first_period_result_12(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)

    return yellow_cards_home_count != yellow_cards_away_count


def _check_yellow_cards_first_period_result_X(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)

    return yellow_cards_home_count == yellow_cards_away_count


def _check_yellow_cards_second_period_result_1(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)

    return yellow_cards_home_count > yellow_cards_away_count


def _check_yellow_cards_second_period_result_1X(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)

    return yellow_cards_home_count >= yellow_cards_away_count


def _check_yellow_cards_second_period_result_X2(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)

    return yellow_cards_home_count <= yellow_cards_away_count


def _check_yellow_cards_second_period_result_2(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)

    return yellow_cards_home_count < yellow_cards_away_count


def _check_yellow_cards_second_period_result_12(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)

    return yellow_cards_home_count != yellow_cards_away_count


def _check_yellow_cards_second_period_result_X(bet_pattern, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)

    return yellow_cards_home_count == yellow_cards_away_count


def _check_yellow_cards_handicap_home(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    if yellow_cards_home_count + handicap == yellow_cards_away_count:
        return None
    else:
        return yellow_cards_home_count + handicap > yellow_cards_away_count


def _check_yellow_cards_handicap_away(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    if yellow_cards_home_count == yellow_cards_away_count + handicap:
        return None
    else:
        return yellow_cards_home_count < yellow_cards_away_count + handicap


def _check_yellow_cards_first_period_handicap_home(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)

    if yellow_cards_home_count + handicap == yellow_cards_away_count:
        return None
    else:
        return yellow_cards_home_count + handicap > yellow_cards_away_count


def _check_yellow_cards_first_period_handicap_away(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)

    if yellow_cards_home_count == yellow_cards_away_count + handicap:
        return None
    else:
        return yellow_cards_home_count < yellow_cards_away_count + handicap


def _check_yellow_cards_second_period_handicap_home(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)

    if yellow_cards_home_count + handicap == yellow_cards_away_count:
        return None
    else:
        return yellow_cards_home_count + handicap > yellow_cards_away_count


def _check_yellow_cards_second_period_handicap_away(bet_pattern, whoscored_match):
    handicap = bet_pattern[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)

    if yellow_cards_home_count < yellow_cards_away_count + handicap:
        return None
    else:
        return yellow_cards_home_count < yellow_cards_away_count + handicap


def _check_yellow_cards_total_greater(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)
    yellow_cards_count = yellow_cards_home_count + yellow_cards_away_count

    if yellow_cards_count == total:
         return None
    else:
         return yellow_cards_count > total


def _check_yellow_cards_total_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)
    yellow_cards_count = yellow_cards_home_count + yellow_cards_away_count

    if yellow_cards_count == total:
         return None
    else:
         return yellow_cards_count < total


def _check_yellow_cards_first_period_total_greater(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)
    yellow_cards_count = yellow_cards_home_count + yellow_cards_away_count

    if yellow_cards_count == total:
         return None
    else:
         return yellow_cards_count > total


def _check_yellow_cards_first_period_total_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)
    yellow_cards_count = yellow_cards_home_count + yellow_cards_away_count

    if yellow_cards_count == total:
         return None
    else:
         return yellow_cards_count < total


def _check_yellow_cards_second_period_total_greater(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)
    yellow_cards_count = yellow_cards_home_count + yellow_cards_away_count

    if yellow_cards_count == total:
         return None
    else:
         return yellow_cards_count > total


def _check_yellow_cards_second_period_total_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)
    yellow_cards_count = yellow_cards_home_count + yellow_cards_away_count

    if yellow_cards_count == total:
         return None
    else:
         return yellow_cards_count < total


def _check_yellow_cards_individual_total_home_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    if yellow_cards_home_count == total:
         return None
    else:
         return yellow_cards_home_count > total


def _check_yellow_cards_individual_total_away_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    if yellow_cards_away_count == total:
         return None
    else:
         return yellow_cards_away_count > total


def _check_yellow_cards_individual_total_home_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    if yellow_cards_home_count == total:
         return None
    else:
         return yellow_cards_home_count < total


def _check_yellow_cards_individual_total_away_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    if yellow_cards_away_count == total:
         return None
    else:
         return yellow_cards_away_count < total


def _check_yellow_cards_first_period_individual_total_home_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)

    if yellow_cards_home_count == total:
         return None
    else:
         return yellow_cards_home_count > total


def _check_yellow_cards_first_period_individual_total_away_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)

    if yellow_cards_away_count == total:
         return None
    else:
         return yellow_cards_away_count > total


def _check_yellow_cards_first_period_individual_total_home_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)

    if yellow_cards_home_count == total:
         return None
    else:
         return yellow_cards_home_count < total


def _check_yellow_cards_first_period_individual_total_away_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_first_period), whoscored_match)

    if yellow_cards_away_count == total:
         return None
    else:
         return yellow_cards_away_count < total


def _check_yellow_cards_second_period_individual_total_home_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)

    if yellow_cards_home_count == total:
         return None
    else:
         return yellow_cards_home_count > total


def _check_yellow_cards_second_period_individual_total_away_greater(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)

    if yellow_cards_away_count == total:
         return None
    else:
         return yellow_cards_away_count > total


def _check_yellow_cards_second_period_individual_total_home_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)

    if yellow_cards_home_count == total:
         return None
    else:
         return yellow_cards_home_count < total


def _check_yellow_cards_second_period_individual_total_away_lesser(bet_pattern, whoscored_match):
    total = bet_pattern[5]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunct(is_yellow_card, is_second_period), whoscored_match)

    if yellow_cards_away_count == total:
         return None
    else:
         return yellow_cards_away_count < total




def check_bet(bet, whoscored_match=None):
    if whoscored_match is None:
        whoscored_match = get_extended_info(bet['match_uuid'])['whoscored']

    rules = {
        (None, 'Исход', 'матч', '1'):                               _check_goals_result_1,
        (None, 'Исход', 'матч', '1X'):                              _check_goals_result_1X,
        (None, 'Исход', 'матч', 'X2'):                              _check_goals_result_X2,
        (None, 'Исход', 'матч', '2'):                               _check_goals_result_2,
        (None, 'Исход', 'матч', '12'):                              _check_goals_result_12,
        (None, 'Исход', 'матч', 'X'):                               _check_goals_result_X,
        (None, 'Исход', '1-й тайм', '1'):                           _check_goals_first_period_result_1,
        (None, 'Исход', '1-й тайм', '1X'):                          _check_goals_first_period_result_1X,
        (None, 'Исход', '1-й тайм', 'X2'):                          _check_goals_first_period_result_X2,
        (None, 'Исход', '1-й тайм', '2'):                           _check_goals_first_period_result_2,
        (None, 'Исход', '1-й тайм', '12'):                          _check_goals_first_period_result_12,
        (None, 'Исход', '1-й тайм', 'X'):                           _check_goals_first_period_result_X,
        (None, 'Исход', '2-й тайм', '1'):                           _check_goals_second_period_result_1,
        (None, 'Исход', '2-й тайм', '1X'):                          _check_goals_second_period_result_1X,
        (None, 'Исход', '2-й тайм', 'X2'):                          _check_goals_second_period_result_X2,
        (None, 'Исход', '2-й тайм', '2'):                           _check_goals_second_period_result_2,
        (None, 'Исход', '2-й тайм', '12'):                          _check_goals_second_period_result_12,
        (None, 'Исход', '2-й тайм', 'X'):                           _check_goals_second_period_result_X,
        (None, 'Фора', 'матч', '1', '*'):                           _check_goals_handicap_home,
        (None, 'Фора', 'матч', '2', '*'):                           _check_goals_handicap_away,
        (None, 'Фора', '1-й тайм', '1', '*'):                       _check_goals_first_period_handicap_home,
        (None, 'Фора', '1-й тайм', '2', '*'):                       _check_goals_first_period_handicap_away,
        (None, 'Фора', '2-й тайм', '1', '*'):                       _check_goals_second_period_handicap_home,
        (None, 'Фора', '2-й тайм', '2', '*'):                       _check_goals_second_period_handicap_away,
        (None, 'Тотал', 'матч', '>', '*'):                          _check_goals_total_greater,
        (None, 'Тотал', 'матч', '<', '*'):                          _check_goals_total_lesser,
        (None, 'Тотал', '1-й тайм', '>', '*'):                      _check_goals_first_period_total_greater,
        (None, 'Тотал', '1-й тайм', '<', '*'):                      _check_goals_first_period_total_lesser,
        (None, 'Тотал', '2-й тайм', '>', '*'):                      _check_goals_second_period_total_greater,
        (None, 'Тотал', '2-й тайм', '<', '*'):                      _check_goals_second_period_total_lesser,
        (None, 'Индивидуальный тотал', 'матч', '1', '>', '*'):      _check_goals_individual_total_home_greater,
        (None, 'Индивидуальный тотал', 'матч', '1', '<', '*'):      _check_goals_individual_total_home_lesser,
        (None, 'Индивидуальный тотал', 'матч', '2', '>', '*'):      _check_goals_individual_total_away_greater,
        (None, 'Индивидуальный тотал', 'матч', '2', '<', '*'):      _check_goals_individual_total_away_lesser,
        (None, 'Индивидуальный тотал', '1-й тайм', '1', '>', '*'):  _check_goals_first_period_individual_total_home_greater,
        (None, 'Индивидуальный тотал', '1-й тайм', '1', '<', '*'):  _check_goals_first_period_individual_total_home_lesser,
        (None, 'Индивидуальный тотал', '1-й тайм', '2', '>', '*'):  _check_goals_first_period_individual_total_away_greater,
        (None, 'Индивидуальный тотал', '1-й тайм', '2', '<', '*'):  _check_goals_first_period_individual_total_away_lesser,
        (None, 'Индивидуальный тотал', '2-й тайм', '1', '>', '*'):  _check_goals_second_period_individual_total_home_greater,
        (None, 'Индивидуальный тотал', '2-й тайм', '1', '<', '*'):  _check_goals_second_period_individual_total_home_lesser,
        (None, 'Индивидуальный тотал', '2-й тайм', '2', '>', '*'):  _check_goals_second_period_individual_total_away_greater,
        (None, 'Индивидуальный тотал', '2-й тайм', '2', '<', '*'):  _check_goals_second_period_individual_total_away_lesser,

        ('УГЛ', 'Исход', 'матч', '1'):                              _check_corners_result_1,
        ('УГЛ', 'Исход', 'матч', '1X'):                             _check_corners_result_1X,
        ('УГЛ', 'Исход', 'матч', 'X2'):                             _check_corners_result_X2,
        ('УГЛ', 'Исход', 'матч', '2'):                              _check_corners_result_2,
        ('УГЛ', 'Исход', 'матч', '12'):                             _check_corners_result_12,
        ('УГЛ', 'Исход', 'матч', 'X'):                              _check_corners_result_X,
        ('УГЛ', 'Исход', '1-й тайм', '1'):                          _check_corners_first_period_result_1,
        ('УГЛ', 'Исход', '1-й тайм', '1X'):                         _check_corners_first_period_result_1X,
        ('УГЛ', 'Исход', '1-й тайм', 'X2'):                         _check_corners_first_period_result_X2,
        ('УГЛ', 'Исход', '1-й тайм', '2'):                          _check_corners_first_period_result_2,
        ('УГЛ', 'Исход', '1-й тайм', '12'):                         _check_corners_first_period_result_12,
        ('УГЛ', 'Исход', '1-й тайм', 'X'):                          _check_corners_first_period_result_X,
        ('УГЛ', 'Исход', '2-й тайм', '1'):                          _check_corners_second_period_result_1,
        ('УГЛ', 'Исход', '2-й тайм', '1X'):                         _check_corners_second_period_result_1X,
        ('УГЛ', 'Исход', '2-й тайм', 'X2'):                         _check_corners_second_period_result_X2,
        ('УГЛ', 'Исход', '2-й тайм', '2'):                          _check_corners_second_period_result_2,
        ('УГЛ', 'Исход', '2-й тайм', '12'):                         _check_corners_second_period_result_12,
        ('УГЛ', 'Исход', '2-й тайм', 'X'):                          _check_corners_second_period_result_X,
        ('УГЛ', 'Фора', 'матч', '1', '*'):                          _check_corners_handicap_home,
        ('УГЛ', 'Фора', 'матч', '2', '*'):                          _check_corners_handicap_away,
        ('УГЛ', 'Фора', '1-й тайм', '1', '*'):                      _check_corners_first_period_handicap_home,
        ('УГЛ', 'Фора', '1-й тайм', '2', '*'):                      _check_corners_first_period_handicap_away,
        ('УГЛ', 'Фора', '2-й тайм', '1', '*'):                      _check_corners_second_period_handicap_home,
        ('УГЛ', 'Фора', '2-й тайм', '2', '*'):                      _check_corners_second_period_handicap_away,
        ('УГЛ', 'Тотал', 'матч', '>', '*'):                         _check_corners_total_greater,
        ('УГЛ', 'Тотал', 'матч', '<', '*'):                         _check_corners_total_lesser,
        ('УГЛ', 'Тотал', '1-й тайм', '>', '*'):                     _check_corners_first_period_total_greater,
        ('УГЛ', 'Тотал', '1-й тайм', '<', '*'):                     _check_corners_first_period_total_lesser,
        ('УГЛ', 'Тотал', '2-й тайм', '>', '*'):                     _check_corners_second_period_total_greater,
        ('УГЛ', 'Тотал', '2-й тайм', '<', '*'):                     _check_corners_second_period_total_lesser,
        ('УГЛ', 'Индивидуальный тотал', 'матч', '1', '>', '*'):     _check_corners_individual_total_home_greater,
        ('УГЛ', 'Индивидуальный тотал', 'матч', '1', '<', '*'):     _check_corners_individual_total_home_lesser,
        ('УГЛ', 'Индивидуальный тотал', 'матч', '2', '>', '*'):     _check_corners_individual_total_away_greater,
        ('УГЛ', 'Индивидуальный тотал', 'матч', '2', '<', '*'):     _check_corners_individual_total_away_lesser,
        ('УГЛ', 'Индивидуальный тотал', '1-й тайм', '1', '>', '*'): _check_corners_first_period_individual_total_home_greater,
        ('УГЛ', 'Индивидуальный тотал', '1-й тайм', '1', '<', '*'): _check_corners_first_period_individual_total_home_lesser,
        ('УГЛ', 'Индивидуальный тотал', '1-й тайм', '2', '>', '*'): _check_corners_first_period_individual_total_away_greater,
        ('УГЛ', 'Индивидуальный тотал', '1-й тайм', '2', '<', '*'): _check_corners_first_period_individual_total_away_lesser,
        ('УГЛ', 'Индивидуальный тотал', '2-й тайм', '1', '>', '*'): _check_corners_second_period_individual_total_home_greater,
        ('УГЛ', 'Индивидуальный тотал', '2-й тайм', '1', '<', '*'): _check_corners_second_period_individual_total_home_lesser,
        ('УГЛ', 'Индивидуальный тотал', '2-й тайм', '2', '>', '*'): _check_corners_second_period_individual_total_away_greater,
        ('УГЛ', 'Индивидуальный тотал', '2-й тайм', '2', '<', '*'): _check_corners_second_period_individual_total_away_lesser,

        ('ЖК', 'Исход', 'матч', '1'):                               _check_yellow_cards_result_1,
        ('ЖК', 'Исход', 'матч', '1X'):                              _check_yellow_cards_result_1X,
        ('ЖК', 'Исход', 'матч', 'X2'):                              _check_yellow_cards_result_X2,
        ('ЖК', 'Исход', 'матч', '2'):                               _check_yellow_cards_result_2,
        ('ЖК', 'Исход', 'матч', '12'):                              _check_yellow_cards_result_12,
        ('ЖК', 'Исход', 'матч', 'X'):                               _check_yellow_cards_result_X,
        ('ЖК', 'Исход', '1-й тайм', '1'):                           _check_yellow_cards_first_period_result_1,
        ('ЖК', 'Исход', '1-й тайм', '1X'):                          _check_yellow_cards_first_period_result_1X,
        ('ЖК', 'Исход', '1-й тайм', 'X2'):                          _check_yellow_cards_first_period_result_X2,
        ('ЖК', 'Исход', '1-й тайм', '2'):                           _check_yellow_cards_first_period_result_2,
        ('ЖК', 'Исход', '1-й тайм', '12'):                          _check_yellow_cards_first_period_result_12,
        ('ЖК', 'Исход', '1-й тайм', 'X'):                           _check_yellow_cards_first_period_result_X,
        ('ЖК', 'Исход', '2-й тайм', '1'):                           _check_yellow_cards_second_period_result_1,
        ('ЖК', 'Исход', '2-й тайм', '1X'):                          _check_yellow_cards_second_period_result_1X,
        ('ЖК', 'Исход', '2-й тайм', 'X2'):                          _check_yellow_cards_second_period_result_X2,
        ('ЖК', 'Исход', '2-й тайм', '2'):                           _check_yellow_cards_second_period_result_2,
        ('ЖК', 'Исход', '2-й тайм', '12'):                          _check_yellow_cards_second_period_result_12,
        ('ЖК', 'Исход', '2-й тайм', 'X'):                           _check_yellow_cards_second_period_result_X,
        ('ЖК', 'Фора', 'матч', '1', '*'):                           _check_yellow_cards_handicap_home,
        ('ЖК', 'Фора', 'матч', '2', '*'):                           _check_yellow_cards_handicap_away,
        ('ЖК', 'Фора', '1-й тайм', '1', '*'):                       _check_yellow_cards_first_period_handicap_home,
        ('ЖК', 'Фора', '1-й тайм', '2', '*'):                       _check_yellow_cards_first_period_handicap_away,
        ('ЖК', 'Фора', '2-й тайм', '1', '*'):                       _check_yellow_cards_second_period_handicap_home,
        ('ЖК', 'Фора', '2-й тайм', '2', '*'):                       _check_yellow_cards_second_period_handicap_away,
        ('ЖК', 'Тотал', 'матч', '>', '*'):                          _check_yellow_cards_total_greater,
        ('ЖК', 'Тотал', 'матч', '<', '*'):                          _check_yellow_cards_total_lesser,
        ('ЖК', 'Тотал', '1-й тайм', '>', '*'):                      _check_yellow_cards_first_period_total_greater,
        ('ЖК', 'Тотал', '1-й тайм', '<', '*'):                      _check_yellow_cards_first_period_total_lesser,
        ('ЖК', 'Тотал', '2-й тайм', '>', '*'):                      _check_yellow_cards_second_period_total_greater,
        ('ЖК', 'Тотал', '2-й тайм', '<', '*'):                      _check_yellow_cards_second_period_total_lesser,
        ('ЖК', 'Индивидуальный тотал', 'матч', '1', '>', '*'):      _check_yellow_cards_individual_total_home_greater,
        ('ЖК', 'Индивидуальный тотал', 'матч', '1', '<', '*'):      _check_yellow_cards_individual_total_home_lesser,
        ('ЖК', 'Индивидуальный тотал', 'матч', '2', '>', '*'):      _check_yellow_cards_individual_total_away_greater,
        ('ЖК', 'Индивидуальный тотал', 'матч', '2', '<', '*'):      _check_yellow_cards_individual_total_away_lesser,
        ('ЖК', 'Индивидуальный тотал', '1-й тайм', '1', '>', '*'):  _check_yellow_cards_first_period_individual_total_home_greater,
        ('ЖК', 'Индивидуальный тотал', '1-й тайм', '1', '<', '*'):  _check_yellow_cards_first_period_individual_total_home_lesser,
        ('ЖК', 'Индивидуальный тотал', '1-й тайм', '2', '>', '*'):  _check_yellow_cards_first_period_individual_total_away_greater,
        ('ЖК', 'Индивидуальный тотал', '1-й тайм', '2', '<', '*'):  _check_yellow_cards_first_period_individual_total_away_lesser,
        ('ЖК', 'Индивидуальный тотал', '2-й тайм', '1', '>', '*'):  _check_yellow_cards_second_period_individual_total_home_greater,
        ('ЖК', 'Индивидуальный тотал', '2-й тайм', '1', '<', '*'):  _check_yellow_cards_second_period_individual_total_home_lesser,
        ('ЖК', 'Индивидуальный тотал', '2-й тайм', '2', '>', '*'):  _check_yellow_cards_second_period_individual_total_away_greater,
        ('ЖК', 'Индивидуальный тотал', '2-й тайм', '2', '<', '*'):  _check_yellow_cards_second_period_individual_total_away_lesser
    }

    for (rule_bet_pattern, rule_lambda) in rules.items():
        if bet_satisfy(rule_bet_pattern, bet):
            try:
                return rule_lambda(bet['pattern'], whoscored_match)
            except TypeError:
                return None

    return None
