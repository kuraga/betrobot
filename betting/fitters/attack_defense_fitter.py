from betting.fitters.teams_pair_and_tournament_based_fitter import TeamsPairAndTournamentBasedFitter


class AttackDefenseFitter(TeamsPairAndTournamentBasedFitter):
    def __init__(self, condition):
        TeamsPairAndTournamentBasedFitter.__init__(self, condition)
