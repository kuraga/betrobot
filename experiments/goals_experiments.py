from experiments.standard_experiments_collection import StandardExperimentsCollection

from betrobot.betting.samplers.date_based_samplers import HistoricalSampler, EveSampler

from betrobot.betting.fitters.goals_attack_defense_fitters import GoalsAttackDefenseFitter, GoalsFirstPeriodAttackDefenseFitter, GoalsSecondPeriodAttackDefenseFitter
from betrobot.betting.predictors.goals_attack_defense_predictors import GoalsResultProbabilitiesAttackDefensePredictor

from betrobot.betting.proposers.goals_results_proposers import GoalsResults1Proposer, GoalsResults1XProposer, GoalsResultsX2Proposer, GoalsResults2Proposer
from betrobot.betting.proposers.goals_period_results_proposers import GoalsFirstPeriodResults1Proposer, GoalsFirstPeriodResults1XProposer, GoalsFirstPeriodResultsX2Proposer, GoalsFirstPeriodResults2Proposer, GoalsSecondPeriodResults1Proposer, GoalsSecondPeriodResults1XProposer, GoalsSecondPeriodResultsX2Proposer, GoalsSecondPeriodResults2Proposer
from betrobot.betting.proposers.goals_handicaps_proposers import GoalsHandicapsHomeProposer, GoalsHandicapsAwayProposer
from betrobot.betting.proposers.goals_period_handicaps_proposers import GoalsFirstPeriodHandicapsHomeProposer, GoalsFirstPeriodHandicapsAwayProposer, GoalsSecondPeriodHandicapsHomeProposer, GoalsSecondPeriodHandicapsAwayProposer
from betrobot.betting.proposers.goals_totals_proposers import GoalsTotalsGreaterProposer, GoalsTotalsLesserProposer
from betrobot.betting.proposers.goals_period_totals_proposers import GoalsFirstPeriodTotalsGreaterProposer, GoalsFirstPeriodTotalsLesserProposer, GoalsSecondPeriodTotalsGreaterProposer, GoalsSecondPeriodTotalsLesserProposer
from betrobot.betting.proposers.goals_individual_totals_proposers import GoalsIndividualTotalsHomeGreaterProposer, GoalsIndividualTotalsHomeLesserProposer, GoalsIndividualTotalsAwayGreaterProposer, GoalsIndividualTotalsAwayLesserProposer
from betrobot.betting.proposers.goals_period_individual_totals_proposers import GoalsFirstPeriodIndividualTotalsHomeGreaterProposer, GoalsFirstPeriodIndividualTotalsHomeLesserProposer, GoalsFirstPeriodIndividualTotalsAwayGreaterProposer, GoalsFirstPeriodIndividualTotalsAwayLesserProposer, GoalsSecondPeriodIndividualTotalsHomeGreaterProposer, GoalsSecondPeriodIndividualTotalsHomeLesserProposer, GoalsSecondPeriodIndividualTotalsAwayGreaterProposer, GoalsSecondPeriodIndividualTotalsAwayLesserProposer


db_name = 'betrobot'
matches_collection_name = 'matchesCleaned'
sample_condition = {
   'date': { '$regex': '^2017-02|^2017-03' }
}


goals_attack_defense_fitter = GoalsAttackDefenseFitter()
goals_first_period_attack_defense_fitter = GoalsFirstPeriodAttackDefenseFitter()
goals_second_period_attack_defense_fitter = GoalsSecondPeriodAttackDefenseFitter()


goals_result_probabilities_attack_defense_predictor = GoalsResultProbabilitiesAttackDefensePredictor()


goals_results_proposers_data = [{
    'name': 'goals_results-1',
    'proposer_class': GoalsResults1Proposer
}, {
    'name': 'goals_results-1X',
    'proposer_class': GoalsResults1XProposer
}, {
    'name': 'goals_results-X2',
    'proposer_class': GoalsResultsX2Proposer
}, {
    'name': 'goals_results-2',
    'proposer_class': GoalsResults2Proposer
}]
goals_first_period_results_proposers_data = [{
    'name': 'goals_period_results-first_period-1',
    'proposer_class': GoalsFirstPeriodResults1Proposer
}, {
    'name': 'goals_period_results-first_period-1X',
    'proposer_class': GoalsFirstPeriodResults1XProposer
}, {
    'name': 'goals_period_results-first_period-X2',
    'proposer_class': GoalsFirstPeriodResultsX2Proposer
}, {
    'name': 'goals_period_results-first_period-2',
    'proposer_class': GoalsFirstPeriodResults2Proposer
}]
goals_second_period_results_proposers_data = [{
    'name': 'goals_period_results-second_period-1',
    'proposer_class': GoalsSecondPeriodResults1Proposer
}, {
    'name': 'goals_period_results-second_period-1X',
    'proposer_class': GoalsSecondPeriodResults1XProposer
}, {
    'name': 'goals_period_results-second_period-X2',
    'proposer_class': GoalsSecondPeriodResultsX2Proposer
}, {
    'name': 'goals_period_results-second_period-2',
    'proposer_class': GoalsSecondPeriodResults2Proposer
}]
goals_handicaps_proposers_data = [{
    'name': 'goals_handicaps-home',
    'proposer_class': GoalsHandicapsHomeProposer
}, {
    'name': 'goals_handicaps-away',
    'proposer_class': GoalsHandicapsAwayProposer
}]
goals_first_period_handicaps_proposers_data = [{
    'name': 'goals_first_period_handicaps-home',
    'proposer_class': GoalsFirstPeriodHandicapsHomeProposer
}, {
    'name': 'goals_first_period_handicaps-away',
    'proposer_class': GoalsFirstPeriodHandicapsAwayProposer
}]
goals_second_period_handicaps_proposers_data = [{
    'name': 'goals_second_period_handicaps-home',
    'proposer_class': GoalsSecondPeriodHandicapsHomeProposer
}, {
    'name': 'goals_second_period_handicaps-away',
    'proposer_class': GoalsSecondPeriodHandicapsAwayProposer
}]
goals_totals_proposers_data = [{
    'name': 'goals_totals-greater',
    'proposer_class': GoalsTotalsGreaterProposer
}, {
    'name': 'goals_totals-lesser',
    'proposer_class': GoalsTotalsLesserProposer
}]
goals_first_period_totals_proposers_data = [{
    'name': 'goals_first_period_totals-greater',
    'proposer_class': GoalsFirstPeriodTotalsGreaterProposer
}, {
    'name': 'goals_first_period_totals-lesser',
    'proposer_class': GoalsFirstPeriodTotalsLesserProposer
}]
goals_second_period_totals_proposers_data = [{
    'name': 'goals_second_period_totals-greater',
    'proposer_class': GoalsSecondPeriodTotalsGreaterProposer
}, {
    'name': 'goals_second_period_totals-lesser',
    'proposer_class': GoalsSecondPeriodTotalsLesserProposer
}]
goals_individual_totals_proposers_data = [{
    'name': 'goals_individual_totals-home-greater',
    'proposer_class': GoalsIndividualTotalsHomeGreaterProposer
}, {
    'name': 'goals_individual_totals-home-lesser',
    'proposer_class': GoalsIndividualTotalsHomeLesserProposer
}, {
    'name': 'goals_individual_totals-away-greater',
    'proposer_class': GoalsIndividualTotalsAwayGreaterProposer
}, {
    'name': 'goals_individual_totals-away-lesser',
    'proposer_class': GoalsIndividualTotalsAwayLesserProposer
}]
goals_first_period_individual_totals_proposers_data = [{
    'name': 'goals_first_period_individual_totals-home-greater',
    'proposer_class': GoalsFirstPeriodIndividualTotalsHomeGreaterProposer
}, {
    'name': 'goals_first_period_individual_totals-home-lesser',
    'proposer_class': GoalsFirstPeriodIndividualTotalsHomeLesserProposer
}, {
    'name': 'goals_first_period_individual_totals-away-greater',
    'proposer_class': GoalsFirstPeriodIndividualTotalsAwayGreaterProposer
}, {
    'name': 'goals_first_period_individual_totals-away-lesser',
    'proposer_class': GoalsFirstPeriodIndividualTotalsAwayLesserProposer
}]
goals_second_period_individual_totals_proposers_data = [{
    'name': 'goals_second_period_individual_totals-home-greater',
    'proposer_class': GoalsSecondPeriodIndividualTotalsHomeGreaterProposer
}, {
    'name': 'goals_second_period_individual_totals-home-lesser',
    'proposer_class': GoalsSecondPeriodIndividualTotalsHomeLesserProposer
}, {
    'name': 'goals_second_period_individual_totals-away-greater',
    'proposer_class': GoalsSecondPeriodIndividualTotalsAwayGreaterProposer
}, {
    'name': 'goals_second_period_individual_totals-away-lesser',
    'proposer_class': GoalsSecondPeriodIndividualTotalsAwayLesserProposer
}]


value_thresholds_data = 1.7


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
    goals_attack_defense_fitter_fitted_data = goals_attack_defense_fitter.fit(train_sampler)
    goals_first_period_attack_defense_fitter_fitted_data = goals_first_period_attack_defense_fitter.fit(train_sampler)
    goals_second_period_attack_defense_fitter_fitted_data = goals_second_period_attack_defense_fitter.fit(train_sampler)
    print()

    providers_data = [{
        'name': 'goals_results-goals_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Исходы голов, предсказание по атаке и обороне команд (используются голы, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': goals_attack_defense_fitter_fitted_data,
        'predictor': goals_result_probabilities_attack_defense_predictor,
        'proposers_data': goals_results_proposers_data
    }, {
        'name': 'goals_first_period_results-goals_first_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Исходы голов 1-го тайма, предсказание по атаке и обороне команд (используются голы, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': goals_first_period_attack_defense_fitter_fitted_data,
        'predictor': goals_result_probabilities_attack_defense_predictor,
        'proposers_data': goals_first_period_results_proposers_data
    }, {
        'name': 'goals_second_period_results-goals_second_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Исходы голов 2-го тайма, предсказание по атаке и обороне команд (используются голы, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': goals_second_period_attack_defense_fitter_fitted_data,
        'predictor': goals_result_probabilities_attack_defense_predictor,
        'proposers_data': goals_second_period_results_proposers_data
    }, {
        'name': 'goals_handicaps-goals_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Форы голов, предсказание по атаке и обороне команд (используются голы, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': goals_attack_defense_fitter_fitted_data,
        'predictor': goals_result_probabilities_attack_defense_predictor,
        'proposers_data': goals_handicaps_proposers_data
    }, {
        'name': 'goals_first_period_handicaps-goals_first_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Форы голов 1-го тайма, предсказание по атаке и обороне команд (используются голы, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': goals_first_period_attack_defense_fitter_fitted_data,
        'predictor': goals_result_probabilities_attack_defense_predictor,
        'proposers_data': goals_first_period_handicaps_proposers_data
    }, {
        'name': 'goals_second_period_handicaps-goals_second_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Форы голов 2-го тайма, предсказание по атаке и обороне команд (используются голы, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': goals_second_period_attack_defense_fitter_fitted_data,
        'predictor': goals_result_probabilities_attack_defense_predictor,
        'proposers_data': goals_second_period_handicaps_proposers_data
    }, {
        'name': 'goals_totals-goals_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Тоталы голов, предсказание по атаке и обороне команд (используются голы, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': goals_attack_defense_fitter_fitted_data,
        'predictor': goals_result_probabilities_attack_defense_predictor,
        'proposers_data': goals_totals_proposers_data
    }, {
        'name': 'goals_first_period_totals-goals_first_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Тоталы голов 1-го тайма, предсказание по атаке и обороне команд (используются голы, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': goals_first_period_attack_defense_fitter_fitted_data,
        'predictor': goals_result_probabilities_attack_defense_predictor,
        'proposers_data': goals_first_period_totals_proposers_data
    }, {
        'name': 'goals_second_period_totals-goals_second_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Тоталы голов 2-го тайма, предсказание по атаке и обороне команд (используются голы, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': goals_second_period_attack_defense_fitter_fitted_data,
        'predictor': goals_result_probabilities_attack_defense_predictor,
        'proposers_data': goals_second_period_totals_proposers_data
    }, {
        'name': 'goals_individual_totals-goals_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Индивидуальные тоталы голов, предсказание по атаке и обороне команд (используются голы, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': goals_attack_defense_fitter_fitted_data,
        'predictor': goals_result_probabilities_attack_defense_predictor,
        'proposers_data': goals_individual_totals_proposers_data
    }, {
        'name': 'goals_first_period_individual_totals-goals_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Индивидуальные тоталы голов 1-го тайма, предсказание по атаке и обороне команд (используются голы, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': goals_first_period_attack_defense_fitter_fitted_data,
        'predictor': goals_result_probabilities_attack_defense_predictor,
        'proposers_data': goals_first_period_individual_totals_proposers_data
    }, {
        'name': 'goals_second_period_individual_totals-goals_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Индивидуальные тоталы голов 2-го тайма, предсказание по атаке и обороне команд (используются голы, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': goals_second_period_attack_defense_fitter_fitted_data,
        'predictor': goals_result_probabilities_attack_defense_predictor,
        'proposers_data': goals_second_period_individual_totals_proposers_data
    }]

    experiments = StandardExperimentsCollection(providers_data, db_name=db_name, matches_collection_name=matches_collection_name, sample_condition=sample_condition, value_thresholds_data=value_thresholds_data)
    experiments.make()
