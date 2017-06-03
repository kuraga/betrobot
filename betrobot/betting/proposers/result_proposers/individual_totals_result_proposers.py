from betrobot.betting.proposers.result_proposers.result_proposer import ResultProposer


class IndividualTotalsHomeGreaterResultProposer(ResultProposer):

    def _handle_bet(self, bet, betcity_match, result_prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        individual_total = bet[4]

        if events_home_count_prediction > individual_total + self.min_margin / 2:
            self.propose(bet, betcity_match, result_prediction=result_prediction, **kwargs)


class IndividualTotalsHomeLesserResultProposer(ResultProposer):

    def _handle_bet(self, bet, betcity_match, result_prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        individual_total = bet[4]

        if events_home_count_prediction < individual_total - self.min_margin / 2:
            self.propose(bet, betcity_match, result_prediction=result_prediction, **kwargs)


class IndividualTotalsAwayGreaterResultProposer(ResultProposer):

    def _handle_bet(self, bet, betcity_match, result_prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        individual_total = bet[4]

        if events_away_count_prediction > individual_total + self.min_margin / 2:
            self.propose(bet, betcity_match, result_prediction=result_prediction, **kwargs)


class IndividualTotalsAwayLesserResultProposer(ResultProposer):

    def _handle_bet(self, bet, betcity_match, result_prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        individual_total = bet[4]

        if events_away_count_prediction < individual_total - self.min_margin / 2:
            self.propose(bet, betcity_match, result_prediction=result_prediction, **kwargs)
