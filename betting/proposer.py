import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')


from common_util import list_wrap
from sport_util import get_bet
from check_util import check_bet
from betting_session import BettingSession


class Proposer(object):

    def __init__(self, betting_sessions=None, thresholds=None):
        if betting_sessions is None:
            betting_sessions = BettingSession('default')

        if isinstance(betting_sessions, dict):
            self.betting_sessions = betting_sessions
        else:
            # TODO: Перейти на ordereddict
            self.betting_sessions = { betting_session.name: betting_session for betting_session in list_wrap(betting_sessions) }

        if isinstance(thresholds, dict):
            self._thresholds = thresolds
        else:
            self._thresholds = { 'default': thresholds }


    def _propose(self, bet_pattern, betcity_match, session_key='default', ground_truth=None, whoscored_match=None):
        bet = get_bet(bet_pattern, betcity_match)
        if bet is None:
            return

        threshold = self._thresholds.get(session_key)

        if ground_truth is None and whoscored_match is not None:
            ground_truth = check_bet(bet, betcity_match['specialWord'], whoscored_match)

        # TODO: Обрабатывать значения threshold, запрещающие ставку
        if threshold is None or bet[5] >= threshold:
            self.betting_sessions[session_key].make_bet(betcity_match, bet, ground_truth)


    def flush(self, collection, session_keys=None):
        if session_keys is None:
            session_keys = list(self.betting_sessions.keys())
        else:
            session_keys = list_wrap(session_keys)

        for session_key in session_keys:
            self.betting_sessions[session_key].flush_bets(collection)


    def to_string(self):
        res = ''

        for betting_session in self.betting_sessions.values():
            res += betting_session.to_string() + '\n'

        return res
