from betrobot.betting.proposer import Proposer
from betrobot.betting.sport_util import filter_bets


class CombinedHandicapsHomeProposer(Proposer):

    def _handle_bets(self, bets, match_header, combined_prediction, **kwargs):
        home_handicap_bets_patterns = [ ('УГЛ', 'Фора', 'матч', '1', '*') ]
        home_handicap_bets = filter_bets(home_handicap_bets_patterns, bets)
        for bet in home_handicap_bets:
            handicap = bet['pattern'][4]
            self._handle_as_home_handicap(bet, handicap, combined_prediction, match_header, **kwargs)


    def _handle_as_home_handicap(self, bet, handicap, combined_prediction, match_header, **kwargs):
        (home_number, away_number) = combined_prediction

        if home_number < -1:
            return
        if away_number > 1:
            return

        if (handicap >= -1 and (home_number - away_number) >= 6) or \
          (handicap >= -0.5 and (home_number - away_number) >= 3) or \
          (handicap >= 0 and (home_number - away_number) >= 0):
            self.propose(bet, match_header, combined_prediction=combined_prediction, **kwargs)


class CombinedHandicapsAwayProposer(Proposer):

    def _handle_bets(self, bets, match_header, combined_prediction, **kwargs):
        away_handicap_bets_patterns = [ ('УГЛ', 'Фора', 'матч', '2', '*') ]
        away_handicap_bets = filter_bets(away_handicap_bets_patterns, bets)
        for bet in away_handicap_bets:
            handicap = bet['pattern'][4]
            self._handle_as_away_handicap(bet, handicap, combined_prediction, match_header, **kwargs)


    def _handle_as_away_handicap(self, bet, handicap, combined_prediction, match_header, **kwargs):
        (home_number, away_number) = combined_prediction

        if away_number < -1:
            return
        if home_number > 1:
            return

        if (handicap >= -1 and (away_number - home_number) >= 6) or \
          (handicap >= -0.5 and (away_number - home_number) >= 3) or \
          (handicap >= 0 and (away_number - home_number) >= 0):
            self.propose(bet, match_header, combined_prediction=combined_prediction, **kwargs)
