from betrobot.betting.proposers.result_proposers.result_proposer import ResultProposer
from betrobot.betting.sport_util import get_bets


class HandicapsHomeResultProposer(ResultProposer):

    def _handle_bet(self, bet, betcity_match, result_prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        handicap = bet[4]

        if events_home_count_prediction - events_away_count_prediction + handicap > self.min_margin:
            self.propose(bet, betcity_match, result_prediction=result_prediction, **kwargs)


class HandicapsAwayResultProposer(ResultProposer):

    def _handle_bet(self, bet, betcity_match, result_prediction, **kwargs):
        (events_home_count_prediction, events_away_count_prediction) = result_prediction
        handicap = bet[4]

        if events_home_count_prediction - events_away_count_prediction + handicap < -self.min_margin:
            self.propose(bet, betcity_match, result_prediction=result_prediction, **kwargs)
