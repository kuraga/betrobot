import os
import io
import logging
from betrobot.util.pickable_mixin import PickableMixin
from betrobot.util.printable_mixin import PrintableMixin
from betrobot.util.database_util import db
from betrobot.util.common_util import get_object, get_identifier
from betrobot.util.logging_util import get_logger
from betrobot.betting.sport_util import get_match_header, get_match_title


class Provider(PickableMixin, PrintableMixin):

    _pick = [ 'description', 'fitters_sets', 'predictor', 'proposers', 'attempt_matches' ]


    def __init__(self, fitters_sets, predictor, proposers, description=None):
        super().__init__()

        self.description = description
        self.fitters_sets = [
            [ get_object(fitter) for fitter in fitters_set ] \
                 for fitters_set in fitters_sets
        ]
        self.predictor = get_object(predictor)
        self.proposers = [ get_object(proposer) for proposer in proposers ]

        self.clean()
        self._prefit_fitters()


    @property
    def _pick_path(self):
        return os.path.join('data', 'providers')


    @property
    def _pick_name(self):
        return 'provider-%s-%s' % (self.__class__.__name__, self.uuid,)


    def handle(self, match_uuid, fit_kwargs=None, predict_kwargs=None, handle_kwargs=None):
        if fit_kwargs is None:
            fit_kwargs = {}
        if predict_kwargs is None:
            predict_kwargs = {}
        if handle_kwargs is None:
            handle_kwargs = {}

        match_header = get_match_header(match_uuid)
        if match_header is None:
            return

        log_capture_string = io.StringIO()
        ch = logging.StreamHandler(log_capture_string)
        ch.setLevel(logging.DEBUG)
        get_logger().addHandler(ch)

        # get_logger('prediction').debug('Провайдер: %s', str(self))
        get_logger('prediction').info('Описание провайдера: %s', self.description)
        get_logger('prediction').info('Предсказание для матча %s', get_match_title(match_header, show_uuid=True))

        fitters_for_predictor = []
        for fitters_set in self.fitters_sets:
            if len(fitters_set) == 0:
                continue

            fitters_set[0].fit(match_header=match_header, **fit_kwargs)
            for j in range(1, len(fitters_set)):
                fitters_set[j].fit(match_header=match_header, **fit_kwargs)
            fitters_for_predictor.append(fitters_set[-1])

        prediction = self.predictor.predict(fitters_for_predictor, match_header, **predict_kwargs)

        get_logger().removeHandler(ch)
        log_contents = log_capture_string.getvalue()
        log_capture_string.close()

        prediction_info_uuid = get_identifier()
        prediction_info = {
            'uuid': prediction_info_uuid,
            'match_uuid': match_uuid,
            'provider_class_name': self.__class__.__name__,
            'provider_description': self.description,
            'provider_uuid': self.uuid,
            'prediction': prediction,
            'log': log_contents
        }

        prediction_infos_collection = db['prediction_infos']
        prediction_infos_collection.insert_one(prediction_info)

        for proposer in self.proposers:
            proposer.handle(match_header, prediction_info=prediction_info, **handle_kwargs)

        self.attempt_matches.add(match_header['uuid'])


    @property
    def matches_count(self):
        return len(self.attempt_matches)


    def clean(self):
        self.attempt_matches = set()

        for fitters_set in self.fitters_sets:
            for fitter in fitters_set:
                fitter.clean()

        for proposer in self.proposers:
            proposer.clean()


    def _prefit_fitters(self):
        for fitters_set in self.fitters_sets:
            if len(fitters_set) == 0:
                continue

            fitters_set[0].prefit(None)
            for j in range(1, len(fitters_set)):
                fitters_set[j].prefit(fitters_set[j-1])


    def _get_init_strs(self):
        return [
            'fitters_sets=[%s]' % (', '.join([ ', '.join(map(str, fitters_set)) for fitters_set in self.fitters_sets ]),),
            'predictor=%s' % (str(self.predictor),),
            'proposers=[%s]' % (str(', '.join(map(str, self.proposers))),)
        ]


    def _get_runtime_strs(self):
        return [
            'uuid=%s' % (self.uuid,)
        ]
