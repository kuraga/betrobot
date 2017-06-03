from betrobot.betting.proposers.result_proposers.result_proposer import ResultProposer


class TotalsGreaterResultProposer(ResultProposer):

    def _handle_bet(self, bet, betcity_match, result_prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        total = bet[4]

        if events_home_count_prediction + events_away_count_prediction > total + self.min_margin:
            self.propose(bet, betcity_match, result_prediction=result_prediction, **kwargs)


class TotalsLesserResultProposer(ResultProposer):

    def _handle_bet(self, bet, betcity_match, result_prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        total = bet[4]

        if events_home_count_prediction + events_away_count_prediction < total - self.min_margin:
            self.propose(bet, betcity_match, result_prediction=result_prediction, **kwargs)
