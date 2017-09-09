from betrobot.betting.proposer import Proposer
from betrobot.betting.sport_util import filter_bets


class CombinedHandicapsHomeProposerMixin:

    def _handle_bets(self, bets, match_header, prediction_info, **kwargs):
        bets_1 = filter_bets(self._bets_1_patterns, bets)
        for bet in bets_1:
            handicap = -0.5
            self._handle_as_home_handicap(bet, handicap, prediction_info, match_header, **kwargs)

        bets_1X = filter_bets(self._bets_1X_patterns, bets)
        for bet in bets_1X:
            handicap = 0.5
            self._handle_as_home_handicap(bet, handicap, prediction_info, match_header, **kwargs)

        home_handicap_bets = filter_bets(self._home_handicap_bets_patterns, bets)
        for bet in home_handicap_bets:
            handicap = bet['pattern'][4]
            self._handle_as_home_handicap(bet, handicap, prediction_info, match_header, **kwargs)


    def _handle_as_home_handicap(self, bet, handicap, prediction_info, match_header, **kwargs):
        combined_prediction = prediction_info['prediction']
        (home_number, away_number) = combined_prediction

        if home_number < -1:
            return
        if away_number > 1:
            return

        if (handicap >= -1 and (home_number - away_number) >= 6) or \
          (handicap >= -0.5 and (home_number - away_number) >= 3) or \
          (handicap >= 0 and (home_number - away_number) >= 0):
            self.propose(bet, match_header, prediction_info, **kwargs)


class CombinedHandicapsAwayProposerMixin:

    def _handle_bets(self, bets, match_header, prediction_info, **kwargs):
        bets_X2 = filter_bets(self._bets_X2_patterns, bets)
        for bet in bets_X2:
            handicap = 0.5
            self._handle_as_away_handicap(bet, handicap, prediction_info, match_header, **kwargs)

        bets_2 = filter_bets(self._bets_2_patterns, bets)
        for bet in bets_2:
            handicap = -0.5
            self._handle_as_away_handicap(bet, handicap, prediction_info, match_header, **kwargs)

        away_handicap_bets = filter_bets(self._away_handicap_bets_patterns, bets)
        for bet in away_handicap_bets:
            handicap = bet['pattern'][4]
            self._handle_as_away_handicap(bet, handicap, prediction_info, match_header, **kwargs)


    def _handle_as_away_handicap(self, bet, handicap, prediction_info, match_header, **kwargs):
        combined_prediction = prediction_info['prediction']
        (home_number, away_number) = combined_prediction

        if away_number < -1:
            return
        if home_number > 1:
            return

        if (handicap >= -1 and (away_number - home_number) >= 6) or \
          (handicap >= -0.5 and (away_number - home_number) >= 3) or \
          (handicap >= 0 and (away_number - home_number) >= 0):
            self.propose(bet, match_header, prediction_info, **kwargs)


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
