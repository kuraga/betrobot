import pymongo
import os
import pickle
from betrobot.betting.provider import Provider
from betrobot.betting.experimentor import Experimentor
from betrobot.util.common_util import safe_get

from betrobot.betting.samplers.date_based_samplers import HistoricalSampler, EveSampler
from betrobot.betting.fitters.corners_attack_defense_fitters import CornersAttackDefenseFitter, CornersFirstPeriodAttackDefenseFitter, CornersSecondPeriodAttackDefenseFitter
from betrobot.betting.predictors.corners_attack_defense_predictors import CornersResultProbabilitiesAttackDefensePredictor
from betrobot.betting.proposers.corners_results_proposers import CornersResults1Proposer, CornersResults1XProposer, CornersResultsX2Proposer, CornersResults2Proposer
from betrobot.betting.proposers.corners_totals_proposers import CornersTotalsGreaterProposer, CornersTotalsLesserProposer
from betrobot.betting.proposers.corners_period_results_proposers import CornersFirstPeriodResults1Proposer, CornersFirstPeriodResults1XProposer, CornersFirstPeriodResultsX2Proposer, CornersFirstPeriodResults2Proposer, CornersSecondPeriodResults1Proposer, CornersSecondPeriodResults1XProposer, CornersSecondPeriodResultsX2Proposer, CornersSecondPeriodResults2Proposer
from betrobot.betting.proposers.corners_handicaps_proposers import CornersHandicapsHomeProposer, CornersHandicapsAwayProposer
from betrobot.betting.proposers.corners_period_handicaps_proposers import CornersFirstPeriodHandicapsHomeProposer, CornersFirstPeriodHandicapsAwayProposer, CornersSecondPeriodHandicapsHomeProposer, CornersSecondPeriodHandicapsAwayProposer
from betrobot.betting.proposers.corners_period_totals_proposers import CornersFirstPeriodTotalsGreaterProposer, CornersFirstPeriodTotalsLesserProposer, CornersSecondPeriodTotalsGreaterProposer, CornersSecondPeriodTotalsLesserProposer
from betrobot.betting.proposers.corners_individual_totals_proposers import CornersIndividualTotalsHomeGreaterProposer, CornersIndividualTotalsHomeLesserProposer, CornersIndividualTotalsAwayGreaterProposer, CornersIndividualTotalsAwayLesserProposer
from betrobot.betting.proposers.corners_period_individual_totals_proposers import CornersFirstPeriodIndividualTotalsHomeGreaterProposer, CornersFirstPeriodIndividualTotalsHomeLesserProposer, CornersFirstPeriodIndividualTotalsAwayGreaterProposer, CornersFirstPeriodIndividualTotalsAwayLesserProposer, CornersSecondPeriodIndividualTotalsHomeGreaterProposer, CornersSecondPeriodIndividualTotalsHomeLesserProposer, CornersSecondPeriodIndividualTotalsAwayGreaterProposer, CornersSecondPeriodIndividualTotalsAwayLesserProposer


def set_thresholds(provider, thresholds_data):
    for proposer_data in provider.proposers_data:
        proposer_name = proposer_data['name']
        proposer = proposer_data['proposer']

        provider_propsers_thresholds_data = safe_get(thresholds_data, provider.name, {})
        threshold = safe_get(provider_propsers_thresholds_data, proposer_name, None)
        proposer.set_threshold(threshold)


def make_experiment(provider, db_name, matches_collection_name, sample_condition):
    experimentor = Experimentor(provider, db_name, matches_collection_name, sample_condition)

    print('Training...')
    experimentor.train()
    print()

    print('Testing...')
    experimentor.test()
    print()

    print('Results')
    print(experimentor.get_investigation())
    print()

    print('Saving...')
    file_name = '%s.pkl' % (provider.name,)
    file_path = os.path.join('data', 'providers', file_name)
    with open(file_path, 'wb') as f:
        pickle.dump(provider, f)

    return experimentor


db_name = 'betrobot'
matches_collection_name = 'matchesCleaned'
sample_condition = { 'date': { '$regex': '^2017-02|^2017-03' } }


train_samplers = {
    # 'historical': HistoricalSampler(db_name, matches_collection_name),
    'eve': EveSampler(db_name, matches_collection_name)
}

corners_attack_defense_fitter = CornersAttackDefenseFitter()
corners_first_period_attack_defense_fitter = CornersFirstPeriodAttackDefenseFitter()
corners_second_period_attack_defense_fitter = CornersSecondPeriodAttackDefenseFitter()

corners_result_probabilities_attack_defense_predictor = CornersResultProbabilitiesAttackDefensePredictor()

corners_results_proposers_data = [{
    'name': 'corners_results-1',
    'proposer': CornersResults1Proposer()
}, {
    'name': 'corners_results-1X',
    'proposer': CornersResults1XProposer()
}, {
    'name': 'corners_results-X2',
    'proposer': CornersResultsX2Proposer()
}, {
    'name': 'corners_results-2',
    'proposer': CornersResults2Proposer()
}]
corners_first_period_results_proposers_data = [{
    'name': 'corners_period_results-first_period-1',
    'proposer': CornersFirstPeriodResults1Proposer()
}, {
    'name': 'corners_period_results-first_period-1X',
    'proposer': CornersFirstPeriodResults1XProposer()
}, {
    'name': 'corners_period_results-first_period-X2',
    'proposer': CornersFirstPeriodResultsX2Proposer()
}, {
    'name': 'corners_period_results-first_period-2',
    'proposer': CornersFirstPeriodResults2Proposer()
}]
corners_second_period_results_proposers_data = [{
    'name': 'corners_period_results-second_period-1',
    'proposer': CornersSecondPeriodResults1Proposer()
}, {
    'name': 'corners_period_results-second_period-1X',
    'proposer': CornersSecondPeriodResults1XProposer()
}, {
    'name': 'corners_period_results-second_period-X2',
    'proposer': CornersSecondPeriodResultsX2Proposer()
}, {
    'name': 'corners_period_results-second_period-2',
    'proposer': CornersSecondPeriodResults2Proposer()
}]
corners_totals_proposers_data = [{
    'name': 'corners_totals-greater',
    'proposer': CornersTotalsGreaterProposer()
}, {
    'name': 'corners_totals-lesser',
    'proposer': CornersTotalsLesserProposer()
}]
corners_handicaps_proposers_data = [{
    'name': 'corners_handicaps-home',
    'proposer': CornersHandicapsHomeProposer()
}, {
    'name': 'corners_handicaps-away',
    'proposer': CornersHandicapsAwayProposer()
}]
corners_first_period_handicaps_proposers_data = [{
    'name': 'corners_first_period_handicaps-home',
    'proposer': CornersFirstPeriodHandicapsHomeProposer()
}, {
    'name': 'corners_first_period_handicaps-away',
    'proposer': CornersFirstPeriodHandicapsAwayProposer()
}]
corners_second_period_handicaps_proposers_data = [{
    'name': 'corners_second_period_handicaps-home',
    'proposer': CornersSecondPeriodHandicapsHomeProposer()
}, {
    'name': 'corners_second_period_handicaps-away',
    'proposer': CornersSecondPeriodHandicapsAwayProposer()
}]
corners_first_period_totals_proposers_data = [{
    'name': 'corners_first_period_totals-greater',
    'proposer': CornersFirstPeriodTotalsGreaterProposer()
}, {
    'name': 'corners_first_period_totals-lesser',
    'proposer': CornersFirstPeriodTotalsLesserProposer()
}]
corners_second_period_totals_proposers_data = [{
    'name': 'corners_second_period_totals-greater',
    'proposer': CornersSecondPeriodTotalsGreaterProposer()
}, {
    'name': 'corners_second_period_totals-lesser',
    'proposer': CornersSecondPeriodTotalsLesserProposer()
}]
corners_individual_totals_proposers_data = [{
    'name': 'corners_individual_totals-home-greater',
    'proposer': CornersIndividualTotalsHomeGreaterProposer()
}, {
    'name': 'corners_individual_totals-home-lesser',
    'proposer': CornersIndividualTotalsHomeLesserProposer()
}, {
    'name': 'corners_individual_totals-away-greater',
    'proposer': CornersIndividualTotalsAwayGreaterProposer()
}, {
    'name': 'corners_individual_totals-away-lesser',
    'proposer': CornersIndividualTotalsAwayLesserProposer()
}]
corners_first_period_individual_totals_proposers_data = [{
    'name': 'corners_first_period_individual_totals-home-greater',
    'proposer': CornersFirstPeriodIndividualTotalsHomeGreaterProposer()
}, {
    'name': 'corners_first_period_individual_totals-home-lesser',
    'proposer': CornersFirstPeriodIndividualTotalsHomeLesserProposer()
}, {
    'name': 'corners_first_period_individual_totals-away-greater',
    'proposer': CornersFirstPeriodIndividualTotalsAwayGreaterProposer()
}, {
    'name': 'corners_first_period_individual_totals-away-lesser',
    'proposer': CornersFirstPeriodIndividualTotalsAwayLesserProposer()
}]
corners_second_period_individual_totals_proposers_data = [{
    'name': 'corners_second_period_individual_totals-home-greater',
    'proposer': CornersSecondPeriodIndividualTotalsHomeGreaterProposer()
}, {
    'name': 'corners_second_period_individual_totals-home-lesser',
    'proposer': CornersSecondPeriodIndividualTotalsHomeLesserProposer()
}, {
    'name': 'corners_second_period_individual_totals-away-greater',
    'proposer': CornersSecondPeriodIndividualTotalsAwayGreaterProposer()
}, {
    'name': 'corners_second_period_individual_totals-away-lesser',
    'proposer': CornersSecondPeriodIndividualTotalsAwayLesserProposer()
}]

thresholds_data = {
    'provider-corners_results-corners_attack_defense-eve': {
        'corners_results-1': 1.9,
        'corners_results-1X': None,
        'corners_results-X2': 1.7,
        'corners_results-2': 2.4
    },
    'provider-corners_totals-corners_attack_defense-eve': {
        'corners_totals-greater': None,
        'corners_totals-lesser': 1.9
    },
    'provider-corners_first_period_results-corners_first_period_attack_defense-eve': {
        'corners_period_results-first_period-1': None,
        'corners_period_results-first_period-1X': None,
        'corners_period_results-first_period-X2': 1.7,
        'corners_period_results-first_period-2': 1.7
    },
    'provider-corners_second_period_results-corners_second_period_attack_defense-eve': {
        'corners_period_results-second_period-1': None,
        'corners_period_results-second_period-1X': None,
        'corners_period_results-second_period-X2': None,
        'corners_period_results-second_period-2': 3.0
    },
    'provider-corners_handicaps-corners_attack_defense-eve': {
        'corners_handicaps-home': 1.7,
        'corners_handicaps-away': 1.7,
    },
    'provider-corners_first_period_handicaps-corners_first_period_attack_defense-eve': {
        'corners_first_period_handicaps-home': 1.7,
        'corners_first_period_handicaps-away': 1.7,
    },
    'provider-corners_second_period_handicaps-corners_second_period_attack_defense-eve': {
        'corners_second_period_handicaps-home': 1.7,
        'corners_second_period_handicaps-away': 1.7,
    },
    'provider-corners_first_period_totals-corners_first_period_attack_defense-eve': {
        'corners_first_period_totals-greater': None,
        'corners_first_period_totals-lesser': None,
    },
    'provider-corners_second_period_totals-corners_second_period_attack_defense-eve': {
        'corners_second_period_totals-greater': None,
        'corners_second_period_totals-lesser': None,
    },
    'provider-corners_individual_totals-corners_attack_defense-eve': {
        'corners_individual_totals-home-greater': 1.0,
        'corners_individual_totals-home-lesser': 1.0,
        'corners_individual_totals-away-greater': 1.0,
        'corners_individual_totals-away-lesser': 1.0
    },
    'provider-corners_first_period_individual_totals-corners_attack_defense-eve': {
        'corners_first_period_individual_totals-home-greater': 1.0,
        'corners_first_period_individual_totals-home-lesser': 1.0,
        'corners_first_period_individual_totals-away-greater': 1.0,
        'corners_first_period_individual_totals-away-lesser': 1.0
    },
    'provider-corners_second_period_individual_totals-corners_attack_defense-eve': {
        'corners_second_period_individual_totals-home-greater': 1.0,
        'corners_second_period_individual_totals-home-lesser': 1.0,
        'corners_second_period_individual_totals-away-greater': 1.0,
        'corners_second_period_individual_totals-away-lesser': 1.0
    }
}


for train_sampler_name, train_sampler in train_samplers.items():
    print('Pre-training...')
    corners_attack_defense_fitter_fitted_data = corners_attack_defense_fitter.fit(train_sampler)
    corners_first_period_attack_defense_fitter_fitted_data = corners_first_period_attack_defense_fitter.fit(train_sampler)
    corners_second_period_attack_defense_fitter_fitted_data = corners_second_period_attack_defense_fitter.fit(train_sampler)
    print()

    name = 'provider-corners_results-corners_attack_defense-%s' % (train_sampler_name,)
    description = 'Исходы угловых, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов)'
    provider1 = Provider(name, description, fitted_datas=corners_attack_defense_fitter_fitted_data, predictor=corners_result_probabilities_attack_defense_predictor, proposers_data=corners_results_proposers_data)
    set_thresholds(provider1, thresholds_data)
    make_experiment(provider1, db_name, matches_collection_name, sample_condition)

    name = 'provider-corners_totals-corners_attack_defense-%s' % (train_sampler_name,)
    description = 'Тоталы угловых, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов)'
    provider2 = Provider(name, description, fitted_datas=corners_attack_defense_fitter_fitted_data, predictor=corners_result_probabilities_attack_defense_predictor, proposers_data=corners_totals_proposers_data)
    set_thresholds(provider2, thresholds_data)
    make_experiment(provider2, db_name, matches_collection_name, sample_condition)

    name = 'provider-corners_first_period_results-corners_first_period_attack_defense-%s' % (train_sampler_name,)
    description = 'Исходы угловых 1-го тайма, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов)'
    provider3 = Provider(name, description, fitted_datas=corners_first_period_attack_defense_fitter_fitted_data, predictor=corners_result_probabilities_attack_defense_predictor, proposers_data=corners_first_period_results_proposers_data)
    set_thresholds(provider3, thresholds_data)
    make_experiment(provider3, db_name, matches_collection_name, sample_condition)

    name = 'provider-corners_second_period_results-corners_second_period_attack_defense-%s' % (train_sampler_name,)
    description = 'Исходы угловых 2-го тайма, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов)'
    provider4 = Provider(name, description, fitted_datas=corners_second_period_attack_defense_fitter_fitted_data, predictor=corners_result_probabilities_attack_defense_predictor, proposers_data=corners_second_period_results_proposers_data)
    set_thresholds(provider4, thresholds_data)
    make_experiment(provider4, db_name, matches_collection_name, sample_condition)
    name = 'provider-corners_handicaps-corners_attack_defense-%s' % (train_sampler_name,)

    name = 'provider-corners_handicaps-corners_attack_defense-%s' % (train_sampler_name,)
    description = 'Форы угловых, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов)'
    provider5 = Provider(name, description, fitted_datas=corners_attack_defense_fitter_fitted_data, predictor=corners_result_probabilities_attack_defense_predictor, proposers_data=corners_handicaps_proposers_data)
    set_thresholds(provider5, thresholds_data)
    make_experiment(provider5, db_name, matches_collection_name, sample_condition)

    name = 'provider-corners_first_period_handicaps-corners_first_period_attack_defense-%s' % (train_sampler_name,)
    description = 'Форы угловых 1-го тайма, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов)'
    provider6 = Provider(name, description, fitted_datas=corners_first_period_attack_defense_fitter_fitted_data, predictor=corners_result_probabilities_attack_defense_predictor, proposers_data=corners_first_period_handicaps_proposers_data)
    set_thresholds(provider6, thresholds_data)
    make_experiment(provider6, db_name, matches_collection_name, sample_condition)

    name = 'provider-corners_second_period_handicaps-corners_second_period_attack_defense-%s' % (train_sampler_name,)
    description = 'Форы угловых 2-го тайма, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов)'
    provider7 = Provider(name, description, fitted_datas=corners_second_period_attack_defense_fitter_fitted_data, predictor=corners_result_probabilities_attack_defense_predictor, proposers_data=corners_second_period_handicaps_proposers_data)
    set_thresholds(provider7, thresholds_data)
    make_experiment(provider7, db_name, matches_collection_name, sample_condition)

    name = 'provider-corners_first_period_totals-corners_first_period_attack_defense-%s' % (train_sampler_name,)
    description = 'Тоталы угловых 1-го тайма, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов)'
    provider8 = Provider(name, description, fitted_datas=corners_first_period_attack_defense_fitter_fitted_data, predictor=corners_result_probabilities_attack_defense_predictor, proposers_data=corners_first_period_totals_proposers_data)
    set_thresholds(provider8, thresholds_data)
    make_experiment(provider8, db_name, matches_collection_name, sample_condition)

    name = 'provider-corners_second_period_totals-corners_second_period_attack_defense-%s' % (train_sampler_name,)
    description = 'Тоталы угловых 2-го тайма, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов)'
    provider9 = Provider(name, description, fitted_datas=corners_second_period_attack_defense_fitter_fitted_data, predictor=corners_result_probabilities_attack_defense_predictor, proposers_data=corners_second_period_totals_proposers_data)
    set_thresholds(provider9, thresholds_data)
    make_experiment(provider9, db_name, matches_collection_name, sample_condition)

    name = 'provider-corners_individual_totals-corners_attack_defense-%s' % (train_sampler_name,)
    description = 'Индивидуальные тоталы угловых, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов)'
    provider10 = Provider(name, description, fitted_datas=corners_attack_defense_fitter_fitted_data, predictor=corners_result_probabilities_attack_defense_predictor, proposers_data=corners_individual_totals_proposers_data)
    set_thresholds(provider10, thresholds_data)
    make_experiment(provider10, db_name, matches_collection_name, sample_condition)

    name = 'provider-corners_first_period_individual_totals-corners_attack_defense-%s' % (train_sampler_name,)
    description = 'Индивидуальные тоталы угловых 1-го тайма, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов)'
    provider11 = Provider(name, description, fitted_datas=corners_first_period_attack_defense_fitter_fitted_data, predictor=corners_result_probabilities_attack_defense_predictor, proposers_data=corners_first_period_individual_totals_proposers_data)
    set_thresholds(provider11, thresholds_data)
    make_experiment(provider11, db_name, matches_collection_name, sample_condition)

    name = 'provider-corners_second_period_individual_totals-corners_attack_defense-%s' % (train_sampler_name,)
    description = 'Индивидуальные тоталы угловых 2-го тайма, предсказание по атаке и обороне команд (угловые, рассматривается вероятность счетов)'
    provider12 = Provider(name, description, fitted_datas=corners_second_period_attack_defense_fitter_fitted_data, predictor=corners_result_probabilities_attack_defense_predictor, proposers_data=corners_second_period_individual_totals_proposers_data)
    set_thresholds(provider12, thresholds_data)
    make_experiment(provider12, db_name, matches_collection_name, sample_condition)
