from betrobot.betting.proposer import Proposer


class CombinedHandicapsHomeProposer(Proposer):

    _candidate_bet_patterns = [ ('УГЛ', 'Фора', 'матч', '1', '*') ]


    def _handle_bet(self, bet, combined_prediction, match_header, **kwargs):
        (home_number, away_number) = combined_prediction
        handicap = bet['pattern'][4]

        if home_number < -1:
            return
        if away_number > 1:
            return

        if (handicap >= -1 and (home_number - away_number) >= 6) or \
          (handicap >= -0.5 and (home_number - away_number) >= 3) or \
          (handicap >= 0 and (home_number - away_number) >= 0):
            self.propose(bet, match_header, combined_prediction=combined_prediction, **kwargs)


class CombinedHandicapsAwayProposer(Proposer):

    _candidate_bet_patterns = [ ('УГЛ', 'Фора', 'матч', '2', '*') ]


    def _handle_bet(self, bet, combined_prediction, match_header, **kwargs):
        (home_number, away_number) = combined_prediction
        handicap = bet['pattern'][4]

        if away_number < -1:
            return
        if home_number > 1:
            return

        if (handicap >= -1 and (away_number - home_number) >= 6) or \
          (handicap >= -0.5 and (away_number - home_number) >= 3) or \
          (handicap >= 0 and (away_number - home_number) >= 0):
            self.propose(bet, match_header, combined_prediction=combined_prediction, **kwargs)
