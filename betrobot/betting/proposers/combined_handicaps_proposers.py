import numpy as np
from betrobot.betting.proposer import Proposer
from betrobot.betting.sport_util import filter_bets


class CombinedHandicapsHomeProposerMixin:

    def _handle_bets(self, bets, match_header, prediction_info, **kwargs):
        propositions = []

        bets_1 = filter_bets(self._bets_1_patterns, bets)
        for bet in bets_1:
            handicap = -0.5
            if self._handle_as_home_handicap(bet, handicap, prediction_info, match_header, **kwargs):
                propositions.append(bet)

        bets_1X = filter_bets(self._bets_1X_patterns, bets)
        for bet in bets_1X:
            handicap = 0.5
            if self._handle_as_home_handicap(bet, handicap, prediction_info, match_header, **kwargs):
                propositions.append(bet)

        home_handicap_bets = filter_bets(self._home_handicap_bets_patterns, bets)
        for bet in home_handicap_bets:
            handicap = bet['pattern'][4]
            if self._handle_as_home_handicap(bet, handicap, prediction_info, match_header, **kwargs):
                propositions.append(bet)

        # Оставляем одну ставку: с минимальным, но приемлимым коэффициентом
        proposition_coeffs = [ bet['value'] for bet in propositions ]
        big_proposition_coeffs = [ bet_value if bet_value >= 1.8 else np.nan for bet_value in proposition_coeffs ]
        if not np.all(np.isnan(big_proposition_coeffs)):
            good_bet_index = np.nanargmin(big_proposition_coeffs)
            good_bet = propositions[good_bet_index]
            self.propose(good_bet, match_header, prediction_info, **kwargs)


    def _handle_as_home_handicap(self, bet, handicap, prediction_info, match_header, **kwargs):
        combined_prediction = prediction_info['prediction']
        (home_number, away_number) = combined_prediction

        if home_number < -1:
            return False
        if away_number > 1:
            return False

        return (handicap >= -1 and (home_number - away_number) >= 6) or \
          (handicap >= -0.5 and (home_number - away_number) >= 3) or \
          (handicap >= 0 and (home_number - away_number) >= 0)


class CombinedHandicapsAwayProposerMixin:

    def _handle_bets(self, bets, match_header, prediction_info, **kwargs):
        propositions = []

        bets_X2 = filter_bets(self._bets_X2_patterns, bets)
        for bet in bets_X2:
            handicap = 0.5
            if self._handle_as_away_handicap(bet, handicap, prediction_info, match_header, **kwargs):
                propositions.append(bet)

        bets_2 = filter_bets(self._bets_2_patterns, bets)
        for bet in bets_2:
            handicap = -0.5
            if self._handle_as_away_handicap(bet, handicap, prediction_info, match_header, **kwargs):
                propositions.append(bet)

        away_handicap_bets = filter_bets(self._away_handicap_bets_patterns, bets)
        for bet in away_handicap_bets:
            handicap = bet['pattern'][4]
            if self._handle_as_away_handicap(bet, handicap, prediction_info, match_header, **kwargs):
                propositions.append(bet)

        # Оставляем одну ставку: с минимальным, но приемлимым коэффициентом
        proposition_coeffs = [ bet['value'] for bet in propositions ]
        big_proposition_coeffs = [ bet_value if bet_value >= 1.8 else np.nan for bet_value in proposition_coeffs ]
        if not np.all(np.isnan(big_proposition_coeffs)):
            good_bet_index = np.nanargmin(big_proposition_coeffs)
            good_bet = propositions[good_bet_index]
            self.propose(good_bet, match_header, prediction_info, **kwargs)


    def _handle_as_away_handicap(self, bet, handicap, prediction_info, match_header, **kwargs):
        combined_prediction = prediction_info['prediction']
        (home_number, away_number) = combined_prediction

        if away_number < -1:
            return False
        if home_number > 1:
            return False

        return (handicap >= -1 and (away_number - home_number) >= 6) or \
          (handicap >= -0.5 and (away_number - home_number) >= 3) or \
          (handicap >= 0 and (away_number - home_number) >= 0)


class CombinedHandicapsHomeProposer(CombinedHandicapsHomeProposerMixin, Proposer):

    _bets_1_patterns = [ ('УГЛ', 'Исход', 'матч', '1') ]
    _bets_1X_patterns = [ ('УГЛ', 'Исход', 'матч', '1X') ]
    _home_handicap_bets_patterns = [ ('УГЛ', 'Фора', 'матч', '1', '*') ]


class CombinedHandicapsAwayProposer(CombinedHandicapsAwayProposerMixin, Proposer):

    _bets_X2_patterns = [ ('УГЛ', 'Исход', 'матч', 'X2') ]
    _bets_2_patterns = [ ('УГЛ', 'Исход', 'матч', '2') ]
    _away_handicap_bets_patterns = [ ('УГЛ', 'Фора', 'матч', '2', '*') ]


class CombinedFirstPeriodHandicapsHomeProposer(CombinedHandicapsHomeProposerMixin, Proposer):

    _bets_1_patterns = [ ('УГЛ', 'Исход', '1-й тайм', '1') ]
    _bets_1X_patterns = [ ('УГЛ', 'Исход', '1-й тайм', '1X') ]
    _home_handicap_bets_patterns = [ ('УГЛ', 'Фора', '1-й тайм', '1', '*') ]


class CombinedFirstPeriodHandicapsAwayProposer(CombinedHandicapsAwayProposerMixin, Proposer):

    _bets_X2_patterns = [ ('УГЛ', 'Исход', '1-й тайм', 'X2') ]
    _bets_2_patterns = [ ('УГЛ', 'Исход', '1-й тайм', '2') ]
    _away_handicap_bets_patterns = [ ('УГЛ', 'Фора', '1-й тайм', '2', '*') ]
