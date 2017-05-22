from betrobot.betting.proposers.result_proposers.result_proposer import ResultProposer


class Results1ResultProposer(ResultProposer):

    def _handle_bet(self, bet, betcity_match, result_prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction

        if events_home_count_prediction - events_away_count_prediction > self.min_events_count_diff_for_win:
            self.propose(bet, betcity_match, result_prediction=result_prediction, **kwargs)


class Results1XResultProposer(ResultProposer):

    def _handle_bet(self, bet, betcity_match, result_prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction

        if events_home_count_prediction - events_away_count_prediction >= self.min_events_count_diff_for_win:
            self.propose(bet, betcity_match, result_prediction=result_prediction, **kwargs)


class ResultsX2ResultProposer(ResultProposer):

    def _handle_bet(self, bet, betcity_match, result_prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction

        if events_home_count_prediction - events_away_count_prediction <= -self.min_events_count_diff_for_win:
            self.propose(bet, betcity_match, result_prediction=result_prediction, **kwargs)


class Results2ResultProposer(ResultProposer):

    def _handle_bet(self, bet, betcity_match, result_prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction

        if events_home_count_prediction - events_away_count_prediction < -self.min_events_count_diff_for_win:
            self.propose(bet, betcity_match, result_prediction=result_prediction, **kwargs)
