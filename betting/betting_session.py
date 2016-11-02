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

        self.bets = pd.DataFrame(columns=['match_uuid', 'tournament', 'date', 'home', 'away', 'match_special_word', 'bet_pattern', 'bet_value', 'ground_truth'])
        self._attempt_count = 0


    def _append_bet(self, match_uuid, tournament, date, home, away, match_special_word, bet_pattern, bet_value, ground_truth):
        bet = {
            'match_uuid': match_uuid,
            'tournament': tournament,
            'date': date,
            'home': home,
            'away': away,
            'match_special_word': match_special_word,
            'bet_pattern': bet_pattern,
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
        self._append_bet(betarch_match['uuid'], betarch_match['tournament'], betarch_match['date'], betarch_match['home'], betarch_match['away'], betarch_match['specialWord'], bet_pattern, bet_value, ground_truth)



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
