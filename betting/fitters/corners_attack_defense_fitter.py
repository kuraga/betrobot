import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./betting/fitters')


from attack_defense_fitter import AttackDefenseFitter
from sport_util import is_corner


class CornersAttackDefenseFitter(AttackDefenseFitter):
    def __init__(self):
        corners_condition = is_corner
        AttackDefenseFitter.__init__(self, corners_condition)
