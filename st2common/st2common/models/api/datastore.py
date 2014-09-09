from st2common.models.base import BaseAPI
from st2common.models.db.datastore import KeyValuePairDB


class KeyValuePairAPI(BaseAPI):
    model = KeyValuePairDB
    schema = {
        'type': 'object',
        'properties': {
            'id': {
                'type': 'string'
            },
            'description': {
                'type': 'string'
            },
            'name': {
                'type': 'string'
            },
            'value': {
                'type': 'string'
            }
        },
        'required': ['name', 'value'],
        'additionalProperties': False
    }

    @classmethod
    def to_model(cls, kvp):
        model = super(cls, cls).to_model(kvp)
        model.value = kvp.value
        return model
