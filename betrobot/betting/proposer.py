import datetime
import pickle
import numpy as np
import pandas as pd
from betrobot.util.sport_util import bet_to_string, get_bet
from betrobot.util.common_util import list_wrap
from betrobot.util.check_util import check_bet
from betrobot.util.pickable import Pickable


class Proposer(Pickable):

    _pick = [ 'value_threshold', 'predicted_threshold', 'ratio_threshold', '_bets_data', '_attempts_count' ]


    def __init__(self, value_threshold=None, predicted_threshold=None, ratio_threshold=None):
        super().__init__()

        self.value_threshold = value_threshold
        self.predicted_threshold = predicted_threshold
        self.ratio_threshold = ratio_threshold

        self.clear()


    def clear(self):
        self._bets_data = pd.DataFrame(columns=['match_uuid', 'match_uuid_2', 'tournament', 'tournament_2', 'date', 'home', 'away', 'match_special_word', 'match_special_word_2', 'bet_pattern', 'bet_pattern_2', 'bet_value', 'data', 'ground_truth'])
        self._attempts_count = 0


    # TODO: Реализовать дедупликацию через анализ (раннее записанной) даты появления ставки
    def get_bets_data(self):
        bets_data = self._bets_data.copy()

        bets_data['bet_pattern_repr'] = bets_data['bet_pattern'].apply(repr)
        bets_data['bet_pattern_2_repr'] = bets_data['bet_pattern_2'].apply(repr)
        bets_data = bets_data.sort_values('bet_value', ascending=True)
        bets_data = bets_data.drop_duplicates(subset=['tournament', 'tournament_2', 'date', 'home', 'away', 'match_special_word', 'match_special_word_2', 'bet_pattern_repr', 'bet_pattern_2_repr'], keep='first')
        bets_data = bets_data.drop(['bet_pattern_repr', 'bet_pattern_2_repr'], axis=1)

        return bets_data


    def propose(self, bet_pattern, betcity_match, predicted_bet_value=None, ground_truth=None, whoscored_match=None, data=None):
        if data is None:
            data = {}

        bet = get_bet(bet_pattern, betcity_match)
        if bet is None:
            return
        bet_value = bet[5]

        if self.value_threshold is not None and bet_value < self.value_threshold:
            return
        if predicted_bet_value is not None and self.predicted_threshold is not None and predicted_bet_value > self.predicted_threshold:
            return
        if predicted_bet_value is not None and self.ratio_threshold is not None and bet_value / predicted_bet_value < self.ratio_threshold:
            return

        if ground_truth is None and whoscored_match is not None:
            ground_truth = check_bet(bet, betcity_match['specialWord'], whoscored_match)

        if predicted_bet_value is not None:
            data['predicted_bet_value'] = np.round(predicted_bet_value, 2)
        if whoscored_match is not None:
            data['whoscored_match'] = whoscored_match['uuid']

        self.make_bet(betcity_match, bet, ground_truth, data=data)


    def _append_bet(self, match_uuid, tournament, date, home, away, match_special_word, bet_pattern, bet_value, ground_truth, data=None, express=False, match_uuid_2=None, tournament_2=None, match_special_word_2=None, bet_pattern_2=None):
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
            'data': data,
            'ground_truth': ground_truth
        }
        self._bets_data = self._bets_data.append(bet, ignore_index=True)
        self._attempts_count += 1


    def make_bet(self, betarch_match, bet, ground_truth, data=None):
        if bet is None:
            return

        bet_pattern = bet[0:5]
        bet_value = bet[5]

        self._append_bet(betarch_match['uuid'], betarch_match['tournament'], betarch_match['date'], betarch_match['home'], betarch_match['away'], betarch_match['specialWord'], bet_pattern, bet_value, ground_truth, data=data)


    def make_express_bet(self, betarch_match, bet, ground_truth, betarch_match_2, bet_2, ground_truth_2, data=None):
        if bet is None or bet_2 is None:
            return

        bet_pattern = bet[0:5]
        bet_value = bet[5]
        bet_pattern_2 = bet_2[0:5]
        bet_value_2 = bet_2[5]
        common_bet_value = bet_value * bet_value_2
        common_ground_truth = ground_truth & ground_truth_2 if ground_truth is not None and ground_truth_2 is not None else None

        self._append_bet(betarch_match['uuid'], betarch_match['tournament'], betarch_match['date'], betarch_match['home'], betarch_match['away'], betarch_match['specialWord'], bet_pattern, common_bet_value, common_ground_truth, True, betarch_match_2['uuid'], betarch_match_2['tournament'], betarch_match_2['specialWord'], bet_pattern_2, data=data)


    def _get_bets(self, betcity_match):
        raise NotImplementedError()


    def _handle_bet(self, bet, prediction, betcity_match, whoscored_match=None, **kwargs):
        raise NotImplementedError()


    def handle(self, betcity_match, prediction, whoscored_match=None, **kwargs):
        if prediction is None:
            return

        bets = self._get_bets(betcity_match)
        for bet in bets:
            self._handle_bet(bet, prediction, betcity_match, whoscored_match=whoscored_match, **kwargs)


    def flush(self, collection):
        bets_data = self.get_bets_data()
        for (i, bet_data) in bets_data.iterrows():
            bet_data_find = bet_data.to_dict()
            bet_data_find['date'] = datetime.datetime.strptime(bet_data_find['date'], '%Y-%m-%d')
            del bet_data_find['match_uuid'], bet_data_find['bet_value'], bet_data_find['ground_truth']

            bet_data_update = bet_data.to_dict()
            bet_data_update['date'] = datetime.datetime.strptime(bet_data_update['date'], '%Y-%m-%d')

            collection.update_one(bet_data_find, { '$set': bet_data_update }, upsert=True)


    # TODO: Переименовать
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


    def __str__(self):
        strs = []
        if self.value_threshold is not None:
            strs.append( 'value_threshold=%.2f' % (self.value_threshold,) )
        if self.predicted_threshold is not None:
            strs.append( 'predicted_threshold=%.2f' % (self.predicted_threshold,) )
        if self.ratio_threshold is not None:
            strs.append( 'ratio_threshold=%.2f' % (self.ratio_threshold,) )

        return '%s(%s)' % (self.__class__.__name__, ', '.join(strs))
