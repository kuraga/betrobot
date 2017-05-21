import numpy as np
from betrobot.betting.proposers.result_proposer_mixins.result_proposer_mixin import ResultProposerMixin


class Results1ResultProposerMixin(ResultProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = prediction
        if events_home_count_prediction - events_away_count_prediction > self.min_diff:
            self.propose(bet, betcity_match, **kwargs)


class Results1XResultProposerMixin(ResultProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = prediction
        if events_home_count_prediction - events_away_count_prediction >= self.min_diff:
            self.propose(bet, betcity_match, **kwargs)


class ResultsX2ResultProposerMixin(ResultProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = prediction
        if events_home_count_prediction - events_away_count_prediction <= -self.min_diff:
            self.propose(bet, betcity_match, **kwargs)


class Results2ResultProposerMixin(ResultProposerMixin):

    def _handle_bet(self, bet, betcity_match, prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = prediction
        if events_home_count_prediction - events_away_count_prediction < -self.min_diff:
            self.propose(bet, betcity_match, **kwargs)
