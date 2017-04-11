import uuid
from betrobot.util.pickable import Pickable


class Provider(Pickable):

    _pick = [ 'uuid', 'name', 'description', 'predictor', 'proposers_data' ]


    def __init__(self, name, description, predictor=None, proposers_data=None):
        super().__init__()

        self.uuid = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.predictor = predictor
        self.proposers_data = proposers_data


    def handle(self, betcity_match, whoscored_match=None, predict_kwargs=None, handle_kwargs=None):
        if predict_kwargs is None:
            predict_kwargs = {}
        if handle_kwargs is None:
            handle_kwargs = {}

        prediction = self.predictor.predict(betcity_match, **predict_kwargs)

        for proposer_data in self.proposers_data:
            proposer_data['proposer'].handle(betcity_match, prediction, whoscored_match=whoscored_match, **handle_kwargs)


    # TODO: save, load


    def clear_proposers(self):
        for proposer_data in self.proposers_data:
            proposer_data['proposer'].clear()
