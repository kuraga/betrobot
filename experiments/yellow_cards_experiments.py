from experiments.standard_experiments_collection import StandardExperimentsCollection

from betrobot.betting.samplers.date_based_samplers import HistoricalSampler, EveSampler

from betrobot.betting.fitters.yellow_cards_attack_defense_fitters import YellowCardsAttackDefenseFitter, YellowCardsFirstPeriodAttackDefenseFitter, YellowCardsSecondPeriodAttackDefenseFitter
from betrobot.betting.predictors.yellow_cards_attack_defense_predictors import YellowCardsResultProbabilitiesAttackDefensePredictor

from betrobot.betting.proposers.yellow_cards_results_proposers import YellowCardsResults1Proposer, YellowCardsResults1XProposer, YellowCardsResultsX2Proposer, YellowCardsResults2Proposer
from betrobot.betting.proposers.yellow_cards_period_results_proposers import YellowCardsFirstPeriodResults1Proposer, YellowCardsFirstPeriodResults1XProposer, YellowCardsFirstPeriodResultsX2Proposer, YellowCardsFirstPeriodResults2Proposer, YellowCardsSecondPeriodResults1Proposer, YellowCardsSecondPeriodResults1XProposer, YellowCardsSecondPeriodResultsX2Proposer, YellowCardsSecondPeriodResults2Proposer
from betrobot.betting.proposers.yellow_cards_handicaps_proposers import YellowCardsHandicapsHomeProposer, YellowCardsHandicapsAwayProposer
from betrobot.betting.proposers.yellow_cards_period_handicaps_proposers import YellowCardsFirstPeriodHandicapsHomeProposer, YellowCardsFirstPeriodHandicapsAwayProposer, YellowCardsSecondPeriodHandicapsHomeProposer, YellowCardsSecondPeriodHandicapsAwayProposer
from betrobot.betting.proposers.yellow_cards_totals_proposers import YellowCardsTotalsGreaterProposer, YellowCardsTotalsLesserProposer
from betrobot.betting.proposers.yellow_cards_period_totals_proposers import YellowCardsFirstPeriodTotalsGreaterProposer, YellowCardsFirstPeriodTotalsLesserProposer, YellowCardsSecondPeriodTotalsGreaterProposer, YellowCardsSecondPeriodTotalsLesserProposer
from betrobot.betting.proposers.yellow_cards_individual_totals_proposers import YellowCardsIndividualTotalsHomeGreaterProposer, YellowCardsIndividualTotalsHomeLesserProposer, YellowCardsIndividualTotalsAwayGreaterProposer, YellowCardsIndividualTotalsAwayLesserProposer
from betrobot.betting.proposers.yellow_cards_period_individual_totals_proposers import YellowCardsFirstPeriodIndividualTotalsHomeGreaterProposer, YellowCardsFirstPeriodIndividualTotalsHomeLesserProposer, YellowCardsFirstPeriodIndividualTotalsAwayGreaterProposer, YellowCardsFirstPeriodIndividualTotalsAwayLesserProposer, YellowCardsSecondPeriodIndividualTotalsHomeGreaterProposer, YellowCardsSecondPeriodIndividualTotalsHomeLesserProposer, YellowCardsSecondPeriodIndividualTotalsAwayGreaterProposer, YellowCardsSecondPeriodIndividualTotalsAwayLesserProposer


db_name = 'betrobot'
matches_collection_name = 'matchesCleaned'
sample_condition = {
   'date': { '$regex': '^2017-02|^2017-03' }
}


yellow_cards_attack_defense_fitter = YellowCardsAttackDefenseFitter()
yellow_cards_first_period_attack_defense_fitter = YellowCardsFirstPeriodAttackDefenseFitter()
yellow_cards_second_period_attack_defense_fitter = YellowCardsSecondPeriodAttackDefenseFitter()


yellow_cards_result_probabilities_attack_defense_predictor = YellowCardsResultProbabilitiesAttackDefensePredictor()


yellow_cards_results_proposers_data = [{
    'name': 'yellow_cards_results-1',
    'proposer_class': YellowCardsResults1Proposer
}, {
    'name': 'yellow_cards_results-1X',
    'proposer_class': YellowCardsResults1XProposer
}, {
    'name': 'yellow_cards_results-X2',
    'proposer_class': YellowCardsResultsX2Proposer
}, {
    'name': 'yellow_cards_results-2',
    'proposer_class': YellowCardsResults2Proposer
}]
yellow_cards_first_period_results_proposers_data = [{
    'name': 'yellow_cards_period_results-first_period-1',
    'proposer_class': YellowCardsFirstPeriodResults1Proposer
}, {
    'name': 'yellow_cards_period_results-first_period-1X',
    'proposer_class': YellowCardsFirstPeriodResults1XProposer
}, {
    'name': 'yellow_cards_period_results-first_period-X2',
    'proposer_class': YellowCardsFirstPeriodResultsX2Proposer
}, {
    'name': 'yellow_cards_period_results-first_period-2',
    'proposer_class': YellowCardsFirstPeriodResults2Proposer
}]
yellow_cards_second_period_results_proposers_data = [{
    'name': 'yellow_cards_period_results-second_period-1',
    'proposer_class': YellowCardsSecondPeriodResults1Proposer
}, {
    'name': 'yellow_cards_period_results-second_period-1X',
    'proposer_class': YellowCardsSecondPeriodResults1XProposer
}, {
    'name': 'yellow_cards_period_results-second_period-X2',
    'proposer_class': YellowCardsSecondPeriodResultsX2Proposer
}, {
    'name': 'yellow_cards_period_results-second_period-2',
    'proposer_class': YellowCardsSecondPeriodResults2Proposer
}]
yellow_cards_handicaps_proposers_data = [{
    'name': 'yellow_cards_handicaps-home',
    'proposer_class': YellowCardsHandicapsHomeProposer
}, {
    'name': 'yellow_cards_handicaps-away',
    'proposer_class': YellowCardsHandicapsAwayProposer
}]
yellow_cards_first_period_handicaps_proposers_data = [{
    'name': 'yellow_cards_first_period_handicaps-home',
    'proposer_class': YellowCardsFirstPeriodHandicapsHomeProposer
}, {
    'name': 'yellow_cards_first_period_handicaps-away',
    'proposer_class': YellowCardsFirstPeriodHandicapsAwayProposer
}]
yellow_cards_second_period_handicaps_proposers_data = [{
    'name': 'yellow_cards_second_period_handicaps-home',
    'proposer_class': YellowCardsSecondPeriodHandicapsHomeProposer
}, {
    'name': 'yellow_cards_second_period_handicaps-away',
    'proposer_class': YellowCardsSecondPeriodHandicapsAwayProposer
}]
yellow_cards_totals_proposers_data = [{
    'name': 'yellow_cards_totals-greater',
    'proposer_class': YellowCardsTotalsGreaterProposer
}, {
    'name': 'yellow_cards_totals-lesser',
    'proposer_class': YellowCardsTotalsLesserProposer
}]
yellow_cards_first_period_totals_proposers_data = [{
    'name': 'yellow_cards_first_period_totals-greater',
    'proposer_class': YellowCardsFirstPeriodTotalsGreaterProposer
}, {
    'name': 'yellow_cards_first_period_totals-lesser',
    'proposer_class': YellowCardsFirstPeriodTotalsLesserProposer
}]
yellow_cards_second_period_totals_proposers_data = [{
    'name': 'yellow_cards_second_period_totals-greater',
    'proposer_class': YellowCardsSecondPeriodTotalsGreaterProposer
}, {
    'name': 'yellow_cards_second_period_totals-lesser',
    'proposer_class': YellowCardsSecondPeriodTotalsLesserProposer
}]
yellow_cards_individual_totals_proposers_data = [{
    'name': 'yellow_cards_individual_totals-home-greater',
    'proposer_class': YellowCardsIndividualTotalsHomeGreaterProposer
}, {
    'name': 'yellow_cards_individual_totals-home-lesser',
    'proposer_class': YellowCardsIndividualTotalsHomeLesserProposer
}, {
    'name': 'yellow_cards_individual_totals-away-greater',
    'proposer_class': YellowCardsIndividualTotalsAwayGreaterProposer
}, {
    'name': 'yellow_cards_individual_totals-away-lesser',
    'proposer_class': YellowCardsIndividualTotalsAwayLesserProposer
}]
yellow_cards_first_period_individual_totals_proposers_data = [{
    'name': 'yellow_cards_first_period_individual_totals-home-greater',
    'proposer_class': YellowCardsFirstPeriodIndividualTotalsHomeGreaterProposer
}, {
    'name': 'yellow_cards_first_period_individual_totals-home-lesser',
    'proposer_class': YellowCardsFirstPeriodIndividualTotalsHomeLesserProposer
}, {
    'name': 'yellow_cards_first_period_individual_totals-away-greater',
    'proposer_class': YellowCardsFirstPeriodIndividualTotalsAwayGreaterProposer
}, {
    'name': 'yellow_cards_first_period_individual_totals-away-lesser',
    'proposer_class': YellowCardsFirstPeriodIndividualTotalsAwayLesserProposer
}]
yellow_cards_second_period_individual_totals_proposers_data = [{
    'name': 'yellow_cards_second_period_individual_totals-home-greater',
    'proposer_class': YellowCardsSecondPeriodIndividualTotalsHomeGreaterProposer
}, {
    'name': 'yellow_cards_second_period_individual_totals-home-lesser',
    'proposer_class': YellowCardsSecondPeriodIndividualTotalsHomeLesserProposer
}, {
    'name': 'yellow_cards_second_period_individual_totals-away-greater',
    'proposer_class': YellowCardsSecondPeriodIndividualTotalsAwayGreaterProposer
}, {
    'name': 'yellow_cards_second_period_individual_totals-away-lesser',
    'proposer_class': YellowCardsSecondPeriodIndividualTotalsAwayLesserProposer
}]


thresholds_data = 1.7


train_samplers_data = [{
    'name': 'historical',
    'description': 'Тренировка на исторических данных',
    'sampler': HistoricalSampler(db_name, matches_collection_name),
    'use': False
}, {
    'name': 'eve',
    'description': 'Тренировка на последних 3-х месяцах',
    'sampler': HistoricalSampler(db_name, matches_collection_name),
    'use': True
}]


for train_sampler_data in train_samplers_data:
    if not train_sampler_data['use']:
        continue

    print('Pre-training...')
    train_sampler = train_sampler_data['sampler']
    yellow_cards_attack_defense_fitter_fitted_data = yellow_cards_attack_defense_fitter.fit(train_sampler)
    yellow_cards_first_period_attack_defense_fitter_fitted_data = yellow_cards_first_period_attack_defense_fitter.fit(train_sampler)
    yellow_cards_second_period_attack_defense_fitter_fitted_data = yellow_cards_second_period_attack_defense_fitter.fit(train_sampler)
    print()

    providers_data = [{
        'name': 'yellow_cards_results-yellow_cards_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Исходы желтых карточек, предсказание по атаке и обороне команд (используются желтые карточки, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': yellow_cards_attack_defense_fitter_fitted_data,
        'predictor': yellow_cards_result_probabilities_attack_defense_predictor,
        'proposers_data': yellow_cards_results_proposers_data
    }, {
        'name': 'yellow_cards_first_period_results-yellow_cards_first_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Исходы желтых карточек 1-го тайма, предсказание по атаке и обороне команд (используются желтые карточки, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': yellow_cards_first_period_attack_defense_fitter_fitted_data,
        'predictor': yellow_cards_result_probabilities_attack_defense_predictor,
        'proposers_data': yellow_cards_first_period_results_proposers_data
    }, {
        'name': 'yellow_cards_second_period_results-yellow_cards_second_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Исходы желтых карточек 2-го тайма, предсказание по атаке и обороне команд (используются желтые карточки, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': yellow_cards_second_period_attack_defense_fitter_fitted_data,
        'predictor': yellow_cards_result_probabilities_attack_defense_predictor,
        'proposers_data': yellow_cards_second_period_results_proposers_data
    }, {
        'name': 'yellow_cards_handicaps-yellow_cards_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Форы желтых карточек, предсказание по атаке и обороне команд (используются желтые карточки, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': yellow_cards_attack_defense_fitter_fitted_data,
        'predictor': yellow_cards_result_probabilities_attack_defense_predictor,
        'proposers_data': yellow_cards_handicaps_proposers_data
    }, {
        'name': 'yellow_cards_first_period_handicaps-yellow_cards_first_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Форы желтых карточек 1-го тайма, предсказание по атаке и обороне команд (используются желтые карточки, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': yellow_cards_first_period_attack_defense_fitter_fitted_data,
        'predictor': yellow_cards_result_probabilities_attack_defense_predictor,
        'proposers_data': yellow_cards_first_period_handicaps_proposers_data
    }, {
        'name': 'yellow_cards_second_period_handicaps-yellow_cards_second_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Форы желтых карточек 2-го тайма, предсказание по атаке и обороне команд (используются желтые карточки, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': yellow_cards_second_period_attack_defense_fitter_fitted_data,
        'predictor': yellow_cards_result_probabilities_attack_defense_predictor,
        'proposers_data': yellow_cards_second_period_handicaps_proposers_data
    }, {
        'name': 'yellow_cards_totals-yellow_cards_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Тоталы желтых карточек, предсказание по атаке и обороне команд (используются желтые карточки, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': yellow_cards_attack_defense_fitter_fitted_data,
        'predictor': yellow_cards_result_probabilities_attack_defense_predictor,
        'proposers_data': yellow_cards_totals_proposers_data
    }, {
        'name': 'yellow_cards_first_period_totals-yellow_cards_first_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Тоталы желтых карточек 1-го тайма, предсказание по атаке и обороне команд (используются желтые карточки, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': yellow_cards_first_period_attack_defense_fitter_fitted_data,
        'predictor': yellow_cards_result_probabilities_attack_defense_predictor,
        'proposers_data': yellow_cards_first_period_totals_proposers_data
    }, {
        'name': 'yellow_cards_second_period_totals-yellow_cards_second_period_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Тоталы желтых карточек 2-го тайма, предсказание по атаке и обороне команд (используются желтые карточки, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': yellow_cards_second_period_attack_defense_fitter_fitted_data,
        'predictor': yellow_cards_result_probabilities_attack_defense_predictor,
        'proposers_data': yellow_cards_second_period_totals_proposers_data
    }, {
        'name': 'yellow_cards_individual_totals-yellow_cards_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Индивидуальные тоталы желтых карточек, предсказание по атаке и обороне команд (используются желтые карточки, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': yellow_cards_attack_defense_fitter_fitted_data,
        'predictor': yellow_cards_result_probabilities_attack_defense_predictor,
        'proposers_data': yellow_cards_individual_totals_proposers_data
    }, {
        'name': 'yellow_cards_first_period_individual_totals-yellow_cards_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Индивидуальные тоталы желтых карточек 1-го тайма, предсказание по атаке и обороне команд (используются желтые карточки, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': yellow_cards_first_period_attack_defense_fitter_fitted_data,
        'predictor': yellow_cards_result_probabilities_attack_defense_predictor,
        'proposers_data': yellow_cards_first_period_individual_totals_proposers_data
    }, {
        'name': 'yellow_cards_second_period_individual_totals-yellow_cards_attack_defense-%s' % (train_sampler_data['name'],),
        'description': 'Индивидуальные тоталы желтых карточек 2-го тайма, предсказание по атаке и обороне команд (используются желтые карточки, рассматривается вероятность счетов) (%s)' % (train_sampler_data['description'],),
        'fitted_datas': yellow_cards_second_period_attack_defense_fitter_fitted_data,
        'predictor': yellow_cards_result_probabilities_attack_defense_predictor,
        'proposers_data': yellow_cards_second_period_individual_totals_proposers_data
    }]

    experiments = StandardExperimentsCollection(providers_data, db_name=db_name, matches_collection_name=matches_collection_name, sample_condition=sample_condition, thresholds_data=thresholds_data)
    experiments.make()
