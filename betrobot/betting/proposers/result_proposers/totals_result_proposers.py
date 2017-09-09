from betrobot.betting.proposers.result_proposers.result_proposer import ResultProposer


class TotalsGreaterResultProposer(ResultProposer):

    def _handle_bet(self, bet, result_prediction, match_header, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        total = bet['pattern'][4]

        if events_home_count_prediction + events_away_count_prediction > total + self.min_margin:
            self.propose(bet, match_header, **kwargs)


class TotalsLesserResultProposer(ResultProposer):

    def _handle_bet(self, bet, result_prediction, match_header, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        total = bet['pattern'][4]

        if events_home_count_prediction + events_away_count_prediction < total - self.min_margin:
            self.propose(bet, match_header, **kwargs)
