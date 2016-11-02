import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')

import datetime
import pickle
import numpy as np
import pandas as pd
from sport_util import bet_to_string


class BettingSession:

    @classmethod
    def load(cls, file_path):
        with open(file_path, 'rb') as f_in:
            return pickle.load(f_in)


    def __init__(self, name, description=None):
        self.name = name
        self.description = description

        self.bets = pd.DataFrame(columns=['match_uuid', 'match_uuid_2', 'tournament', 'tournament_2', 'date', 'home', 'away', 'match_special_word', 'match_special_word_2', 'bet_pattern', 'bet_pattern_2', 'bet_value', 'ground_truth'])
        self._attempt_count = 0


    def append_bet(self, match_uuid, tournament, date, home, away, match_special_word, bet_pattern, bet_value, ground_truth, express=False, match_uuid_2=None, tournament_2=None, match_special_word_2=None, bet_pattern_2=None):
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
            'ground_truth': ground_truth,
            'result': None
        }
        self.bets = self.bets.append(bet, ignore_index=True)
        self._attempt_count += 1


    def make_bet(self, betarch_match, bet, ground_truth):
        if bet is None:
            return

        bet_pattern = bet[0:5]
        bet_value = bet[5]

        self.append_bet(betarch_match['uuid'], betarch_match['tournament'], betarch_match['date'], betarch_match['home'], betarch_match['away'], betarch_match['specialWord'], bet_pattern, bet_value, ground_truth)



    def make_express_bet(self, betarch_match, bet, ground_truth, betarch_match_2, bet_2, ground_truth_2):
        if bet is None or bet_2 is None:
            return

        bet_pattern = bet[0:5]
        bet_value = bet[5]
        bet_pattern_2 = bet_2[0:5]
        bet_value_2 = bet_2[5]
        common_bet_value = bet_value * bet_value_2
        common_ground_truth = ground_truth & ground_truth_2 if ground_truth is not None and ground_truth_2 is not None else None

        self.append_bet(betarch_match['uuid'], betarch_match['tournament'], betarch_match['date'], betarch_match['home'], betarch_match['away'], betarch_match['specialWord'], bet_pattern, common_bet_value, common_ground_truth, True, betarch_match_2['uuid'], betarch_match_2['tournament'], betarch_match_2['specialWord'], bet_pattern_2)



    def to_string(self):
        bets1 = self.bets.drop(['match_uuid'], axis=1)
        bets1['bet_pattern'] = bets1['bet_pattern'].apply(bet_to_string)

        res = ''
        res += self.name + '\n\n'
        if self.description is not None:
            res += self.description + '\n\n'
        res += bets1.to_string(index=False)

        return res


    def investigate(self):
        investigation = pd.DataFrame(columns=['min_koef', 'koef_mean', 'matches', 'bets', 'win', 'accurancy', 'roi'])

        for min_koef in np.arange(1.0, self.bets['bet_value'].dropna().quantile(0.8)+0.05, 0.05):
            bets = self.bets[ self.bets['ground_truth'].notnull() & (self.bets['bet_value'] > min_koef) ]
            bets_count = bets.shape[0]
            if bets_count == 0: continue

            koef_mean = bets['bet_value'].mean()
            matches_count = bets['match_uuid'].nunique()
            bets_successful = bets[ bets['ground_truth'] ]
            bets_successful_count = bets_successful.shape[0]
            accurancy = bets_successful_count / bets_count
            roi = bets_successful['bet_value'].sum() / bets_count - 1

            investigation = investigation.append({
               'min_koef': min_koef,
               'koef_mean': koef_mean,
               'matches': matches_count,
               'bets': bets_count,
               'win': bets_successful_count,
               'accurancy': accurancy,
               'roi': roi
            }, ignore_index=True)

        return investigation


    def save(self, file_path):
        with open(file_path, 'wb') as f_out:
            pickle.dump(self, f_out)


    # TODO: Выводить текст, а не числа
    def print_investigation(self, matches_count=None, nrows=10):
        investigation = self.investigate()

        investigation1 = investigation.sort_values(by=['roi', 'min_koef'], ascending=[False, True])[:nrows]
        investigation2 = pd.DataFrame.from_dict({
            'min_koef': investigation1['min_koef'],
            'koef_mean': investigation1['koef_mean'].round(2),
            'matches': (100 * investigation1['matches'].astype(np.int) / matches_count).round(1) if matches_count is not None else None,
            'roi': (100 * investigation1['roi']).round(1),
            'accurancy': (100 * investigation1['accurancy']).round(1)
        })

        res = ''
        res += self.name + '\n\n'
        if self.description is not None:
            res += self.description + '\n\n'
        res += investigation2.to_string(index=False)

        print(res)


    def flush_bets(self, collection):
        for (i, bet) in self.bets.iterrows():
            bet1 = bet.to_dict()
            bet1['date'] = datetime.datetime.strptime(bet['date'], '%Y-%m-%d')
            del bet1['match_uuid']

            bet2 = bet.to_dict()
            bet2['date'] = datetime.datetime.strptime(bet['date'], '%Y-%m-%d')

            collection.update_one(bet1, { '$set': bet2 }, upsert=True)
