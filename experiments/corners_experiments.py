from experiments.standard_experiments_collection import StandardExperimentsCollection

from betrobot.betting.samplers.date_based_samplers import HistoricalSampler, EveSampler

from betrobot.betting.fitters.corners_attack_defense_fitters import CornersAttackDefenseFitter, CornersFirstPeriodAttackDefenseFitter, CornersSecondPeriodAttackDefenseFitter
from betrobot.betting.predictors.corners_attack_defense_predictors import CornersResultProbabilitiesAttackDefensePredictor

from betrobot.betting.proposers.corners_results_proposers import CornersResults1Proposer, CornersResults1XProposer, CornersResultsX2Proposer, CornersResults2Proposer
from betrobot.betting.proposers.corners_period_results_proposers import CornersFirstPeriodResults1Proposer, CornersFirstPeriodResults1XProposer, CornersFirstPeriodResultsX2Proposer, CornersFirstPeriodResults2Proposer, CornersSecondPeriodResults1Proposer, CornersSecondPeriodResults1XProposer, CornersSecondPeriodResultsX2Proposer, CornersSecondPeriodResults2Proposer
from betrobot.betting.proposers.corners_handicaps_proposers import CornersHandicapsHomeProposer, CornersHandicapsAwayProposer
from betrobot.betting.proposers.corners_period_handicaps_proposers import CornersFirstPeriodHandicapsHomeProposer, CornersFirstPeriodHandicapsAwayProposer, CornersSecondPeriodHandicapsHomeProposer, CornersSecondPeriodHandicapsAwayProposer
from betrobot.betting.proposers.corners_totals_proposers import CornersTotalsGreaterProposer, CornersTotalsLesserProposer
from betrobot.betting.proposers.corners_period_totals_proposers import CornersFirstPeriodTotalsGreaterProposer, CornersFirstPeriodTotalsLesserProposer, CornersSecondPeriodTotalsGreaterProposer, CornersSecondPeriodTotalsLesserProposer
from betrobot.betting.proposers.corners_individual_totals_proposers import CornersIndividualTotalsHomeGreaterProposer, CornersIndividualTotalsHomeLesserProposer, CornersIndividualTotalsAwayGreaterProposer, CornersIndividualTotalsAwayLesserProposer
from betrobot.betting.proposers.corners_period_individual_totals_proposers import CornersFirstPeriodIndividualTotalsHomeGreaterProposer, CornersFirstPeriodIndividualTotalsHomeLesserProposer, CornersFirstPeriodIndividualTotalsAwayGreaterProposer, CornersFirstPeriodIndividualTotalsAwayLesserProposer, CornersSecondPeriodIndividualTotalsHomeGreaterProposer, CornersSecondPeriodIndividualTotalsHomeLesserProposer, CornersSecondPeriodIndividualTotalsAwayGreaterProposer, CornersSecondPeriodIndividualTotalsAwayLesserProposer


db_name = 'betrobot'
matches_collection_name = 'matchesCleaned'
sample_condition = {
   'date': { '$regex': '^2017-03' }
}


corners_attack_defense_fitter = CornersAttackDefenseFitter()
corners_first_period_attack_defense_fitter = CornersFirstPeriodAttackDefenseFitter()
corners_second_period_attack_defense_fitter = CornersSecondPeriodAttackDefenseFitter()


corners_result_probabilities_attack_defense_predictor = CornersResultProbabilitiesAttackDefensePredictor()


corners_results_proposers_data = [{
    'name': 'corners_results-1',
    'proposer_class': CornersResults1Proposer
}, {
    'name': 'corners_results-1X',
    'proposer_class': CornersResults1XProposer
}, {
    'name': 'corners_results-X2',
    'proposer_class': CornersResultsX2Proposer
}, {
    'name': 'corners_results-2',
    'proposer_class': CornersResults2Proposer
}]
corners_first_period_results_proposers_data = [{
    'name': 'corners_period_results-first_period-1',
    'proposer_class': CornersFirstPeriodResults1Proposer
}, {
    'name': 'corners_period_results-first_period-1X',
    'proposer_class': CornersFirstPeriodResults1XProposer
}, {
    'name': 'corners_period_results-first_period-X2',
    'proposer_class': CornersFirstPeriodResultsX2Proposer
}, {
    'name': 'corners_period_results-first_period-2',
    'proposer_class': CornersFirstPeriodResults2Proposer
}]
corners_second_period_results_proposers_data = [{
    'name': 'corners_period_results-second_period-1',
    'proposer_class': CornersSecondPeriodResults1Proposer
}, {
    'name': 'corners_period_results-second_period-1X',
    'proposer_class': CornersSecondPeriodResults1XProposer
}, {
    'name': 'corners_period_results-second_period-X2',
    'proposer_class': CornersSecondPeriodResultsX2Proposer
}, {
    'name': 'corners_period_results-second_period-2',
    'proposer_class': CornersSecondPeriodResults2Proposer
}]
corners_handicaps_proposers_data = [{
    'name': 'corners_handicaps-home',
    'proposer_class': CornersHandicapsHomeProposer
}, {
    'name': 'corners_handicaps-away',
    'proposer_class': CornersHandicapsAwayProposer
}]
corners_first_period_handicaps_proposers_data = [{
    'name': 'corners_first_period_handicaps-home',
    'proposer_class': CornersFirstPeriodHandicapsHomeProposer
}, {
    'name': 'corners_first_period_handicaps-away',
    'proposer_class': CornersFirstPeriodHandicapsAwayProposer
}]
corners_second_period_handicaps_proposers_data = [{
    'name': 'corners_second_period_handicaps-home',
    'proposer_class': CornersSecondPeriodHandicapsHomeProposer
}, {
    'name': 'corners_second_period_handicaps-away',
    'proposer_class': CornersSecondPeriodHandicapsAwayProposer
}]
corners_totals_proposers_data = [{
    'name': 'corners_totals-greater',
    'proposer_class': CornersTotalsGreaterProposer
}, {
    'name': 'corners_totals-lesser',
    'proposer_class': CornersTotalsLesserProposer
}]
corners_first_period_totals_proposers_data = [{
    'name': 'corners_first_period_totals-greater',
    'proposer_class': CornersFirstPeriodTotalsGreaterProposer
}, {
    'name': 'corners_first_period_totals-lesser',
    'proposer_class': CornersFirstPeriodTotalsLesserProposer
}]
corners_second_period_totals_proposers_data = [{
    'name': 'corners_second_period_totals-greater',
    'proposer_class': CornersSecondPeriodTotalsGreaterProposer
}, {
    'name': 'corners_second_period_totals-lesser',
    'proposer_class': CornersSecondPeriodTotalsLesserProposer
}]
corners_individual_totals_proposers_data = [{
    'name': 'corners_individual_totals-home-greater',
    'proposer_class': CornersIndividualTotalsHomeGreaterProposer
}, {
    'name': 'corners_individual_totals-home-lesser',
    'proposer_class': CornersIndividualTotalsHomeLesserProposer
}, {
    'name': 'corners_individual_totals-away-greater',
    'proposer_class': CornersIndividualTotalsAwayGreaterProposer
}, {
    'name': 'corners_individual_totals-away-lesser',
    'proposer_class': CornersIndividualTotalsAwayLesserProposer
}]
corners_first_period_individual_totals_proposers_data = [{
    'name': 'corners_first_period_individual_totals-home-greater',
    'proposer_class': CornersFirstPeriodIndividualTotalsHomeGreaterProposer
}, {
    'name': 'corners_first_period_individual_totals-home-lesser',
    'proposer_class': CornersFirstPeriodIndividualTotalsHomeLesserProposer
}, {
    'name': 'corners_first_period_individual_totals-away-greater',
    'proposer_class': CornersFirstPeriodIndividualTotalsAwayGreaterProposer
}, {
    'name': 'corners_first_period_individual_totals-away-lesser',
    'proposer_class': CornersFirstPeriodIndividualTotalsAwayLesserProposer
}]
corners_second_period_individual_totals_proposers_data = [{
    'name': 'corners_second_period_individual_totals-home-greater',
    'proposer_class': CornersSecondPeriodIndividualTotalsHomeGreaterProposer
}, {
    'name': 'corners_second_period_individual_totals-home-lesser',
    'proposer_class': CornersSecondPeriodIndividualTotalsHomeLesserProposer
}, {
    'name': 'corners_second_period_individual_totals-away-greater',
    'proposer_class': CornersSecondPeriodIndividualTotalsAwayGreaterProposer
}, {
    'name': 'corners_second_period_individual_totals-away-lesser',
    'proposer_class': CornersSecondPeriodIndividualTotalsAwayLesserProposer
}]


value_thresholds_data = {
    'corners_results-corners_attack_defense-eve': {
        'corners_results-1': None,
        'corners_results-1X': None,
        'corners_results-X2': 1.8,
        'corners_results-2': 1.8
    },
    'corners_first_period_results-corners_first_period_attack_defense-eve': {
        'corners_period_results-first_period-1': None,
        'corners_period_results-first_period-1X': None,
        'corners_period_results-first_period-X2': 1.8,
        'corners_period_results-first_period-2': 1.8
    },
    'corners_second_period_results-corners_second_period_attack_defense-eve': {
        'corners_period_results-second_period-1': None,
        'corners_period_results-second_period-1X': None,
        'corners_period_results-second_period-X2': 1.8,
        'corners_period_results-second_period-2': None
    },
    'corners_handicaps-corners_attack_defense-eve': {
        'corners_handicaps-home': 1.8,
        'corners_handicaps-away': None,
    },
    'corners_first_period_handicaps-corners_first_period_attack_defense-eve': {
        'corners_first_period_handicaps-home': 1.8,
        'corners_first_period_handicaps-away': None,
    },
    'corners_second_period_handicaps-corners_second_period_attack_defense-eve': {
        'corners_second_period_handicaps-home': 1.8,
        'corners_second_period_handicaps-away': None,
    },
    'corners_totals-corners_attack_defense-eve': {
        'corners_totals-greater': None,
        'corners_totals-lesser': None
    },
    'corners_first_period_totals-corners_first_period_attack_defense-eve': {
        'corners_first_period_totals-greater': None,
        'corners_first_period_totals-lesser': None
    },
    'corners_second_period_totals-corners_second_period_attack_defense-eve': {
        'corners_second_period_totals-greater': None,
        'corners_second_period_totals-lesser': None
    },
    'corners_individual_totals-corners_attack_defense-eve': {
        'corners_individual_totals-home-greater': None,
        'corners_individual_totals-home-lesser': None,
        'corners_individual_totals-away-greater': None,
        'corners_individual_totals-away-lesser': None
    },
    'corners_first_period_individual_totals-corners_attack_defense-eve': {
        'corners_first_period_individual_totals-home-greater': None,
        'corners_first_period_individual_totals-home-lesser': None,
        'corners_first_period_individual_totals-away-greater': None,
        'corners_first_period_individual_totals-away-lesser': None
    },
    'corners_second_period_individual_totals-corners_attack_defense-eve': {
        'corners_second_period_individual_totals-home-greater': None,
        'corners_second_period_individual_totals-home-lesser': None,
        'corners_second_period_individual_totals-away-greater': None,
        'corners_second_period_individual_totals-away-lesser': None
    }
}


train_samplers_data = [{
    'name': 'historical',
    'description': 'Тренировка на исторических данных',
    'sampler': HistoricalSampler(db_name, matches_collection_name),
    'use': False
}, {
    'name': 'eve',
    'description': 'Тренировка на последних 3-х месяцах',
    'sampler': EveSampler(db_name, matches_collection_name),
    'use': True
}]


for train_sampler_data in train_samplers_data:
    if not train_sampler_data['use']:
        continue

    print('Pre-training...')
    train_sampler = train_sampler_data['sampler']
    corners_attack_defense_fitter_fitted_data = corners_attack_defense_fitter.fit(train_sampler)
    corners_first_period_attack_defense_fitter_fitted_data = corners_first_period_attack_defense_fitter.fit(train_sampler)
    corners_second_period_attack_defense_fitter_fitted_data = corners_second_period_attack_defense_fitter.fit(train_sampler)
    print()

    providers_data = [{
        'name': 'corners_results-corners_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Исходы угловых, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': corners_attack_defense_fitter_fitted_data,
        'predictor': corners_result_probabilities_attack_defense_predictor,
        'proposers_data': corners_results_proposers_data
    }, {
        'name': 'corners_first_period_results-corners_first_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Исходы угловых 1-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': corners_first_period_attack_defense_fitter_fitted_data,
        'predictor': corners_result_probabilities_attack_defense_predictor,
        'proposers_data': corners_first_period_results_proposers_data
    }, {
        'name': 'corners_second_period_results-corners_second_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Исходы угловых 2-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': corners_second_period_attack_defense_fitter_fitted_data,
        'predictor': corners_result_probabilities_attack_defense_predictor,
        'proposers_data': corners_second_period_results_proposers_data
    }, {
        'name': 'corners_handicaps-corners_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Форы угловых, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': corners_attack_defense_fitter_fitted_data,
        'predictor': corners_result_probabilities_attack_defense_predictor,
        'proposers_data': corners_handicaps_proposers_data
    }, {
        'name': 'corners_first_period_handicaps-corners_first_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Форы угловых 1-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': corners_first_period_attack_defense_fitter_fitted_data,
        'predictor': corners_result_probabilities_attack_defense_predictor,
        'proposers_data': corners_first_period_handicaps_proposers_data
    }, {
        'name': 'corners_second_period_handicaps-corners_second_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Форы угловых 2-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': corners_second_period_attack_defense_fitter_fitted_data,
        'predictor': corners_result_probabilities_attack_defense_predictor,
        'proposers_data': corners_second_period_handicaps_proposers_data
    }, {
        'name': 'corners_totals-corners_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Тоталы угловых, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': corners_attack_defense_fitter_fitted_data,
        'predictor': corners_result_probabilities_attack_defense_predictor,
        'proposers_data': corners_totals_proposers_data
    }, {
        'name': 'corners_first_period_totals-corners_first_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Тоталы угловых 1-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': corners_first_period_attack_defense_fitter_fitted_data,
        'predictor': corners_result_probabilities_attack_defense_predictor,
        'proposers_data': corners_first_period_totals_proposers_data
    }, {
        'name': 'corners_second_period_totals-corners_second_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Тоталы угловых 2-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': corners_second_period_attack_defense_fitter_fitted_data,
        'predictor': corners_result_probabilities_attack_defense_predictor,
        'proposers_data': corners_second_period_totals_proposers_data
    }, {
        'name': 'corners_individual_totals-corners_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Индивидуальные тоталы угловых, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': corners_attack_defense_fitter_fitted_data,
        'predictor': corners_result_probabilities_attack_defense_predictor,
        'proposers_data': corners_individual_totals_proposers_data
    }, {
        'name': 'corners_first_period_individual_totals-corners_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Индивидуальные тоталы угловых 1-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': corners_first_period_attack_defense_fitter_fitted_data,
        'predictor': corners_result_probabilities_attack_defense_predictor,
        'proposers_data': corners_first_period_individual_totals_proposers_data
    }, {
        'name': 'corners_second_period_individual_totals-corners_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Индивидуальные тоталы угловых 2-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': corners_second_period_attack_defense_fitter_fitted_data,
        'predictor': corners_result_probabilities_attack_defense_predictor,
        'proposers_data': corners_second_period_individual_totals_proposers_data
    }]

    experiments = StandardExperimentsCollection(providers_data, db_name=db_name, matches_collection_name=matches_collection_name, sample_condition=sample_condition, value_thresholds_data=value_thresholds_data)
    experiments.make()
