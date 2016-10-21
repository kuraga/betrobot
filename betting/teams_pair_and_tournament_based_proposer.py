import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')

from proposer import Proposer
from model import Model
from sport_util import get_whoscored_tournament_id_of_betcity_match, get_whoscored_team_ids_of_betcity_match
from common_util import list_wrap


class TeamsPairAndTournnamentBasedProposer(Proposer):

    def __init__(self, betting_session, model_name_pattern):
        Proposer.__init__(self, betting_session)

        self._model_name_patterns = list_wrap(model_name_pattern)


    def _predict(self, betcity_match, model_index=0):
        tournament_id = get_whoscored_tournament_id_of_betcity_match(betcity_match)
        if tournament_id is None:
            return None
        model_name_pattern = self._model_name_patterns[model_index]
        model_name = model_name_pattern % (tournament_id,)
        model = Model.get(model_name)
        if model is None:
            return None

        (whoscored_home, whoscored_away) = get_whoscored_team_ids_of_betcity_match(betcity_match)
        if whoscored_home is None or whoscored_away is None:
            return None

        return model.predict(whoscored_home, whoscored_away)
