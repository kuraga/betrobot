from betting.providers.sample_fit_predict_propose_provider import SampleFitPredictProposeProvider
from betting.samplers.historical_sampler import HistoricalSampler
from betting.fitters.corners_attack_defense_fitter import CornersAttackDefenseFitter
from betting.predictors.corners_attack_defense_results_predictor import CornersResultsAttackDefensePredictor
from betting.proposers.corners_results_attack_defense_proposer import CornersResults1AttackDefenseProposer, CornersResults1XAttackDefenseProposer, CornersResultsX2AttackDefenseProposer, CornersResults2AttackDefenseProposer
from util.common_util import safe_get


class CornersResultsAttackDefenseHistoricalProvider(SampleFitPredictProposeProvider):

    def __init__(self, thresholds=None):
        train_sampler = HistoricalSampler()
        fitter = CornersAttackDefenseFitter()
        predictor = CornersResultsAttackDefensePredictor()
        proposers_data = [{
            'name': '1',
            'proposer': CornersResults1AttackDefenseProposer(threshold=safe_get(thresholds, '1'))
        }, {
            'name': '1X',
            'proposer': CornersResults1XAttackDefenseProposer(threshold=safe_get(thresholds, '1X'))
        }, {
            'name': 'X2',
            'proposer': CornersResultsX2AttackDefenseProposer(threshold=safe_get(thresholds, 'X2'))
        }, {
            'name': '2',
            'proposer': CornersResults2AttackDefenseProposer(threshold=safe_get(thresholds, '2'))
        }]

        SampleFitPredictProposeProvider.__init__(self, train_sampler, fitter, predictor, proposers_data)
