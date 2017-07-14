from abc import ABCMeta


class CornersResults1ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Исход', 'матч', '1') ]


class CornersResults1XProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Исход', 'матч', '1X') ]


class CornersResultsX2ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Исход', 'матч', 'X2') ]


class CornersResults2ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Исход', 'матч', '2') ]


class CornersFirstPeriodResults1ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Исход', '1-й тайм', '1') ]


class CornersFirstPeriodResults1XProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Исход', '1-й тайм', '1X') ]


class CornersFirstPeriodResultsX2ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Исход', '1-й тайм', 'X2') ]


class CornersFirstPeriodResults2ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Исход', '1-й тайм', '2') ]


class CornersSecondPeriodResults1ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Исход', '2-й тайм', '1') ]


class CornersSecondPeriodResults1XProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Исход', '2-й тайм', '1X') ]


class CornersSecondPeriodResultsX2ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Исход', '2-й тайм', 'X2') ]


class CornersSecondPeriodResults2ProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Исход', '2-й тайм', '2') ]




class CornersHandicapsHomeProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Фора', 'матч', '1', '*') ]


class CornersHandicapsAwayProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Фора', 'матч', '2', '*') ]


class CornersFirstPeriodHandicapsHomeProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Фора', '1-й тайм', '1', '*') ]


class CornersFirstPeriodHandicapsAwayProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Фора', '1-й тайм', '2', '*') ]


class CornersSecondPeriodHandicapsHomeProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Фора', '2-й тайм', '1', '*') ]


class CornersSecondPeriodHandicapsAwayProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Фора', '2-й тайм', '2', '*') ]




class CornersTotalsGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Тотал', 'матч', '>', '*') ]


class CornersTotalsLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Тотал', 'матч', '<', '*') ]


class CornersFirstPeriodTotalsGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Тотал', '1-й тайм', '>', '*') ]


class CornersFirstPeriodTotalsLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Тотал', '1-й тайм', '<', '*') ]


class CornersSecondPeriodTotalsGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Тотал', '2-й тайм', '>', '*') ]


class CornersSecondPeriodTotalsLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Тотал', '2-й тайм', '<', '*') ]




class CornersIndividualTotalsHomeGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Индивидуальный тотал', 'матч', '1', '>', '*') ]


class CornersIndividualTotalsHomeLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Индивидуальный тотал', 'матч', '1', '<', '*') ]


class CornersIndividualTotalsAwayGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Индивидуальный тотал', 'матч', '2', '>', '*') ]


class CornersIndividualTotalsAwayLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Индивидуальный тотал', 'матч', '2', '<', '*') ]


class CornersFirstPeriodIndividualTotalsHomeGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Индивидуальный тотал', '1-й тайм', '1', '>', '*') ]


class CornersFirstPeriodIndividualTotalsHomeLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Индивидуальный тотал', '1-й тайм', '1', '<', '*') ]


class CornersFirstPeriodIndividualTotalsAwayGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Индивидуальный тотал', '1-й тайм', '2', '>', '*') ]


class CornersFirstPeriodIndividualTotalsAwayLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Индивидуальный тотал', '1-й тайм', '2', '<', '*') ]


class CornersSecondPeriodIndividualTotalsHomeGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Индивидуальный тотал', '2-й тайм', '1', '>', '*') ]


class CornersSecondPeriodIndividualTotalsHomeLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Индивидуальный тотал', '2-й тайм', '1', '<', '*') ]


class CornersSecondPeriodIndividualTotalsAwayGreaterProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Индивидуальный тотал', '2-й тайм', '2', '>', '*') ]


class CornersSecondPeriodIndividualTotalsAwayLesserProposerMixin(metaclass=ABCMeta):

    _candidate_bet_patterns = [ ('УГЛ', 'Индивидуальный тотал', '2-й тайм', '2', '<', '*') ]
