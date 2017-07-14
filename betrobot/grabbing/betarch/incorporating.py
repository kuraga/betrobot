def _satisfy(condition, l):
    for i in range(len(condition)):
        if condition[i] != '*' and condition[i] != l[i] and \
          not ((condition[i] is None and l[i] == '') or (condition[i] == '' and l[i] is None)):
            return False

    return True


def _get_pattern_of_betarch_bet(betarch_bet, betarch_match):
    match_special_word = betarch_match['specialWord']

    rules = {
        ('*', 'Исход', '', '1', None):                                             lambda betarch_bet: (match_special_word, 'Исход', 'матч', '1'),
        ('*', 'Исход', '', '1X', None):                                            lambda betarch_bet: (match_special_word, 'Исход', 'матч', '1X'),
        ('*', 'Исход', '', 'X2', None):                                            lambda betarch_bet: (match_special_word, 'Исход', 'матч', 'X2'),
        ('*', 'Исход', '', '2', None):                                             lambda betarch_bet: (match_special_word, 'Исход', 'матч', '2'),
        ('*', 'Исходы по таймам (1-й тайм)', '', '1', None):                       lambda betarch_bet: (match_special_word, 'Исход', '1-й тайм', '1'),
        ('*', 'Исходы по таймам (1-й тайм)', '', '1X', None):                      lambda betarch_bet: (match_special_word, 'Исход', '1-й тайм', '1X'),
        ('*', 'Исходы по таймам (1-й тайм)', '', 'X2', None):                      lambda betarch_bet: (match_special_word, 'Исход', '1-й тайм', 'X2'),
        ('*', 'Исходы по таймам (1-й тайм)', '', '2', None):                       lambda betarch_bet: (match_special_word, 'Исход', '1-й тайм', '2'),
        ('*', 'Исходы по таймам (2-й тайм)', '', '1', None):                       lambda betarch_bet: (match_special_word, 'Исход', '2-й тайм', '1'),
        ('*', 'Исходы по таймам (2-й тайм)', '', '1X', None):                      lambda betarch_bet: (match_special_word, 'Исход', '2-й тайм', '1X'),
        ('*', 'Исходы по таймам (2-й тайм)', '', 'X2', None):                      lambda betarch_bet: (match_special_word, 'Исход', '2-й тайм', 'X2'),
        ('*', 'Исходы по таймам (2-й тайм)', '', '2', None):                       lambda betarch_bet: (match_special_word, 'Исход', '2-й тайм', '2'),
        ('*', 'Фора', '1', '', '*'):                                               lambda betarch_bet: (match_special_word, 'Фора', 'матч', '1', betarch_bet[4]),
        ('*', 'Фора', betarch_match['home'], '', '*'):                             lambda betarch_bet: (match_special_word, 'Фора', 'матч', '1', betarch_bet[4]),
        ('*', 'Фора', '2', '', '*'):                                               lambda betarch_bet: (match_special_word, 'Фора', 'матч', '2', betarch_bet[4]),
        ('*', 'Фора', betarch_match['away'], '', '*'):                             lambda betarch_bet: (match_special_word, 'Фора', 'матч', '2', betarch_bet[4]),
        ('*', 'Исходы по таймам (1-й тайм)', 'Фора', '1', '*'):                    lambda betarch_bet: (match_special_word, 'Фора', '1-й тайм', '1', betarch_bet[4]),
        ('*', 'Исходы по таймам (1-й тайм)', 'Фора', betarch_match['home'], '*'):  lambda betarch_bet: (match_special_word, 'Фора', '1-й тайм', '1', betarch_bet[4]),
        ('*', 'Исходы по таймам (1-й тайм)', 'Фора', '2', '*'):                    lambda betarch_bet: (match_special_word, 'Фора', '1-й тайм', '2', betarch_bet[4]),
        ('*', 'Исходы по таймам (1-й тайм)', 'Фора', betarch_match['away'], '*'):  lambda betarch_bet: (match_special_word, 'Фора', '1-й тайм', '2', betarch_bet[4]),
        ('*', 'Исходы по таймам (2-й тайм)', 'Фора', '1', '*'):                    lambda betarch_bet: (match_special_word, 'Фора', '2-й тайм', '1', betarch_bet[4]),
        ('*', 'Исходы по таймам (2-й тайм)', 'Фора', betarch_match['home'], '*'):  lambda betarch_bet: (match_special_word, 'Фора', '2-й тайм', '1', betarch_bet[4]),
        ('*', 'Исходы по таймам (2-й тайм)', 'Фора', '2', '*'):                    lambda betarch_bet: (match_special_word, 'Фора', '2-й тайм', '2', betarch_bet[4]),
        ('*', 'Исходы по таймам (2-й тайм)', 'Фора', betarch_match['away'], '*'):  lambda betarch_bet: (match_special_word, 'Фора', '2-й тайм', '2', betarch_bet[4]),
        ('*', 'Тотал', '', 'Бол', '*'):                                            lambda betarch_bet: (match_special_word, 'Тотал', 'матч', '>', betarch_bet[4]),
        ('*', 'Тотал', '', 'Мен', '*'):                                            lambda betarch_bet: (match_special_word, 'Тотал', 'матч', '<', betarch_bet[4]),
        ('*', 'Дополнительные тоталы', '', 'Бол', '*'):                            lambda betarch_bet: (match_special_word, 'Тотал', 'матч', '>', betarch_bet[4]),
        ('*', 'Дополнительные тоталы', '', 'Мен', '*'):                            lambda betarch_bet: (match_special_word, 'Тотал', 'матч', '<', betarch_bet[4]),
        ('*', 'Исходы по таймам (1-й тайм)', '', 'Бол', '*'):                      lambda betarch_bet: (match_special_word, 'Тотал', '1-й тайм', '>', betarch_bet[4]),
        ('*', 'Исходы по таймам (1-й тайм)', '', 'Мен', '*'):                      lambda betarch_bet: (match_special_word, 'Тотал', '1-й тайм', '<', betarch_bet[4]),
        ('*', 'Исходы по таймам (2-й тайм)', '', 'Бол', '*'):                      lambda betarch_bet: (match_special_word, 'Тотал', '2-й тайм', '>', betarch_bet[4]),
        ('*', 'Исходы по таймам (2-й тайм)', '', 'Мен', '*'):                      lambda betarch_bet: (match_special_word, 'Тотал', '2-й тайм', '<', betarch_bet[4]),
        ('*', 'Индивидуальный тотал', '1', 'Бол', '*'):                            lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '1', '>', betarch_bet[5]),
        ('*', 'Индивидуальный тотал', '1', 'Мен', '*'):                            lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '1', '<', betarch_bet[5]),
        ('*', 'Индивидуальный тотал', betarch_match['home'], 'Бол', '*'):          lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '1', '>', betarch_bet[5]),
        ('*', 'Индивидуальный тотал', betarch_match['home'], 'Мен', '*'):          lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '1', '<', betarch_bet[5]),
        ('*', 'Индивидуальный тотал', '2', 'Бол', '*'):                            lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '2', '>', betarch_bet[5]),
        ('*', 'Индивидуальный тотал', '2', 'Мен', '*'):                            lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '2', '<', betarch_bet[5]),
        ('*', 'Индивидуальный тотал', betarch_match['away'], 'Бол', '*'):          lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '2', '>', betarch_bet[5]),
        ('*', 'Индивидуальный тотал', betarch_match['away'], 'Мен', '*'):          lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', 'матч', '2', '<', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 1-й тайм', '1', 'Бол', '*'):                   lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '1', '>', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 1-й тайм', '1', 'Мен', '*'):                   lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '1', '<', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 1-й тайм', betarch_match['home'], 'Бол', '*'): lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '1', '>', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 1-й тайм', betarch_match['home'], 'Мен', '*'): lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '1', '<', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 1-й тайм', '2', 'Бол', '*'):                   lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '2', '>', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 1-й тайм', '2', 'Мен', '*'):                   lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '2', '<', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 1-й тайм', betarch_match['away'], 'Бол', '*'): lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '2', '>', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 1-й тайм', betarch_match['away'], 'Мен', '*'): lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '1-й тайм', '2', '<', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 2-й тайм', '1', 'Бол', '*'):                   lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '1', '>', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 2-й тайм', '1', 'Мен', '*'):                   lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '1', '<', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 2-й тайм', betarch_match['home'], 'Бол', '*'): lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '1', '>', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 2-й тайм', betarch_match['home'], 'Мен', '*'): lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '1', '<', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 2-й тайм', '2', 'Бол', '*'):                   lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '2', '>', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 2-й тайм', '2', 'Мен', '*'):                   lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '2', '<', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 2-й тайм', betarch_match['away'], 'Бол', '*'): lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '2', '>', betarch_bet[5]),
        ('*', 'Индивидуальный тотал 2-й тайм', betarch_match['away'], 'Мен', '*'): lambda betarch_bet: (match_special_word, 'Индивидуальный тотал', '2-й тайм', '2', '<', betarch_bet[5])
    }

    for (rule_bet_pattern, rule_lambda) in rules.items():
        if _satisfy(rule_bet_pattern, betarch_bet):
            return rule_lambda(betarch_bet)


def transform_betarch_bets(betarch_match):
    bets = []

    for betarch_bet in betarch_match['bets']:
        bet_pattern = _get_pattern_of_betarch_bet(betarch_bet, betarch_match)
        bet_value = betarch_bet[5]
        if bet_pattern is None or bet_value is None:
            continue

        bets.append({
            'pattern': bet_pattern,
            'value': bet_value,
            'ground_truth': None
        })

    return bets
