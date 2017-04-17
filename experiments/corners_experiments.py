import datetime

from experiments.standard_experiments_collection import StandardExperimentsCollection

from betrobot.betting.samplers.whole_sampler import WholeSampler

from betrobot.betting.fitters.corners_statistic_fitters import CornersStatisticFitter, CornersFirstPeriodStatisticFitter, CornersSecondPeriodStatisticFitter
from betrobot.betting.fitters.attack_defense_fitter import AttackDefenseFitter
from betrobot.betting.fitters.date_filter_statistic_transformer_fitters import MatchPastStatisticTransformerFitter, MatchEveStatisticTransformerFitter

from betrobot.betting.predictors.corners_attack_defense_predictors import CornersResultProbabilitiesAttackDefensePredictor
from betrobot.betting.predictors.refitter_wrapped_predictor import RefitterWrappedPredictor

from betrobot.betting.proposers.corners_proposers import CornersResults1Proposer, CornersResults1XProposer, CornersResultsX2Proposer, CornersResults2Proposer, CornersFirstPeriodResults1Proposer, CornersFirstPeriodResults1XProposer, CornersFirstPeriodResultsX2Proposer, CornersFirstPeriodResults2Proposer, CornersSecondPeriodResults1Proposer, CornersSecondPeriodResults1XProposer, CornersSecondPeriodResultsX2Proposer, CornersSecondPeriodResults2Proposer, CornersHandicapsHomeProposer, CornersHandicapsAwayProposer, CornersFirstPeriodHandicapsHomeProposer, CornersFirstPeriodHandicapsAwayProposer, CornersSecondPeriodHandicapsHomeProposer, CornersSecondPeriodHandicapsAwayProposer, CornersTotalsGreaterProposer, CornersTotalsLesserProposer, CornersFirstPeriodTotalsGreaterProposer, CornersFirstPeriodTotalsLesserProposer, CornersSecondPeriodTotalsGreaterProposer, CornersSecondPeriodTotalsLesserProposer, CornersIndividualTotalsHomeGreaterProposer, CornersIndividualTotalsHomeLesserProposer, CornersIndividualTotalsAwayGreaterProposer, CornersIndividualTotalsAwayLesserProposer, CornersFirstPeriodIndividualTotalsHomeGreaterProposer, CornersFirstPeriodIndividualTotalsHomeLesserProposer, CornersFirstPeriodIndividualTotalsAwayGreaterProposer, CornersFirstPeriodIndividualTotalsAwayLesserProposer, CornersSecondPeriodIndividualTotalsHomeGreaterProposer, CornersSecondPeriodIndividualTotalsHomeLesserProposer, CornersSecondPeriodIndividualTotalsAwayGreaterProposer, CornersSecondPeriodIndividualTotalsAwayLesserProposer


db_name = 'betrobot'
matches_collection_name = 'matchesCleaned'
sample_condition = {
   'date': { '$gte': datetime.datetime.today() - datetime.timedelta(days=120) }
}


print('Training...')

train_sampler = WholeSampler()

corners_statistic_fitter = CornersStatisticFitter()
corners_statistic_fitter.fit(train_sampler=train_sampler)
corners_first_period_statistic_fitter = CornersFirstPeriodStatisticFitter()
corners_first_period_statistic_fitter.fit(train_sampler=train_sampler)
corners_second_period_statistic_fitter = CornersSecondPeriodStatisticFitter()
corners_second_period_statistic_fitter.fit(train_sampler=train_sampler)

print()


corners_results_proposers_data = [{
    'name': 'corners_results-1',
    'proposer_class': CornersResults1Proposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_results-1X',
    'proposer_class': CornersResults1XProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_results-X2',
    'proposer_class': CornersResultsX2Proposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_results-2',
    'proposer_class': CornersResults2Proposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}]
corners_first_period_results_proposers_data = [{
    'name': 'corners_period_results-first_period-1',
    'proposer_class': CornersFirstPeriodResults1Proposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_period_results-first_period-1X',
    'proposer_class': CornersFirstPeriodResults1XProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_period_results-first_period-X2',
    'proposer_class': CornersFirstPeriodResultsX2Proposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_period_results-first_period-2',
    'proposer_class': CornersFirstPeriodResults2Proposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}]
corners_second_period_results_proposers_data = [{
    'name': 'corners_period_results-second_period-1',
    'proposer_class': CornersSecondPeriodResults1Proposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_period_results-second_period-1X',
    'proposer_class': CornersSecondPeriodResults1XProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_period_results-second_period-X2',
    'proposer_class': CornersSecondPeriodResultsX2Proposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_period_results-second_period-2',
    'proposer_class': CornersSecondPeriodResults2Proposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}]
corners_handicaps_proposers_data = [{
    'name': 'corners_handicaps-home',
    'proposer_class': CornersHandicapsHomeProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_handicaps-away',
    'proposer_class': CornersHandicapsAwayProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}]
corners_first_period_handicaps_proposers_data = [{
    'name': 'corners_first_period_handicaps-home',
    'proposer_class': CornersFirstPeriodHandicapsHomeProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_first_period_handicaps-away',
    'proposer_class': CornersFirstPeriodHandicapsAwayProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}]
corners_second_period_handicaps_proposers_data = [{
    'name': 'corners_second_period_handicaps-home',
    'proposer_class': CornersSecondPeriodHandicapsHomeProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_second_period_handicaps-away',
    'proposer_class': CornersSecondPeriodHandicapsAwayProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}]
corners_totals_proposers_data = [{
    'name': 'corners_totals-greater',
    'proposer_class': CornersTotalsGreaterProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_totals-lesser',
    'proposer_class': CornersTotalsLesserProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}]
corners_first_period_totals_proposers_data = [{
    'name': 'corners_first_period_totals-greater',
    'proposer_class': CornersFirstPeriodTotalsGreaterProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_first_period_totals-lesser',
    'proposer_class': CornersFirstPeriodTotalsLesserProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}]
corners_second_period_totals_proposers_data = [{
    'name': 'corners_second_period_totals-greater',
    'proposer_class': CornersSecondPeriodTotalsGreaterProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_second_period_totals-lesser',
    'proposer_class': CornersSecondPeriodTotalsLesserProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}]
corners_individual_totals_proposers_data = [{
    'name': 'corners_individual_totals-home-greater',
    'proposer_class': CornersIndividualTotalsHomeGreaterProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_individual_totals-home-lesser',
    'proposer_class': CornersIndividualTotalsHomeLesserProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_individual_totals-away-greater',
    'proposer_class': CornersIndividualTotalsAwayGreaterProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_individual_totals-away-lesser',
    'proposer_class': CornersIndividualTotalsAwayLesserProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}]
corners_first_period_individual_totals_proposers_data = [{
    'name': 'corners_first_period_individual_totals-home-greater',
    'proposer_class': CornersFirstPeriodIndividualTotalsHomeGreaterProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_first_period_individual_totals-home-lesser',
    'proposer_class': CornersFirstPeriodIndividualTotalsHomeLesserProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_first_period_individual_totals-away-greater',
    'proposer_class': CornersFirstPeriodIndividualTotalsAwayGreaterProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_first_period_individual_totals-away-lesser',
    'proposer_class': CornersFirstPeriodIndividualTotalsAwayLesserProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}]
corners_second_period_individual_totals_proposers_data = [{
    'name': 'corners_second_period_individual_totals-home-greater',
    'proposer_class': CornersSecondPeriodIndividualTotalsHomeGreaterProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_second_period_individual_totals-home-lesser',
    'proposer_class': CornersSecondPeriodIndividualTotalsHomeLesserProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_second_period_individual_totals-away-greater',
    'proposer_class': CornersSecondPeriodIndividualTotalsAwayGreaterProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}, {
    'name': 'corners_second_period_individual_totals-away-lesser',
    'proposer_class': CornersSecondPeriodIndividualTotalsAwayLesserProposer,
    'proposer_kwargs': { 'value_threshold': 1.8, 'predicted_threshold': 1.7, 'ratio_threshold': 1.25 }
}]


date_filter_statistic_transformer_fitters_data = [{
    'name': 'historical',
    'description': 'Исторические (до матча) данные',
    'statistic_transformer_fitter_class': MatchPastStatisticTransformerFitter,
    'use': False
}, {
    'name': 'eve',
    'description': 'Недавние (100 дней до матча) данные',
    'statistic_transformer_fitter_class': MatchEveStatisticTransformerFitter,
    'use': True
}]


import types
from betrobot.util.sport_util import get_whoscored_teams_of_betcity_match, get_tournament_id_of_betcity_match
from betrobot.betting.fitters.tournament_filter_statistic_transformer_fitter import TournamentFilterStatisticTransformerFitter

def magic_fitter(statistic_fitter, date_filter_statistic_transformer_fitter_data):
    def magic__fit(self, betcity_match):
        (home, away) = get_whoscored_teams_of_betcity_match(betcity_match)
        tournament_id = get_tournament_id_of_betcity_match(betcity_match)

        date_filter_statistic_transformer_fitter.fit(statistic_fitter=statistic_fitter, betcity_match=betcity_match)
        tournament_filter_statistic_transformer_fitter.fit(statistic_fitter=date_filter_statistic_transformer_fitter, tournament_id=tournament_id)
        attack_defense_fitter._fit_old(statistic_fitter=tournament_filter_statistic_transformer_fitter, home=home, away=away)

    date_filter_statistic_transformer_fitter = date_filter_statistic_transformer_fitter_data['statistic_transformer_fitter_class']()
    tournament_filter_statistic_transformer_fitter = TournamentFilterStatisticTransformerFitter()
    attack_defense_fitter = AttackDefenseFitter()
    attack_defense_fitter._fit_old = attack_defense_fitter._fit
    attack_defense_fitter._fit = types.MethodType(magic__fit, attack_defense_fitter)

    return attack_defense_fitter


for date_filter_statistic_transformer_fitter_data in date_filter_statistic_transformer_fitters_data:
    if not date_filter_statistic_transformer_fitter_data['use']:
        continue

    providers_data = [{
        'name': 'corners_results-corners_attack_defense-%s' % (date_filter_statistic_transformer_fitter_data['name'],),
        'description': 'Исходы угловых, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (date_filter_statistic_transformer_fitter_data['description'],),
        'predictor': RefitterWrappedPredictor( magic_fitter(corners_statistic_fitter, date_filter_statistic_transformer_fitter_data), predictor_class=CornersResultProbabilitiesAttackDefensePredictor ),
        'proposers_data': corners_results_proposers_data
    }, {
        'name': 'corners_first_period_results-corners_first_period_attack_defense-%s' % (date_filter_statistic_transformer_fitter_data['name'],),
        'description': 'Исходы угловых 1-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (date_filter_statistic_transformer_fitter_data['description'],),
        'predictor': RefitterWrappedPredictor( magic_fitter(corners_first_period_statistic_fitter, date_filter_statistic_transformer_fitter_data), predictor_class=CornersResultProbabilitiesAttackDefensePredictor ),
        'proposers_data': corners_first_period_results_proposers_data
    }, {
        'name': 'corners_second_period_results-corners_second_period_attack_defense-%s' % (date_filter_statistic_transformer_fitter_data['name'],),
        'description': 'Исходы угловых 2-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (date_filter_statistic_transformer_fitter_data['description'],),
        'predictor': RefitterWrappedPredictor( magic_fitter(corners_second_period_statistic_fitter, date_filter_statistic_transformer_fitter_data), predictor_class=CornersResultProbabilitiesAttackDefensePredictor ),
        'proposers_data': corners_second_period_results_proposers_data
    }, {
        'name': 'corners_handicaps-corners_attack_defense-%s' % (date_filter_statistic_transformer_fitter_data['name'],),
        'description': 'Форы угловых, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (date_filter_statistic_transformer_fitter_data['description'],),
        'predictor': RefitterWrappedPredictor( magic_fitter(corners_statistic_fitter, date_filter_statistic_transformer_fitter_data), predictor_class=CornersResultProbabilitiesAttackDefensePredictor ),
        'proposers_data': corners_handicaps_proposers_data
    }, {
        'name': 'corners_first_period_handicaps-corners_first_period_attack_defense-%s' % (date_filter_statistic_transformer_fitter_data['name'],),
        'description': 'Форы угловых 1-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (date_filter_statistic_transformer_fitter_data['description'],),
        'predictor': RefitterWrappedPredictor( magic_fitter(corners_first_period_statistic_fitter, date_filter_statistic_transformer_fitter_data), predictor_class=CornersResultProbabilitiesAttackDefensePredictor ),
        'proposers_data': corners_first_period_handicaps_proposers_data
    }, {
        'name': 'corners_second_period_handicaps-corners_second_period_attack_defense-%s' % (date_filter_statistic_transformer_fitter_data['name'],),
        'description': 'Форы угловых 2-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (date_filter_statistic_transformer_fitter_data['description'],),
        'predictor': RefitterWrappedPredictor( magic_fitter(corners_second_period_statistic_fitter, date_filter_statistic_transformer_fitter_data), predictor_class=CornersResultProbabilitiesAttackDefensePredictor ),
        'proposers_data': corners_second_period_handicaps_proposers_data
    }, {
        'name': 'corners_totals-corners_attack_defense-%s' % (date_filter_statistic_transformer_fitter_data['name'],),
        'description': 'Тоталы угловых, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (date_filter_statistic_transformer_fitter_data['description'],),
        'predictor': RefitterWrappedPredictor( magic_fitter(corners_statistic_fitter, date_filter_statistic_transformer_fitter_data), predictor_class=CornersResultProbabilitiesAttackDefensePredictor ),
        'proposers_data': corners_totals_proposers_data
    }, {
        'name': 'corners_first_period_totals-corners_first_period_attack_defense-%s' % (date_filter_statistic_transformer_fitter_data['name'],),
        'description': 'Тоталы угловых 1-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (date_filter_statistic_transformer_fitter_data['description'],),
        'predictor': RefitterWrappedPredictor( magic_fitter(corners_first_period_statistic_fitter, date_filter_statistic_transformer_fitter_data), predictor_class=CornersResultProbabilitiesAttackDefensePredictor ),
        'proposers_data': corners_first_period_totals_proposers_data
    }, {
        'name': 'corners_second_period_totals-corners_second_period_attack_defense-%s' % (date_filter_statistic_transformer_fitter_data['name'],),
        'description': 'Тоталы угловых 2-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (date_filter_statistic_transformer_fitter_data['description'],),
        'predictor': RefitterWrappedPredictor( magic_fitter(corners_second_period_statistic_fitter, date_filter_statistic_transformer_fitter_data), predictor_class=CornersResultProbabilitiesAttackDefensePredictor ),
        'proposers_data': corners_second_period_totals_proposers_data
    }, {
        'name': 'corners_individual_totals-corners_attack_defense-%s' % (date_filter_statistic_transformer_fitter_data['name'],),
        'description': 'Индивидуальные тоталы угловых, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (date_filter_statistic_transformer_fitter_data['description'],),
        'predictor': RefitterWrappedPredictor( magic_fitter(corners_statistic_fitter, date_filter_statistic_transformer_fitter_data), predictor_class=CornersResultProbabilitiesAttackDefensePredictor ),
        'proposers_data': corners_individual_totals_proposers_data
    }, {
        'name': 'corners_first_period_individual_totals-corners_attack_defense-%s' % (date_filter_statistic_transformer_fitter_data['name'],),
        'description': 'Индивидуальные тоталы угловых 1-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (date_filter_statistic_transformer_fitter_data['description'],),
        'predictor': RefitterWrappedPredictor( magic_fitter(corners_first_period_statistic_fitter, date_filter_statistic_transformer_fitter_data), predictor_class=CornersResultProbabilitiesAttackDefensePredictor ),
        'proposers_data': corners_first_period_individual_totals_proposers_data
    }, {
        'name': 'corners_second_period_individual_totals-corners_attack_defense-%s' % (date_filter_statistic_transformer_fitter_data['name'],),
        'description': 'Индивидуальные тоталы угловых 2-го тайма, предсказание по атаке и обороне команд (используются угловые, рассматривается вероятность счетов) (%s)' % (date_filter_statistic_transformer_fitter_data['description'],),
        'predictor': RefitterWrappedPredictor( magic_fitter(corners_second_period_statistic_fitter, date_filter_statistic_transformer_fitter_data), predictor_class=CornersResultProbabilitiesAttackDefensePredictor ),
        'proposers_data': corners_second_period_individual_totals_proposers_data
     }]

    experiments = StandardExperimentsCollection(providers_data, db_name=db_name, matches_collection_name=matches_collection_name, sample_condition=sample_condition)
    experiments.make()
