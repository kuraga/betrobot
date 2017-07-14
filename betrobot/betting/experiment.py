import os
import tqdm
import numpy as np
import pandas as pd
from betrobot.util.pickable_mixin import PickableMixin
from betrobot.util.printable_mixin import PrintableMixin
from betrobot.util.common_util import get_object, is_template
from betrobot.util.database_util import db
from betrobot.betting.provider import Provider


class Experiment(PickableMixin, PrintableMixin):

    _pick = [ 'description', 'providers', 'presenters', 'test_sample_condition' ]


    def __init__(self, providers_data, presenters, description=None, test_sample_condition=None):
        super().__init__()

        if test_sample_condition is None:
            test_sample_condition = {}

        self.description = description
        self.test_sample_condition = test_sample_condition

        self.providers = [ self._create_provider(provider_data) for provider_data in providers_data ]
        self.presenters = [ get_object(presenter) for presenter in presenters ]


    @property
    def _pick_path(self):
        return os.path.join('data', 'experiments')


    @property
    def _pick_name(self):
        return 'experiment-%s' % (self.uuid,)


    def _create_provider(self, provider_data):
        description = 'В рамках эксперимента %s' % (self.uuid,)
        if self.description is not None:
            description += '\nОписание эксперимента: %s' % (self.description,)

        for fitter_templates in provider_data['fitters_sets']:
           if not all(map(is_template, fitter_templates)):
                raise ValueError('Fitters should be represented as templates not objects')

        provider = Provider(provider_data['fitters_sets'], provider_data['predictor'], provider_data['proposers'], description=description)

        return provider


    def test(self):
        match_headers_collection = db['match_headers']
        sample = match_headers_collection.find(self.test_sample_condition, { 'uuid': True })
        for match_header in tqdm.tqdm(sample, total=sample.count()):
            for provider in self.providers:
                provider.handle(match_header['uuid'])


    def get_representation(self, present_kwargs=None):
        if present_kwargs is None:
            present_kwargs = {}

        result = ''

        result += '**************************************************'
        result += '\nЭксперимент %s' % (self.uuid,)
        result += '\n'
        if self.description is not None:
            result += '\n%s' % (self.description,)
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


    def clean(self):
        for provider in self.providers:
            provider.clean_proposers()


    def save_providers(self):
        for provider in self.providers:
            provider.save()


    def _get_init_strs(self):
        return [
            'providers=[%s]' % (str(', '.join(map(str, self.providers))),),
            'presenters=[%s]' % (str(', '.join(map(str, self.presenters))),),
            'test_sample_condition=%s' % (str(self.test_sample_condition),)
        ]


    def _get_runtime_strs(self):
        return [
            'uuid=%s' % (self.uuid,)
        ]
