from betrobot.betting.proposers.result_proposers.result_proposer import ResultProposer


class Results1ResultProposer(ResultProposer):

    def _handle_bet(self, bet, result_prediction, match_header, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction

        if events_home_count_prediction - events_away_count_prediction > self.min_margin:
            self.propose(bet, match_header, result_prediction=result_prediction, **kwargs)


class Results1XResultProposer(ResultProposer):

    def _handle_bet(self, bet, result_prediction, match_header, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction

        if events_home_count_prediction - events_away_count_prediction >= self.min_margin:
            self.propose(bet, match_header, result_prediction=result_prediction, **kwargs)


class ResultsX2ResultProposer(ResultProposer):

    def _handle_bet(self, bet, result_prediction, match_header, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction

        if events_home_count_prediction - events_away_count_prediction <= -self.min_margin:
            self.propose(bet, match_header, result_prediction=result_prediction, **kwargs)


class Results2ResultProposer(ResultProposer):

    def _handle_bet(self, bet, result_prediction, match_header, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction


        if events_home_count_prediction - events_away_count_prediction < -self.min_margin:
            self.propose(bet, match_header, result_prediction=result_prediction, **kwargs)
