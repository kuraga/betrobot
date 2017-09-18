from abc import ABCMeta


class GoalsResults1ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Исход', 'матч', '1') ]


class GoalsResults1XProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Исход', 'матч', '1X') ]


class GoalsResultsX2ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Исход', 'матч', 'X2') ]


class GoalsResults2ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Исход', 'матч', '2') ]


class GoalsFirstPeriodResults1ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Исход', '1-й тайм', '1') ]


class GoalsFirstPeriodResults1XProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Исход', '1-й тайм', '1X') ]


class GoalsFirstPeriodResultsX2ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Исход', '1-й тайм', 'X2') ]


class GoalsFirstPeriodResults2ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Исход', '1-й тайм', '2') ]


class GoalsSecondPeriodResults1ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Исход', '2-й тайм', '1') ]


class GoalsSecondPeriodResults1XProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Исход', '2-й тайм', '1X') ]


class GoalsSecondPeriodResultsX2ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Исход', '2-й тайм', 'X2') ]


class GoalsSecondPeriodResults2ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Исход', '2-й тайм', '2') ]




class GoalsHandicapsHomeProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Фора', 'матч', '1', '*') ]


class GoalsHandicapsAwayProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Фора', 'матч', '2', '*') ]


class GoalsFirstPeriodHandicapsHomeProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Фора', '1-й тайм', '1', '*') ]


class GoalsFirstPeriodHandicapsAwayProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Фора', '1-й тайм', '2', '*') ]


class GoalsSecondPeriodHandicapsHomeProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Фора', '2-й тайм', '1', '*') ]


class GoalsSecondPeriodHandicapsAwayProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Фора', '2-й тайм', '2', '*') ]




class GoalsTotalsGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Тотал', 'матч', '>', '*') ]


class GoalsTotalsLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Тотал', 'матч', '<', '*') ]


class GoalsFirstPeriodTotalsGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Тотал', '1-й тайм', '>', '*') ]


class GoalsFirstPeriodTotalsLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Тотал', '1-й тайм', '<', '*') ]


class GoalsSecondPeriodTotalsGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Тотал', '2-й тайм', '>', '*') ]


class GoalsSecondPeriodTotalsLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Тотал', '2-й тайм', '<', '*') ]




class GoalsIndividualTotalsHomeGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Индивидуальный тотал', 'матч', '1', '>', '*') ]


class GoalsIndividualTotalsHomeLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Индивидуальный тотал', 'матч', '1', '<', '*') ]


class GoalsIndividualTotalsAwayGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Индивидуальный тотал', 'матч', '2', '>', '*') ]


class GoalsIndividualTotalsAwayLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Индивидуальный тотал', 'матч', '2', '<', '*') ]


class GoalsFirstPeriodIndividualTotalsHomeGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Индивидуальный тотал', '1-й тайм', '1', '>', '*') ]


class GoalsFirstPeriodIndividualTotalsHomeLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Индивидуальный тотал', '1-й тайм', '1', '<', '*') ]


class GoalsFirstPeriodIndividualTotalsAwayGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Индивидуальный тотал', '1-й тайм', '2', '>', '*') ]


class GoalsFirstPeriodIndividualTotalsAwayLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Индивидуальный тотал', '1-й тайм', '2', '<', '*') ]


class GoalsSecondPeriodIndividualTotalsHomeGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Индивидуальный тотал', '2-й тайм', '1', '>', '*') ]


class GoalsSecondPeriodIndividualTotalsHomeLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Индивидуальный тотал', '2-й тайм', '1', '<', '*') ]


class GoalsSecondPeriodIndividualTotalsAwayGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Индивидуальный тотал', '2-й тайм', '2', '>', '*') ]


class GoalsSecondPeriodIndividualTotalsAwayLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ (None, 'Индивидуальный тотал', '2-й тайм', '2', '<', '*') ]
