from betrobot.util.common_util import conjunction
from betrobot.betting.sport_util import bet_satisfy, count_events_of_teams, is_home_or_away_by_betcity_team_name, is_goal, is_corner, is_yellow_card, is_first_period, is_second_period


def _check_goals_result_1(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    return goals_home_count > goals_away_count


def _check_goals_result_2(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    return goals_home_count < goals_away_count


def _check_goals_result_1X(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    return goals_home_count >= goals_away_count


def _check_goals_result_X2(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)

    return goals_home_count <= goals_away_count


def _check_goals_first_period_result_1(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_first_period), whoscored_match)

    return goals_home_count > goals_away_count


def _check_goals_first_period_result_2(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_first_period), whoscored_match)

    return goals_home_count < goals_away_count


def _check_goals_first_period_result_1X(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_first_period), whoscored_match)

    return goals_home_count >= goals_away_count


def _check_goals_first_period_result_X2(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_first_period), whoscored_match)

    return goals_home_count <= goals_away_count


def _check_goals_second_period_result_1(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_second_period), whoscored_match)

    return goals_home_count > goals_away_count


def _check_goals_second_period_result_2(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_second_period), whoscored_match)

    return goals_home_count < goals_away_count


def _check_goals_second_period_result_1X(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_second_period), whoscored_match)

    return goals_home_count >= goals_away_count


def _check_goals_second_period_result_X2(bet, match_special_word, whoscored_match):
    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_second_period), whoscored_match)

    return goals_home_count <= goals_away_count


def _check_goals_handicap(bet, match_special_word, whoscored_match):
    team = bet[2]
    handicap = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if goals_home_count + handicap == goals_away_count:
           return None
        else:
           return goals_home_count + handicap > goals_away_count

    elif is_home_or_away == 'A':
        if goals_home_count < goals_away_count == handicap:
           return None
        else:
           return goals_home_count < goals_away_count + handicap
    else:
        return None


def _check_goals_first_period_handicap(bet, match_special_word, whoscored_match):
    team = bet[3]
    handicap = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_first_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if goals_home_count + handicap == goals_away_count:
           return None
        else:
           return goals_home_count + handicap > goals_away_count

    elif is_home_or_away == 'A':
        if goals_home_count < goals_away_count == handicap:
           return None
        else:
           return goals_home_count < goals_away_count + handicap
    else:
        return None


def _check_goals_second_period_handicap(bet, match_special_word, whoscored_match):
    team = bet[3]
    handicap = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_second_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if goals_home_count + handicap == goals_away_count:
           return None
        else:
           return goals_home_count + handicap > goals_away_count

    elif is_home_or_away == 'A':
        if goals_home_count < goals_away_count == handicap:
           return None
        else:
           return goals_home_count < goals_away_count + handicap
    else:
        return None


def _check_goals_total_greater(bet, match_special_word, whoscored_match):
    total = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)
    goals_count = goals_home_count + goals_away_count

    if goals_count == total:
        return None
    else:
        return goals_count > total


def _check_goals_total_lesser(bet, match_special_word, whoscored_match):
    total = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)
    goals_count = goals_home_count + goals_away_count

    if goals_count == total:
        return None
    else:
        return goals_count < total


def _check_goals_first_period_total_greater(bet, match_special_word, whoscored_match):
    total = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_first_period), whoscored_match)
    goals_count = goals_home_count + goals_away_count

    if goals_count == total:
        return None
    else:
        return goals_count > total


def _check_goals_first_period_total_lesser(bet, match_special_word, whoscored_match):
    total = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_first_period), whoscored_match)
    goals_count = goals_home_count + goals_away_count

    if goals_count == total:
        return None
    else:
        return goals_count < total


def _check_goals_second_period_total_greater(bet, match_special_word, whoscored_match):
    total = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_second_period), whoscored_match)
    goals_count = goals_home_count + goals_away_count

    if goals_count == total:
        return None
    else:
        return goals_count > total


def _check_goals_second_period_total_lesser(bet, match_special_word, whoscored_match):
    total = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_second_period), whoscored_match)
    goals_count = goals_home_count + goals_away_count

    if goals_count == total:
        return None
    else:
        return goals_count < total


def _check_goals_individual_total_greater(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if goals_home_count == total:
            return None
        else:
            return goals_home_count > total

    elif is_home_or_away == 'A':
        if goals_away_count == total:
            return None
        else:
            return goals_away_count > total
    else:
        return None


def _check_goals_individual_total_lesser(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(is_goal, whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if goals_home_count == total:
            return None
        else:
            return goals_home_count < total

    elif is_home_or_away == 'A':
        if goals_away_count == total:
            return None
        else:
            return goals_away_count < total
    else:
        return None


def _check_goals_first_period_individual_total_greater(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_first_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if goals_home_count == total:
            return None
        else:
            return goals_home_count > total

    elif is_home_or_away == 'A':
        if goals_away_count == total:
            return None
        else:
            return goals_away_count > total
    else:
        return None


def _check_goals_first_period_individual_total_lesser(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_first_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if goals_home_count == total:
            return None
        else:
            return goals_home_count < total

    elif is_home_or_away == 'A':
        if goals_away_count == total:
            return None
        else:
            return goals_away_count < total
    else:
        return None


def _check_goals_second_period_individual_total_greater(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_second_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if goals_home_count == total:
            return None
        else:
            return goals_home_count > total

    elif is_home_or_away == 'A':
        if goals_away_count == total:
            return None
        else:
            return goals_away_count > total
    else:
        return None


def _check_goals_second_period_individual_total_lesser(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (goals_home_count, goals_away_count) = count_events_of_teams(conjunction(is_goal, is_second_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if goals_home_count == total:
            return None
        else:
            return goals_home_count < total

    elif is_home_or_away == 'A':
        if goals_away_count == total:
            return None
        else:
            return goals_away_count < total
    else:
        return None




def _check_corners_result_1(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    return corners_home_count > corners_away_count


def _check_corners_result_1X(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    return corners_home_count >= corners_away_count


def _check_corners_result_X2(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    return corners_home_count <= corners_away_count


def _check_corners_result_2(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)

    return corners_home_count < corners_away_count


def _check_corners_first_period_result_1(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_first_period), whoscored_match)

    return corners_home_count > corners_away_count


def _check_corners_first_period_result_1X(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_first_period), whoscored_match)

    return corners_home_count >= corners_away_count


def _check_corners_first_period_result_X2(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_first_period), whoscored_match)

    return corners_home_count <= corners_away_count


def _check_corners_first_period_result_2(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_first_period), whoscored_match)

    return corners_home_count < corners_away_count


def _check_corners_second_period_result_1(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_second_period), whoscored_match)

    return corners_home_count > corners_away_count


def _check_corners_second_period_result_1X(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_second_period), whoscored_match)

    return corners_home_count >= corners_away_count


def _check_corners_second_period_result_X2(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_second_period), whoscored_match)

    return corners_home_count <= corners_away_count


def _check_corners_second_period_result_2(bet, match_special_word, whoscored_match):
    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_second_period), whoscored_match)

    return corners_home_count < corners_away_count


def _check_corners_handicap(bet, match_special_word, whoscored_match):
    team = bet[2]
    handicap = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if corners_home_count + handicap == corners_away_count:
           return None
        else:
           return corners_home_count + handicap > corners_away_count

    elif is_home_or_away == 'A':
        if corners_home_count < corners_away_count == handicap:
           return None
        else:
           return corners_home_count < corners_away_count + handicap
    else:
        return None


def _check_corners_first_period_handicap(bet, match_special_word, whoscored_match):
    team = bet[3]
    handicap = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_first_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if corners_home_count + handicap == corners_away_count:
           return None
        else:
           return corners_home_count + handicap > corners_away_count

    elif is_home_or_away == 'A':
        if corners_home_count < corners_away_count == handicap:
           return None
        else:
           return corners_home_count < corners_away_count + handicap
    else:
        return None


def _check_corners_second_period_handicap(bet, match_special_word, whoscored_match):
    team = bet[3]
    handicap = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_second_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if corners_home_count + handicap == corners_away_count:
           return None
        else:
           return corners_home_count + handicap > corners_away_count

    elif is_home_or_away == 'A':
        if corners_home_count < corners_away_count == handicap:
           return None
        else:
           return corners_home_count < corners_away_count + handicap
    else:
        return None


def _check_corners_total_greater(bet, match_special_word, whoscored_match):
    total = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
    corners_count = corners_home_count + corners_away_count

    if corners_count == total:
        return None
    else:
        return corners_count > total


def _check_corners_total_lesser(bet, match_special_word, whoscored_match):
    total = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
    corners_count = corners_home_count + corners_away_count

    if corners_count == total:
        return None
    else:
        return corners_count < total


def _check_corners_first_period_total_greater(bet, match_special_word, whoscored_match):
    total = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_first_period), whoscored_match)
    corners_count = corners_home_count + corners_away_count

    if corners_count == total:
        return None
    else:
        return corners_count > total


def _check_corners_first_period_total_lesser(bet, match_special_word, whoscored_match):
    total = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_first_period), whoscored_match)
    corners_count = corners_home_count + corners_away_count

    if corners_count == total:
        return None
    else:
        return corners_count < total


def _check_corners_second_period_total_greater(bet, match_special_word, whoscored_match):
    total = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_second_period), whoscored_match)
    corners_count = corners_home_count + corners_away_count

    if corners_count == total:
        return None
    else:
        return corners_count > total


def _check_corners_second_period_total_lesser(bet, match_special_word, whoscored_match):
    total = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_second_period), whoscored_match)
    corners_count = corners_home_count + corners_away_count

    if corners_count == total:
        return None
    else:
        return corners_count < total


def _check_corners_individual_total_greater(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if corners_home_count == total:
            return None
        else:
            return corners_home_count > total

    elif is_home_or_away == 'A':
        if corners_away_count == total:
            return None
        else:
            return corners_away_count > total
    else:
        return None


def _check_corners_individual_total_lesser(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(is_corner, whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if corners_home_count == total:
            return None
        else:
            return corners_home_count < total

    elif is_home_or_away == 'A':
        if corners_away_count == total:
            return None
        else:
            return corners_away_count < total
    else:
        return None


def _check_corners_first_period_individual_total_greater(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_first_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if corners_home_count == total:
            return None
        else:
            return corners_home_count > total

    elif is_home_or_away == 'A':
        if corners_away_count == total:
            return None
        else:
            return corners_away_count > total
    else:
        return None


def _check_corners_first_period_individual_total_lesser(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_first_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if corners_home_count == total:
            return None
        else:
            return corners_home_count < total

    elif is_home_or_away == 'A':
        if corners_away_count == total:
            return None
        else:
            return corners_away_count < total
    else:
        return None


def _check_corners_second_period_individual_total_greater(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_second_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if corners_home_count == total:
            return None
        else:
            return corners_home_count > total

    elif is_home_or_away == 'A':
        if corners_away_count == total:
            return None
        else:
            return corners_away_count > total
    else:
        return None


def _check_corners_second_period_individual_total_lesser(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (corners_home_count, corners_away_count) = count_events_of_teams(conjunction(is_corner, is_second_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if corners_home_count == total:
            return None
        else:
            return corners_home_count < total

    elif is_home_or_away == 'A':
        if corners_away_count == total:
            return None
        else:
            return corners_away_count < total
    else:
        return None




def _check_yellow_cards_result_1(bet, match_special_word, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    return yellow_cards_home_count > yellow_cards_away_count


def _check_yellow_cards_result_1X(bet, match_special_word, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    return yellow_cards_home_count >= yellow_cards_away_count


def _check_yellow_cards_result_X2(bet, match_special_word, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    return yellow_cards_home_count <= yellow_cards_away_count


def _check_yellow_cards_result_2(bet, match_special_word, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)

    return yellow_cards_home_count < yellow_cards_away_count


def _check_yellow_cards_first_period_result_1(bet, match_special_word, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_first_period), whoscored_match)

    return yellow_cards_home_count > yellow_cards_away_count


def _check_yellow_cards_first_period_result_1X(bet, match_special_word, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_first_period), whoscored_match)

    return yellow_cards_home_count >= yellow_cards_away_count


def _check_yellow_cards_first_period_result_X2(bet, match_special_word, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_first_period), whoscored_match)

    return yellow_cards_home_count <= yellow_cards_away_count


def _check_yellow_cards_first_period_result_2(bet, match_special_word, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_first_period), whoscored_match)

    return yellow_cards_home_count < yellow_cards_away_count


def _check_yellow_cards_second_period_result_1(bet, match_special_word, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_second_period), whoscored_match)

    return yellow_cards_home_count > yellow_cards_away_count


def _check_yellow_cards_second_period_result_1X(bet, match_special_word, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_second_period), whoscored_match)

    return yellow_cards_home_count >= yellow_cards_away_count


def _check_yellow_cards_second_period_result_X2(bet, match_special_word, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_second_period), whoscored_match)

    return yellow_cards_home_count <= yellow_cards_away_count


def _check_yellow_cards_second_period_result_2(bet, match_special_word, whoscored_match):
    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_second_period), whoscored_match)

    return yellow_cards_home_count < yellow_cards_away_count


def _check_yellow_cards_handicap(bet, match_special_word, whoscored_match):
    team = bet[2]
    handicap = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if yellow_cards_home_count + handicap == yellow_cards_away_count:
           return None
        else:
           return yellow_cards_home_count + handicap > yellow_cards_away_count

    elif is_home_or_away == 'A':
        if yellow_cards_home_count < yellow_cards_away_count == handicap:
           return None
        else:
           return yellow_cards_home_count < yellow_cards_away_count + handicap
    else:
        return None


def _check_yellow_cards_first_period_handicap(bet, match_special_word, whoscored_match):
    team = bet[3]
    handicap = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_first_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if yellow_cards_home_count + handicap == yellow_cards_away_count:
           return None
        else:
           return yellow_cards_home_count + handicap > yellow_cards_away_count

    elif is_home_or_away == 'A':
        if yellow_cards_home_count < yellow_cards_away_count == handicap:
           return None
        else:
           return yellow_cards_home_count < yellow_cards_away_count + handicap
    else:
        return None


def _check_yellow_cards_second_period_handicap(bet, match_special_word, whoscored_match):
    team = bet[3]
    handicap = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_second_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if yellow_cards_home_count + handicap == yellow_cards_away_count:
           return None
        else:
           return yellow_cards_home_count + handicap > yellow_cards_away_count

    elif is_home_or_away == 'A':
        if yellow_cards_home_count < yellow_cards_away_count == handicap:
           return None
        else:
           return yellow_cards_home_count < yellow_cards_away_count + handicap
    else:
        return None


def _check_yellow_cards_total_greater(bet, match_special_word, whoscored_match):
    total = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)
    yellow_cards_count = yellow_cards_home_count + yellow_cards_away_count

    if yellow_cards_count == total:
        return None
    else:
        return yellow_cards_count > total


def _check_yellow_cards_total_lesser(bet, match_special_word, whoscored_match):
    total = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)
    yellow_cards_count = yellow_cards_home_count + yellow_cards_away_count

    if yellow_cards_count == total:
        return None
    else:
        return yellow_cards_count < total


def _check_yellow_cards_first_period_total_greater(bet, match_special_word, whoscored_match):
    total = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_first_period), whoscored_match)
    yellow_cards_count = yellow_cards_home_count + yellow_cards_away_count

    if yellow_cards_count == total:
        return None
    else:
        return yellow_cards_count > total


def _check_yellow_cards_first_period_total_lesser(bet, match_special_word, whoscored_match):
    total = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_first_period), whoscored_match)
    yellow_cards_count = yellow_cards_home_count + yellow_cards_away_count

    if yellow_cards_count == total:
        return None
    else:
        return yellow_cards_count < total


def _check_yellow_cards_second_period_total_greater(bet, match_special_word, whoscored_match):
    total = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_second_period), whoscored_match)
    yellow_cards_count = yellow_cards_home_count + yellow_cards_away_count

    if yellow_cards_count == total:
        return None
    else:
        return yellow_cards_count > total


def _check_yellow_cards_second_period_total_lesser(bet, match_special_word, whoscored_match):
    total = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_second_period), whoscored_match)
    yellow_cards_count = yellow_cards_home_count + yellow_cards_away_count

    if yellow_cards_count == total:
        return None
    else:
        return yellow_cards_count < total


def _check_yellow_cards_individual_total_greater(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if yellow_cards_home_count == total:
            return None
        else:
            return yellow_cards_home_count > total

    elif is_home_or_away == 'A':
        if yellow_cards_away_count == total:
            return None
        else:
            return yellow_cards_away_count > total
    else:
        return None


def _check_yellow_cards_individual_total_lesser(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(is_yellow_card, whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if yellow_cards_home_count == total:
            return None
        else:
            return yellow_cards_home_count < total

    elif is_home_or_away == 'A':
        if yellow_cards_away_count == total:
            return None
        else:
            return yellow_cards_away_count < total
    else:
        return None


def _check_yellow_cards_first_period_individual_total_greater(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_first_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if yellow_cards_home_count == total:
            return None
        else:
            return yellow_cards_home_count > total

    elif is_home_or_away == 'A':
        if yellow_cards_away_count == total:
            return None
        else:
            return yellow_cards_away_count > total
    else:
        return None


def _check_yellow_cards_first_period_individual_total_lesser(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_first_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if yellow_cards_home_count == total:
            return None
        else:
            return yellow_cards_home_count < total

    elif is_home_or_away == 'A':
        if yellow_cards_away_count == total:
            return None
        else:
            return yellow_cards_away_count < total
    else:
        return None


def _check_yellow_cards_second_period_individual_total_greater(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_second_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if yellow_cards_home_count == total:
            return None
        else:
            return yellow_cards_home_count > total

    elif is_home_or_away == 'A':
        if yellow_cards_away_count == total:
            return None
        else:
            return yellow_cards_away_count > total
    else:
        return None


def _check_yellow_cards_second_period_individual_total_lesser(bet, match_special_word, whoscored_match):
    team = bet[2]
    total = bet[4]

    (yellow_cards_home_count, yellow_cards_away_count) = count_events_of_teams(conjunction(is_yellow_card, is_second_period), whoscored_match)
    is_home_or_away = is_home_or_away_by_betcity_team_name(team, whoscored_match)

    if is_home_or_away == 'H':
        if yellow_cards_home_count == total:
            return None
        else:
            return yellow_cards_home_count < total

    elif is_home_or_away == 'A':
        if yellow_cards_away_count == total:
            return None
        else:
            return yellow_cards_away_count < total
    else:
        return None




def check_bet(bet, match_special_word, whoscored_match):
    if bet is None or whoscored_match is None:
        return None

    rules = [
        [ None, ('*', 'Исход', '', '1', None), _check_goals_result_1 ],
        [ None, ('*', 'Исход', '', '1X', None), _check_goals_result_1X ],
        [ None, ('*', 'Исход', '', 'X2', None), _check_goals_result_X2 ],
        [ None, ('*', 'Исход', '', '2', None), _check_goals_result_2 ],
        [ None, ('*', 'Исходы по таймам (1-й тайм)', '', '1', None), _check_goals_first_period_result_1 ],
        [ None, ('*', 'Исходы по таймам (1-й тайм)', '', '1X', None), _check_goals_first_period_result_1X ],
        [ None, ('*', 'Исходы по таймам (1-й тайм)', '', 'X2', None), _check_goals_first_period_result_X2 ],
        [ None, ('*', 'Исходы по таймам (1-й тайм)', '', '2', None), _check_goals_first_period_result_2 ],
        [ None, ('*', 'Исходы по таймам (2-й тайм)', '', '1', None), _check_goals_second_period_result_1 ],
        [ None, ('*', 'Исходы по таймам (2-й тайм)', '', '1X', None), _check_goals_second_period_result_1X ],
        [ None, ('*', 'Исходы по таймам (2-й тайм)', '', 'X2', None), _check_goals_second_period_result_X2 ],
        [ None, ('*', 'Исходы по таймам (2-й тайм)', '', '2', None), _check_goals_second_period_result_2 ],
        [ None, ('*', 'Фора', '*', '', '*'), _check_goals_handicap ],
        [ None, ('*', 'Исходы по таймам (1-й тайм)', 'Фора', '*', '*'), _check_goals_first_period_handicap ],
        [ None, ('*', 'Исходы по таймам (2-й тайм)', 'Фора', '*', '*'), _check_goals_second_period_handicap ],
        [ None, ('*', 'Тотал', '', 'Бол', '*'), _check_goals_total_greater ],
        [ None, ('*', 'Дополнительные тоталы', '', 'Бол', '*'), _check_goals_total_greater ],
        [ None, ('*', 'Тотал', '', 'Мен', '*'), _check_goals_total_lesser ],
        [ None, ('*', 'Дополнительные тоталы', '', 'Мен', '*'), _check_goals_total_lesser ],
        [ None, ('*', 'Исходы по таймам (1-й тайм)', '', 'Бол', '*'), _check_goals_first_period_total_greater ],
        [ None, ('*', 'Исходы по таймам (1-й тайм)', '', 'Мен', '*'), _check_goals_first_period_total_lesser ],
        [ None, ('*', 'Исходы по таймам (2-й тайм)', '', 'Бол', '*'), _check_goals_second_period_total_greater ],
        [ None, ('*', 'Исходы по таймам (2-й тайм)', '', 'Мен', '*'), _check_goals_second_period_total_lesser ],
        [ None, ('*', 'Индивидуальный тотал', '*', 'Бол', '*'), _check_goals_individual_total_greater ],
        [ None, ('*', 'Индивидуальный тотал', '*', 'Мен', '*'), _check_goals_individual_total_lesser ],
        [ None, ('*', 'Индивидуальный тотал 1-й тайм', '*', 'Бол', '*'), _check_goals_first_period_individual_total_greater ],
        [ None, ('*', 'Индивидуальный тотал 1-й тайм', '*', 'Мен', '*'), _check_goals_first_period_individual_total_lesser ],
        [ None, ('*', 'Индивидуальный тотал 2-й тайм', '*', 'Бол', '*'), _check_goals_second_period_individual_total_greater ],
        [ None, ('*', 'Индивидуальный тотал 2-й тайм', '*', 'Мен', '*'), _check_goals_second_period_individual_total_lesser ],

        [ 'УГЛ', ('*', 'Исход', '', '1', None), _check_corners_result_1 ],
        [ 'УГЛ', ('*', 'Исход', '', '1X', None), _check_corners_result_1X ],
        [ 'УГЛ', ('*', 'Исход', '', 'X2', None), _check_corners_result_X2 ],
        [ 'УГЛ', ('*', 'Исход', '', '2', None), _check_corners_result_2 ],
        [ 'УГЛ', ('*', 'Исходы по таймам (1-й тайм)', '', '1', None), _check_corners_first_period_result_1 ],
        [ 'УГЛ', ('*', 'Исходы по таймам (1-й тайм)', '', '1X', None), _check_corners_first_period_result_1X ],
        [ 'УГЛ', ('*', 'Исходы по таймам (1-й тайм)', '', 'X2', None), _check_corners_first_period_result_X2 ],
        [ 'УГЛ', ('*', 'Исходы по таймам (1-й тайм)', '', '2', None), _check_corners_first_period_result_2 ],
        [ 'УГЛ', ('*', 'Исходы по таймам (2-й тайм)', '', '1', None), _check_corners_second_period_result_1 ],
        [ 'УГЛ', ('*', 'Исходы по таймам (2-й тайм)', '', '1X', None), _check_corners_second_period_result_1X ],
        [ 'УГЛ', ('*', 'Исходы по таймам (2-й тайм)', '', 'X2', None), _check_corners_second_period_result_X2 ],
        [ 'УГЛ', ('*', 'Исходы по таймам (2-й тайм)', '', '2', None), _check_corners_second_period_result_2 ],
        [ 'УГЛ', ('*', 'Фора', '*', '', '*'), _check_corners_handicap ],
        [ 'УГЛ', ('*', 'Исходы по таймам (1-й тайм)', 'Фора', '*', '*'), _check_corners_first_period_handicap ],
        [ 'УГЛ', ('*', 'Исходы по таймам (2-й тайм)', 'Фора', '*', '*'), _check_corners_second_period_handicap ],
        [ 'УГЛ', ('*', 'Тотал', '', 'Бол', '*'), _check_corners_total_greater ],
        [ 'УГЛ', ('*', 'Дополнительные тоталы', '', 'Бол', '*'), _check_corners_total_greater ],
        [ 'УГЛ', ('*', 'Тотал', '', 'Мен', '*'), _check_corners_total_lesser ],
        [ 'УГЛ', ('*', 'Дополнительные тоталы', '', 'Мен', '*'), _check_corners_total_lesser ],
        [ 'УГЛ', ('*', 'Исходы по таймам (1-й тайм)', '', 'Бол', '*'), _check_corners_first_period_total_greater ],
        [ 'УГЛ', ('*', 'Исходы по таймам (1-й тайм)', '', 'Мен', '*'), _check_corners_first_period_total_lesser ],
        [ 'УГЛ', ('*', 'Исходы по таймам (2-й тайм)', '', 'Бол', '*'), _check_corners_second_period_total_greater ],
        [ 'УГЛ', ('*', 'Исходы по таймам (2-й тайм)', '', 'Мен', '*'), _check_corners_second_period_total_lesser ],
        [ 'УГЛ', ('*', 'Индивидуальный тотал', '*', 'Бол', '*'), _check_corners_individual_total_greater ],
        [ 'УГЛ', ('*', 'Индивидуальный тотал', '*', 'Мен', '*'), _check_corners_individual_total_lesser ],
        [ 'УГЛ', ('*', 'Индивидуальный тотал 1-й тайм', '*', 'Бол', '*'), _check_corners_first_period_individual_total_greater ],
        [ 'УГЛ', ('*', 'Индивидуальный тотал 1-й тайм', '*', 'Мен', '*'), _check_corners_first_period_individual_total_lesser ],
        [ 'УГЛ', ('*', 'Индивидуальный тотал 2-й тайм', '*', 'Бол', '*'), _check_corners_second_period_individual_total_greater ],
        [ 'УГЛ', ('*', 'Индивидуальный тотал 2-й тайм', '*', 'Мен', '*'), _check_corners_second_period_individual_total_lesser ],

        [ 'ЖК', ('*', 'Исход', '', '1', None), _check_yellow_cards_result_1 ],
        [ 'ЖК', ('*', 'Исход', '', '1X', None), _check_yellow_cards_result_1X ],
        [ 'ЖК', ('*', 'Исход', '', 'X2', None), _check_yellow_cards_result_X2 ],
        [ 'ЖК', ('*', 'Исход', '', '2', None), _check_yellow_cards_result_2 ],
        [ 'ЖК', ('*', 'Исходы по таймам (1-й тайм)', '', '1', None), _check_yellow_cards_first_period_result_1 ],
        [ 'ЖК', ('*', 'Исходы по таймам (1-й тайм)', '', '1X', None), _check_yellow_cards_first_period_result_1X ],
        [ 'ЖК', ('*', 'Исходы по таймам (1-й тайм)', '', 'X2', None), _check_yellow_cards_first_period_result_X2 ],
        [ 'ЖК', ('*', 'Исходы по таймам (1-й тайм)', '', '2', None), _check_yellow_cards_first_period_result_2 ],
        [ 'ЖК', ('*', 'Исходы по таймам (2-й тайм)', '', '1', None), _check_yellow_cards_second_period_result_1 ],
        [ 'ЖК', ('*', 'Исходы по таймам (2-й тайм)', '', '1X', None), _check_yellow_cards_second_period_result_1X ],
        [ 'ЖК', ('*', 'Исходы по таймам (2-й тайм)', '', 'X2', None), _check_yellow_cards_second_period_result_X2 ],
        [ 'ЖК', ('*', 'Исходы по таймам (2-й тайм)', '', '2', None), _check_yellow_cards_second_period_result_2 ],
        [ 'ЖК', ('*', 'Фора', '*', '', '*'), _check_yellow_cards_handicap ],
        [ 'ЖК', ('*', 'Исходы по таймам (1-й тайм)', 'Фора', '*', '*'), _check_yellow_cards_first_period_handicap ],
        [ 'ЖК', ('*', 'Исходы по таймам (2-й тайм)', 'Фора', '*', '*'), _check_yellow_cards_second_period_handicap ],
        [ 'ЖК', ('*', 'Тотал', '', 'Бол', '*'), _check_yellow_cards_total_greater ],
        [ 'ЖК', ('*', 'Дополнительные тоталы', '', 'Бол', '*'), _check_yellow_cards_total_greater ],
        [ 'ЖК', ('*', 'Тотал', '', 'Мен', '*'), _check_yellow_cards_total_lesser ],
        [ 'ЖК', ('*', 'Дополнительные тоталы', '', 'Мен', '*'), _check_yellow_cards_total_lesser ],
        [ 'ЖК', ('*', 'Исходы по таймам (1-й тайм)', '', 'Бол', '*'), _check_yellow_cards_first_period_total_greater ],
        [ 'ЖК', ('*', 'Исходы по таймам (1-й тайм)', '', 'Мен', '*'), _check_yellow_cards_first_period_total_lesser ],
        [ 'ЖК', ('*', 'Исходы по таймам (2-й тайм)', '', 'Бол', '*'), _check_yellow_cards_second_period_total_greater ],
        [ 'ЖК', ('*', 'Исходы по таймам (2-й тайм)', '', 'Мен', '*'), _check_yellow_cards_second_period_total_lesser ],
        [ 'ЖК', ('*', 'Индивидуальный тотал', '*', 'Бол', '*'), _check_yellow_cards_individual_total_greater ],
        [ 'ЖК', ('*', 'Индивидуальный тотал', '*', 'Мен', '*'), _check_yellow_cards_individual_total_lesser ],
        [ 'ЖК', ('*', 'Индивидуальный тотал 1-й тайм', '*', 'Бол', '*'), _check_yellow_cards_first_period_individual_total_greater ],
        [ 'ЖК', ('*', 'Индивидуальный тотал 1-й тайм', '*', 'Мен', '*'), _check_yellow_cards_first_period_individual_total_lesser ],
        [ 'ЖК', ('*', 'Индивидуальный тотал 2-й тайм', '*', 'Бол', '*'), _check_yellow_cards_second_period_individual_total_greater ],
        [ 'ЖК', ('*', 'Индивидуальный тотал 2-й тайм', '*', 'Мен', '*'), _check_yellow_cards_second_period_individual_total_lesser ]
    ]

    bet_pattern = tuple(bet[0:5])
    for (rule_match_special_word, rule_bet_pattern, rule_lambda) in rules:
        if match_special_word == rule_match_special_word and bet_satisfy(rule_bet_pattern, bet_pattern):
            return rule_lambda(bet, match_special_word, whoscored_match)

    return None
