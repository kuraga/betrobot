import uuid
import os
import pickle
import pymongo
import pprint
import tqdm
import numpy as np
import pandas as pd
from betrobot.util.pickable_mixin import PickableMixin
from betrobot.util.printable_mixin import PrintableMixin
from betrobot.betting.provider import Provider


def _get_object(object_or_data):
    if not isinstance(object_or_data, tuple):
        return object_or_data
    else:
        (class_, args, kwargs) = object_or_data
        return class_(*args, **kwargs)


class Experiment(PickableMixin, PrintableMixin):

    _pick = [ 'uuid', 'description', 'providers', 'presenters', 'db_name', 'collection_name', 'train_sample_condition', 'test_sample_condition' ]


    def __init__(self, providers_data, presenters, description=None, db_name='betrobot', collection_name='matches', train_sample_condition=None, test_sample_condition=None):
        super().__init__()

        if test_sample_condition is None:
            test_sample_condition = {}

        self.description = description
        self.db_name = db_name
        self.collection_name = collection_name
        self.train_sample_condition = train_sample_condition
        self.test_sample_condition = test_sample_condition

        self.uuid = str(uuid.uuid4())
        self.providers = [ self._create_provider(provider_data) for provider_data in providers_data ]
        self.presenters = [ _get_object(presenter) for presenter in presenters ]

        self._init_collection()


    def _create_provider(self, provider_data):
        description = ''

        description += 'В рамках эксперимента %s' % (self.uuid,)
        if self.description is not None:
            description += '\nОписание эксперимента: %s' % (self.description,)

        train_sampler = _get_object(provider_data['train_sampler'])

        # TODO: fitter не может быть объектом
        fitters = [ _get_object(fitter_or_template) for fitter_or_template in provider_data['fitters'] ]
        for fitter in fitters:
            if not fitter.is_fitted:
                fitter.fit(train_sampler, self.train_sample_condition)

        if 'refitters_sets' not in provider_data or provider_data['refitters_sets'] is None:
            refitters_sets = None
        else:
            # TODO: refitter не может быть объектом
            refitters_sets = [
                [ _get_object(refitter_or_template) for refitter_or_template in refitters_or_templates ] \
                     for refitters_or_templates in provider_data['refitters_sets']
            ]

        predictor = _get_object(provider_data['predictor'])

        proposers = [ _get_object(proposer) for proposer in provider_data['proposers'] ]

        provider = Provider(fitters, refitters_sets, predictor, proposers, description=description)

        return provider


    def _on_unpickle(self):
        super()._on_unpickle()

        self._init_collection()


    def _init_collection(self):
        self._client = pymongo.MongoClient()
        self._db = self._client[self.db_name]
        self._matches_collection = self._db[self.collection_name]


    def test(self):
        sample = self._matches_collection.find(self.test_sample_condition)

        for data in tqdm.tqdm(sample, total=sample.count()):
            whoscored_match = data['whoscored'][0]

            if len(data['betarch']) == 0:
                continue

            # TODO: Сделать выбор матча/матчей на основе даты
            main_match_index = np.argmax([ -1 ] + [ len(betarch_match['bets']) if betarch_match['specialWord'] is None else -1 for betarch_match in data['betarch'] ]) - 1
            corners_match_index = np.argmax([ -1 ] + [ len(betarch_match['bets']) if betarch_match['specialWord'] == 'УГЛ' else -1 for betarch_match in data['betarch'] ]) - 1
            yellow_cards_match_index = np.argmax([ -1 ] + [ len(betarch_match['bets']) if betarch_match['specialWord'] == 'ЖК' else -1 for betarch_match in data['betarch'] ]) - 1

            for provider in self.providers:
                if main_match_index >= 0:
                    provider.handle(data['betarch'][main_match_index], whoscored_match=whoscored_match)
                if corners_match_index >= 0:
                    provider.handle(data['betarch'][corners_match_index], whoscored_match=whoscored_match)
                if yellow_cards_match_index >= 0:
                    provider.handle(data['betarch'][yellow_cards_match_index], whoscored_match=whoscored_match)

        # DEBUG
        # for proposer in self.provider.proposers:
        #    proposer.flush(self._db['proposed'])


    def get_representation(self, present_kwargs=None):
        if present_kwargs is None:
            present_kwargs = {}

        result = ''

        result += '**************************************************'
        result += '\nЭксперимент %s' % (self.uuid,)
        result += '\n'
        if self.description is not None:
            result += '\n%s' % (self.description,)
        result += '\nУсловие обучающей выборки: %s' % str(self.train_sample_condition)
        result += '\nУсловие тестовой выборки: %s' % str(self.test_sample_condition)
        result += '\n'

        for provider in self.providers:
            result += '\n=================================================='
            result += '\nПровайдер %s' % (str(provider),)
            if provider.description is not None:
                result += '\n%s' % (provider.description,)
            result += '\n'

            for presenter in self.presenters:
                result += '\n> Провайдер %s(...)[uuid=%s], презентер %s' % (provider.__class__.__name__, provider.uuid, str(presenter))
                result += '\n'
                result += presenter.present(provider, **present_kwargs)
                result += '\n'

            result += '\n=================================================='

        result += '\n**************************************************'
        result += '\n'

        return result


    # TODO: load


    def save(self):
        file_name = 'experiment-%s.pkl' % (self.uuid,)
        file_path = os.path.join('data', 'experiments', file_name)
        with open(file_path, 'wb') as f_out:
            pickle.dump(self, f_out)


    def clear(self):
        for provider in self.providers:
            provider.clear_proposers()


    def save_providers(self):
        for provider in self.providers:
            provider.save()


    def _get_init_strs(self):
        return [
            'uuid=%s' % (self.uuid,),
            'providers=[%s]' % (str(', '.join(map(str, self.providers))),),
            'presenters=[%s]' % (str(', '.join(map(str, self.presenters))),),
            'db_name=%s' % (self.db_name,),
            'collection_name=%s' % (self.collection_name,),
            'train_sample_condition=%s' % (str(self.train_sample_condition),),
            'test_sample_condition=%s' % (str(self.test_sample_condition),)
        ]
