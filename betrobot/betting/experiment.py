import uuid
import os
import pickle
import pymongo
import pprint
import tqdm
import numpy as np
import pandas as pd
from betrobot.util.pickable import Pickable
from betrobot.betting.provider import Provider


def _get_object(object_or_data):
    if not isinstance(object_or_data, tuple):
        return object_or_data
    else:
        (class_, args, kwargs) = object_or_data
        return class_(*args, **kwargs)


class Experiment(Pickable):

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
        fitter = _get_object(provider_data['fitter'])
        if not fitter.is_fitted:
            fitter.fit(train_sampler, self.train_sample_condition)

        if 'refitters' not in provider_data or provider_data['refitters'] is None:
            refitters = None
        else:
            # TODO: refitter не может быть объектом
            refitters = [ _get_object(refitter) for refitter in provider_data['refitters'] ]

        predictor = _get_object(provider_data['predictor'])

        proposers = [ _get_object(proposer) for proposer in provider_data['proposers'] ]

        provider = Provider(fitter, refitters, predictor, proposers, description=description)

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

            # TODO: Сделать выбор матча/матчей на основе даты
            if len(data['betarch']) == 0:
                continue
            # FIXME DEBUG: не УГЛ!
            i = np.argmax([ len(betarch_match['bets']) if betarch_match['specialWord'] == 'УГЛ' else -1 for betarch_match in data['betarch'] ])
            betarch_match = data['betarch'][i]

            for provider in self.providers:
                provider.handle(betarch_match, whoscored_match=whoscored_match)

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


    def __str__(self):
        return '%s(providers=[%s], presenters=[%s], db_name="%s", collection_name="%s", train_sample_condition=%s, test_sample_condition=%s)[uuid=%s]' % (self.__class__.__name__, str(', '.join(map(str, self.providers))), str(', '.join(map(str, self.presenters))), self.db_name, self.collection_name, str(self.train_sample_condition), str(self.test_sample_condition), self.uuid)
