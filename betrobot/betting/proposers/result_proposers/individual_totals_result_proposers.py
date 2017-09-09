from betrobot.betting.proposers.result_proposers.result_proposer import ResultProposer


class IndividualTotalsHomeGreaterResultProposer(ResultProposer):

    def _handle_bet(self, bet, result_prediction, match_header, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        individual_total = bet['pattern'][5]

        if events_home_count_prediction > individual_total + self.min_margin / 2:
            self.propose(bet, match_header, **kwargs)


class IndividualTotalsHomeLesserResultProposer(ResultProposer):

    def _handle_bet(self, bet, result_prediction, match_header, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        individual_total = bet['pattern'][5]

        if events_home_count_prediction < individual_total - self.min_margin / 2:
            self.propose(bet, match_header, **kwargs)


class IndividualTotalsAwayGreaterResultProposer(ResultProposer):

    def _handle_bet(self, bet, result_prediction, match_header, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        individual_total = bet['pattern'][5]

        if events_away_count_prediction > individual_total + self.min_margin / 2:
            self.propose(bet, match_header, **kwargs)


class IndividualTotalsAwayLesserResultProposer(ResultProposer):

    def _handle_bet(self, bet, result_prediction, match_header, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        individual_total = bet['pattern'][5]

        if events_away_count_prediction < individual_total - self.min_margin / 2:
            self.propose(bet, match_header, **kwargs)
