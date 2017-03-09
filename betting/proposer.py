import datetime
import pickle
import numpy as np
import pandas as pd
from util.sport_util import bet_to_string, get_bet
from util.common_util import list_wrap
from util.check_util import check_bet
from util.pickable import Pickable


class Proposer(Pickable):

    _pick = [ '_threshold', '_bets_data', '_attempt_count' ]


    def __init__(self, threshold=None):
        self._threshold = threshold

        self._bets_data = pd.DataFrame(columns=['match_uuid', 'match_uuid_2', 'tournament', 'tournament_2', 'date', 'home', 'away', 'match_special_word', 'match_special_word_2', 'bet_pattern', 'bet_pattern_2', 'bet_value', 'ground_truth'])
        self._attempt_count = 0

        super().__init__()


    # TODO: Реализовать дедупликацию через анализ (раннее записанной) даты появления ставки
    def get_bets_data(self):
        bets_data = self._bets_data.copy()

        bets_data['bet_pattern_repr'] = bets_data['bet_pattern'].apply(repr)
        bets_data['bet_pattern_2_repr'] = bets_data['bet_pattern_2'].apply(repr)
        bets_data = bets_data.sort_values('bet_value', ascending=True)
        bets_data = bets_data.drop_duplicates(subset=['tournament', 'tournament_2', 'date', 'home', 'away', 'match_special_word', 'match_special_word_2', 'bet_pattern_repr', 'bet_pattern_2_repr'], keep='last')
        bets_data = bets_data.drop(['bet_pattern_repr', 'bet_pattern_2_repr'], axis=1)

        return bets_data


    def propose(self, bet_pattern, betcity_match, ground_truth=None, whoscored_match=None):
        bet = get_bet(bet_pattern, betcity_match)
        if bet is None:
            return

        # TODO: Обрабатывать значения threshold, запрещающие ставку
        if self._threshold is not None and bet[5] < self._threshold:
            return

        if ground_truth is None and whoscored_match is not None:
            ground_truth = check_bet(bet, betcity_match['specialWord'], whoscored_match)

        self.make_bet(betcity_match, bet, ground_truth)


    def _append_bet(self, match_uuid, tournament, date, home, away, match_special_word, bet_pattern, bet_value, ground_truth, express=False, match_uuid_2=None, tournament_2=None, match_special_word_2=None, bet_pattern_2=None):
        bet = {
            'express': express,
            'match_uuid': match_uuid,
            'match_uuid_2': match_uuid_2,
            'tournament': tournament,
            'tournament_2': tournament_2,
            'date': date,
            'home': home,
            'away': away,
            'match_special_word': match_special_word,
            'match_special_word_2': match_special_word_2,
            'bet_pattern': bet_pattern,
            'bet_pattern_2': bet_pattern_2,
            'bet_value': bet_value,
            'ground_truth': ground_truth
        }
        self._bets_data = self._bets_data.append(bet, ignore_index=True)
        self._attempt_count += 1


    def make_bet(self, betarch_match, bet, ground_truth):
        if bet is None:
            return

        bet_pattern = bet[0:5]
        bet_value = bet[5]

        self._append_bet(betarch_match['uuid'], betarch_match['tournament'], betarch_match['date'], betarch_match['home'], betarch_match['away'], betarch_match['specialWord'], bet_pattern, bet_value, ground_truth)



    def make_express_bet(self, betarch_match, bet, ground_truth, betarch_match_2, bet_2, ground_truth_2):
        if bet is None or bet_2 is None:
            return

        bet_pattern = bet[0:5]
        bet_value = bet[5]
        bet_pattern_2 = bet_2[0:5]
        bet_value_2 = bet_2[5]
        common_bet_value = bet_value * bet_value_2
        common_ground_truth = ground_truth & ground_truth_2 if ground_truth is not None and ground_truth_2 is not None else None

        self._append_bet(betarch_match['uuid'], betarch_match['tournament'], betarch_match['date'], betarch_match['home'], betarch_match['away'], betarch_match['specialWord'], bet_pattern, common_bet_value, common_ground_truth, True, betarch_match_2['uuid'], betarch_match_2['tournament'], betarch_match_2['specialWord'], bet_pattern_2)


    def flush(self, collection):
        bets_data = self.get_bets_data()
        for (i, bet_data) in bets_data.iterrows():
            bet_data_find = bet_data.to_dict()
            bet_data_find['date'] = datetime.datetime.strptime(bet_data_find['date'], '%Y-%m-%d')
            del bet_data_find['match_uuid'], bet_data_find['bet_value'], bet_data_find['ground_truth']

            bet_data_update = bet_data.to_dict()
            bet_data_update['date'] = datetime.datetime.strptime(bet_data_update['date'], '%Y-%m-%d')
            del bet_data_update['bet_value'], bet_data_update['ground_truth']

            collection.update_one(bet_data_find, { '$set': bet_data_update }, upsert=True)


    # TODO: Реализовать __str__
    def to_string(self):
        bets_data = self.get_bets_data()
        bets_data = bets_data.drop(['match_uuid'], axis=1)
        bets_data['bet_pattern'] = bets_data['bet_pattern'].apply(bet_to_string)

        result = ''
        result += self.name + '\n\n'
        if self.description is not None:
            result += self.description + '\n\n'
        result += bets_data.to_string(index=False)

        return result
