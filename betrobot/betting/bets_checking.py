from betrobot.util.common_util import conjunct
from betrobot.betting.sport_util import get_extended_info, bet_satisfy, count_events_of_teams, is_goal, is_corner, is_yellow_card, is_first_period, is_second_period




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




# FIXME: После пересборки базы можно убрать match_uuid
def check_bet(bet, whoscored_match=None, match_uuid=None):
    if match_uuid is None:
        match_uuid = bet['match_uuid']

    if whoscored_match is None:
        whoscored_match = get_extended_info(match_uuid)['whoscored']

    rules = {
        ('УГЛ', 'Исход', 'матч', '1'):                              _check_corners_result_1,
        ('УГЛ', 'Исход', 'матч', '1X'):                             _check_corners_result_1X,
        ('УГЛ', 'Исход', 'матч', 'X2'):                             _check_corners_result_X2,
        ('УГЛ', 'Исход', 'матч', '2'):                              _check_corners_result_2,
        ('УГЛ', 'Исход', '1-й тайм', '1'):                          _check_corners_first_period_result_1,
        ('УГЛ', 'Исход', '1-й тайм', '1X'):                         _check_corners_first_period_result_1X,
        ('УГЛ', 'Исход', '1-й тайм', 'X2'):                         _check_corners_first_period_result_X2,
        ('УГЛ', 'Исход', '1-й тайм', '2'):                          _check_corners_first_period_result_2,
        ('УГЛ', 'Исход', '2-й тайм', '1'):                          _check_corners_second_period_result_1,
        ('УГЛ', 'Исход', '2-й тайм', '1X'):                         _check_corners_second_period_result_1X,
        ('УГЛ', 'Исход', '2-й тайм', 'X2'):                         _check_corners_second_period_result_X2,
        ('УГЛ', 'Исход', '2-й тайм', '2'):                          _check_corners_second_period_result_2,
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
        ('УГЛ', 'Индивидуальный тотал', '2-й тайм', '2', '<', '*'): _check_corners_second_period_individual_total_away_lesser
    }

    for (rule_bet_pattern, rule_lambda) in rules.items():
        if bet_satisfy(rule_bet_pattern, bet):
            try:
                return rule_lambda(bet['pattern'], whoscored_match)
            except TypeError:
                return None

    return None
