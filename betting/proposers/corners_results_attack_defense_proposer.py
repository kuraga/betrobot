from betting.proposers.corners_results_proposer import CornersResultsProposer


class CornersResults1AttackDefenseProposer(CornersResultsProposer):

    def _handle(self, betcity_match, corners_predicted_home, corners_predicted_away, whoscored_match=None):
        # Делаем ставку на победу на победу хозяев, если предсказанный тотал хозяев превышает предсказанный тотал гостей хотя бы на 2
        if corners_predicted_home - corners_predicted_away >= 2:
            bet_pattern = ('УГЛ', 'Исход', None, '1', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class CornersResults1XAttackDefenseProposer(CornersResultsProposer):

    def _handle(self, betcity_match, corners_predicted_home, corners_predicted_away, whoscored_match=None):
        # Делаем ставку на победу на победу хозяев или ничью, если предсказанный тотал хозяев превышает предсказанный тотал гостей хотя бы на 1
        if corners_predicted_home - corners_predicted_away >= 1:
            bet_pattern = ('УГЛ', 'Исход', None, '1X', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class CornersResultsX2AttackDefenseProposer(CornersResultsProposer):

    def _handle(self, betcity_match, corners_predicted_home, corners_predicted_away, whoscored_match=None):
        # Делаем ставку на победу на победу гостей или ничью, если предсказанный тотал гостей превышает предсказанный тотал хозяев хотя бы на 1
        if corners_predicted_home - corners_predicted_away <= -1:
            bet_pattern = ('УГЛ', 'Исход', None, 'X2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)


class CornersResults2AttackDefenseProposer(CornersResultsProposer):

    def _handle(self, betcity_match, corners_predicted_home, corners_predicted_away, whoscored_match=None):
        # Делаем ставку на победу на победу гостей, если предсказанный тотал гостей превышает предсказанный тотал хозяев хотя бы на 2
        if corners_predicted_home - corners_predicted_away <= -2:
            bet_pattern = ('УГЛ', 'Исход', None, '2', None)
            self.propose(bet_pattern, betcity_match, whoscored_match=whoscored_match)
