def _satisfy(condition, l):
    for i in range(len(condition)):
        if condition[i] != '*' and condition[i] != l[i] and \
          not ((condition[i] is None and l[i] == '') or (condition[i] == '' and l[i] is None)):
            return False

    return True


def _get_pattern_of_betcity_bet(betcity_bet, betcity_match):
    match_special_word = betcity_match['specialWord']

    rules = {
        ('*', 'Исход', '', '1', None):                                             lambda betcity_bet: (match_special_word, 'Исход', 'матч', '1'),
        ('*', 'Исход', '', '1X', None):                                            lambda betcity_bet: (match_special_word, 'Исход', 'матч', '1X'),
        ('*', 'Исход', '', 'X2', None):                                            lambda betcity_bet: (match_special_word, 'Исход', 'матч', 'X2'),
        ('*', 'Исход', '', '2', None):                                             lambda betcity_bet: (match_special_word, 'Исход', 'матч', '2'),
        ('*', 'Исходы по таймам (1-й тайм)', '', '1', None):                       lambda betcity_bet: (match_special_word, 'Исход', '1-й тайм', '1'),
        ('*', 'Исходы по таймам (1-й тайм)', '', '1X', None):                      lambda betcity_bet: (match_special_word, 'Исход', '1-й тайм', '1X'),
        ('*', 'Исходы по таймам (1-й тайм)', '', 'X2', None):                      lambda betcity_bet: (match_special_word, 'Исход', '1-й тайм', 'X2'),
        ('*', 'Исходы по таймам (1-й тайм)', '', '2', None):                       lambda betcity_bet: (match_special_word, 'Исход', '1-й тайм', '2'),
        ('*', 'Исходы по таймам (2-й тайм)', '', '1', None):                       lambda betcity_bet: (match_special_word, 'Исход', '2-й тайм', '1'),
        ('*', 'Исходы по таймам (2-й тайм)', '', '1X', None):                      lambda betcity_bet: (match_special_word, 'Исход', '2-й тайм', '1X'),
        ('*', 'Исходы по таймам (2-й тайм)', '', 'X2', None):                      lambda betcity_bet: (match_special_word, 'Исход', '2-й тайм', 'X2'),
        ('*', 'Исходы по таймам (2-й тайм)', '', '2', None):                       lambda betcity_bet: (match_special_word, 'Исход', '2-й тайм', '2'),
        ('*', 'Фора', '1', '', '*'):                                               lambda betcity_bet: (match_special_word, 'Фора', 'матч', '1', betcity_bet[4]),
        ('*', 'Фора', betcity_match['home'], '', '*'):                             lambda betcity_bet: (match_special_word, 'Фора', 'матч', '1', betcity_bet[4]),
        ('*', 'Фора', '2', '', '*'):                                               lambda betcity_bet: (match_special_word, 'Фора', 'матч', '2', betcity_bet[4]),
        ('*', 'Фора', betcity_match['away'], '', '*'):                             lambda betcity_bet: (match_special_word, 'Фора', 'матч', '2', betcity_bet[4]),
        ('*', 'Исходы по таймам (1-й тайм)', 'Фора', '1', '*'):                    lambda betcity_bet: (match_special_word, 'Фора', '1-й тайм', '1', betcity_bet[4]),
        ('*', 'Исходы по таймам (1-й тайм)', 'Фора', betcity_match['home'], '*'):  lambda betcity_bet: (match_special_word, 'Фора', '1-й тайм', '1', betcity_bet[4]),
        ('*', 'Исходы по таймам (1-й тайм)', 'Фора', '2', '*'):                    lambda betcity_bet: (match_special_word, 'Фора', '1-й тайм', '2', betcity_bet[4]),
        ('*', 'Исходы по таймам (1-й тайм)', 'Фора', betcity_match['away'], '*'):  lambda betcity_bet: (match_special_word, 'Фора', '1-й тайм', '2', betcity_bet[4]),
        ('*', 'Исходы по таймам (2-й тайм)', 'Фора', '1', '*'):                    lambda betcity_bet: (match_special_word, 'Фора', '2-й тайм', '1', betcity_bet[4]),
        ('*', 'Исходы по таймам (2-й тайм)', 'Фора', betcity_match['home'], '*'):  lambda betcity_bet: (match_special_word, 'Фора', '2-й тайм', '1', betcity_bet[4]),
        ('*', 'Исходы по таймам (2-й тайм)', 'Фора', '2', '*'):                    lambda betcity_bet: (match_special_word, 'Фора', '2-й тайм', '2', betcity_bet[4]),
        ('*', 'Исходы по таймам (2-й тайм)', 'Фора', betcity_match['away'], '*'):  lambda betcity_bet: (match_special_word, 'Фора', '2-й тайм', '2', betcity_bet[4]),
        ('*', 'Тотал', '', 'Бол', '*'):                                            lambda betcity_bet: (match_special_word, 'Тотал', 'матч', '>', betcity_bet[4]),
        ('*', 'Тотал', '', 'Мен', '*'):                                            lambda betcity_bet: (match_special_word, 'Тотал', 'матч', '<', betcity_bet[4]),
        ('*', 'Дополнительные тоталы', '', 'Бол', '*'):                            lambda betcity_bet: (match_special_word, 'Тотал', 'матч', '>', betcity_bet[4]),
        ('*', 'Дополнительные тоталы', '', 'Мен', '*'):                            lambda betcity_bet: (match_special_word, 'Тотал', 'матч', '<', betcity_bet[4]),
        ('*', 'Исходы по таймам (1-й тайм)', '', 'Бол', '*'):                      lambda betcity_bet: (match_special_word, 'Тотал', '1-й тайм', '>', betcity_bet[4]),
        ('*', 'Исходы по таймам (1-й тайм)', '', 'Мен', '*'):                      lambda betcity_bet: (match_special_word, 'Тотал', '1-й тайм', '<', betcity_bet[4]),
        ('*', 'Исходы по таймам (2-й тайм)', '', 'Бол', '*'):                      lambda betcity_bet: (match_special_word, 'Тотал', '2-й тайм', '>', betcity_bet[4]),
        ('*', 'Исходы по таймам (2-й тайм)', '', 'Мен', '*'):                      lambda betcity_bet: (match_special_word, 'Тотал', '2-й тайм', '<', betcity_bet[4]),
        ('*', 'Индивидуальный тотал', '1', 'Бол', '*'):                            lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '1', '>', betcity_bet[4]),
        ('*', 'Индивидуальный тотал', '1', 'Мен', '*'):                            lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '1', '<', betcity_bet[4]),
        ('*', 'Индивидуальный тотал', betcity_match['home'], 'Бол', '*'):          lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '1', '>', betcity_bet[4]),
        ('*', 'Индивидуальный тотал', betcity_match['home'], 'Мен', '*'):          lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '1', '<', betcity_bet[4]),
        ('*', 'Индивидуальный тотал', '2', 'Бол', '*'):                            lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '2', '>', betcity_bet[4]),
        ('*', 'Индивидуальный тотал', '2', 'Мен', '*'):                            lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '2', '<', betcity_bet[4]),
        ('*', 'Индивидуальный тотал', betcity_match['away'], 'Бол', '*'):          lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '2', '>', betcity_bet[4]),
        ('*', 'Индивидуальный тотал', betcity_match['away'], 'Мен', '*'):          lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '2', '<', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 1-й тайм', '1', 'Бол', '*'):                   lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '1', '>', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 1-й тайм', '1', 'Мен', '*'):                   lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '1', '<', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['home'], 'Бол', '*'): lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '1', '>', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['home'], 'Мен', '*'): lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '1', '<', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 1-й тайм', '2', 'Бол', '*'):                   lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '2', '>', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 1-й тайм', '2', 'Мен', '*'):                   lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '2', '<', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['away'], 'Бол', '*'): lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '2', '>', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 1-й тайм', betcity_match['away'], 'Мен', '*'): lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '2', '<', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 2-й тайм', '1', 'Бол', '*'):                   lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '1', '>', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 2-й тайм', '1', 'Мен', '*'):                   lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '1', '<', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['home'], 'Бол', '*'): lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '1', '>', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['home'], 'Мен', '*'): lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '1', '<', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 2-й тайм', '2', 'Бол', '*'):                   lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '2', '>', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 2-й тайм', '2', 'Мен', '*'):                   lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '2', '<', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['away'], 'Бол', '*'): lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '2', '>', betcity_bet[4]),
        ('*', 'Индивидуальный тотал 2-й тайм', betcity_match['away'], 'Мен', '*'): lambda betcity_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '2', '<', betcity_bet[4])
    }

    for (rule_bet_pattern, rule_lambda) in rules.items():
        if _satisfy(rule_bet_pattern, betcity_bet):
            return rule_lambda(betcity_bet)


def transform_betcity_bets(betcity_match):
    bets = []

    for betcity_bet in betcity_match['bets']:
        bet_pattern = _get_pattern_of_betcity_bet(betcity_bet, betcity_match)
        bet_value = betcity_bet[5]
        if bet_pattern is None or bet_value is None:
            continue

        bets.append({
            'pattern': bet_pattern,
            'value': bet_value,
            'ground_truth': None
        })

    return bets
