import os
import pickle
from betrobot.util.pickable import Pickable
from betrobot.betting.experiment import Experiment
from betrobot.betting.provider import Provider
from betrobot.util.common_util import safe_get


class StandardExperimentsCollection(Pickable):

    _pick = [ '_experiments' ]


    def __init__(self, providers_data, db_name, matches_collection_name, sample_condition, value_thresholds_data):
        Pickable.__init__(self)

        self._experiments = []
        for provider_data in providers_data:
            provider_proposers_value_thresholds_data = safe_get(value_thresholds_data, provider_data['name'], {})

            provider_proposers_data = []
            for proposer_data in provider_data['proposers_data']:
                proposer_class = proposer_data['proposer_class']
                proposer_value_threshold = safe_get(provider_proposers_value_thresholds_data, proposer_data['name'], None)
                new_proposer_data = {
                    'name': proposer_data['name'],
                    'proposer': proposer_class(value_threshold=proposer_value_threshold)
                }
                provider_proposers_data.append(new_proposer_data)

            provider = Provider(provider_data['name'], provider_data['description'], predictor=provider_data['predictor'], proposers_data=provider_proposers_data)
            experiment = Experiment(provider, db_name=db_name, matches_collection_name=matches_collection_name, sample_condition=sample_condition)
            self._experiments.append(experiment)


    def make(self):
        for experiment in self._experiments:
            print()

            experiment.test()

            print(experiment.get_investigation())

            experiment.clear()

            file_name = 'provider-%s.pkl' % (experiment.provider.name,)
            file_path = os.path.join('data', 'providers', file_name)
            with open(file_path, 'wb') as f:
                pickle.dump(experiment.provider, f)

            print()
