import numpy as np
from betrobot.betting.proposers.results_result_proposer_mixins.results_result_proposer_mixin import ResultsResultProposerMixin


class Results1ResultsResultProposerMixin(ResultsResultProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = prediction
        if events_home_count_prediction - events_away_count_prediction > self.min_diff:
            self.propose(bet, betcity_match, **kwargs)


class Results1XResultsResultProposerMixin(ResultsResultProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = prediction
        if events_home_count_prediction - events_away_count_prediction >= self.min_diff:
            self.propose(bet, betcity_match, **kwargs)


class ResultsX2ResultsResultProposerMixin(ResultsResultProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = prediction
        if events_home_count_prediction - events_away_count_prediction <= -self.min_diff:
            self.propose(bet, betcity_match, **kwargs)


class Results2ResultsResultProposerMixin(ResultsResultProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = prediction
        if events_home_count_prediction - events_away_count_prediction < -self.min_diff:
            self.propose(bet, betcity_match, **kwargs)
