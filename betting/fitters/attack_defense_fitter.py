import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./betting/fitters')


from teams_pair_and_tournament_based_fitter import TeamsPairAndTournamentBasedFitter


class AttackDefenseFitter(TeamsPairAndTournamentBasedFitter):
    def __init__(self, condition):
        TeamsPairAndTournamentBasedFitter.__init__(self, condition)
