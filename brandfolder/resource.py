from abc import ABC, abstractmethod
from typing import Optional


class Resource(ABC):
    def __init__(self, client, data):
        self.client = client
        self._id = data['id']
        self.type = data['type']
        self._attributes = data['attributes']
        self._updates = {}
        self.resource_name = self.__class__.RESOURCE_NAME
        self.resource_type = self.__class__.RESOURCE_TYPE
        self.endpoint = f'/{self.resource_type}/{self._id}'

    def __str__(self):
        return f'{self.resource_name} {self.id}: {self.attributes}'

    @abstractmethod
    def __repr__(self):
        return '''Return the object representation'''

    @property
    def id(self):
        return self._id

    @property
    def attributes(self):
        return {**self._attributes, **self._updates}

    def get(self, key, default=None):
        """Returns the value for key if key exists on the object, else default.
        If default is not given, it default to None, so that this method never
        raises a KeyError.

        Args:
            key (str): Attribute name
            default: Fallback value to return

        Returns:
            Value on the Resource
        """
        return self._attributes.get(key, default)

    @property
    def updates(self):
        '''Local changes to be pushed to Brandfolder'''
        return self._updates.copy()

    def refresh(self):
        data = self.client.get_data(self.endpoint)
        self._attributes = data['attributes']

    def set(self, **updates):
        self._updates.update(updates)
        self.attributes.update(updates)
        return self

    def update(self):
        data = {
            'data': {
                'attributes': self.updates
            }
        }
        self.client.put(self.endpoint, json=data)
        self._updates = {}
        return self

    def delete(self):
        self.client.delete(self.endpoint)
