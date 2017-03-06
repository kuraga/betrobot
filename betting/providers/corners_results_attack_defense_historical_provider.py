import sys
sys.path.append('./')
sys.path.append('./util')
sys.path.append('./betting')
sys.path.append('./betting/providers')
sys.path.append('./betting/samplers')
sys.path.append('./betting/fitters')
sys.path.append('./betting/predictors')
sys.path.append('./betting/proposers')


from sample_fit_predict_propose_provider import SampleFitPredictProposeProvider
from historical_sampler import HistoricalSampler
from corners_attack_defense_fitter import CornersAttackDefenseFitter
from corners_attack_defense_results_predictor import CornersResultsAttackDefensePredictor
from corners_results_attack_defense_proposer import CornersResultsAttackDefenseProposer


class CornersResultsAttackDefenseHistoricalProvider(SampleFitPredictProposeProvider):
    def __init__(self, thresholds=None):
        train_sampler = HistoricalSampler()
        fitter = CornersAttackDefenseFitter()
        predictor = CornersResultsAttackDefensePredictor()
        proposer = CornersResultsAttackDefenseProposer(thresholds=thresholds)

        SampleFitPredictProposeProvider.__init__(self, train_sampler, fitter, predictor, proposer)
