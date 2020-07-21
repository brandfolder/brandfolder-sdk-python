import logging
from typing import Optional
import os

from brandfolder.resource_container import ResourceContainer
from brandfolder.organization import Organization
from brandfolder.brandfolder import Brandfolder
from brandfolder.collection import Collection

import requests


class Client:

    def __init__(self,
                 api_key: str,
                 user_agent='brandfolder-python-sdk',
                 base_url='https://brandfolder.com/api/',
                 headers: Optional[dict] = None):
        """
        Creates a Client to interact with the Brandfolder API
        :param api_key: api key used to call the api
        :param headers: updated headers to
        """
        self.api_key = api_key
        self.url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'User-Agent': user_agent
        })
        if headers:
            self.session.headers.update(headers)

        self.organizations = ResourceContainer(self, Organization)
        self.brandfolders = ResourceContainer(self, Brandfolder)
        self.collections = ResourceContainer(self, Collection)

    def request(self, verb: str, endpoint: str, params: Optional[dict] = None, **kwargs) -> dict:
        if not params:
            params = {}

        version = kwargs.get('version', 'v4')

        with self.session.request(verb, f'{self.url}{version}{endpoint}', params=params, **kwargs) as res:
            logging.debug(f'{verb} {res.url}')
            try:
                res.raise_for_status()
            except requests.exceptions.HTTPError as e:
                logging.error(e)
                logging.error(f'Error for {verb} {res.url} with payload: {kwargs.get("json")}')
                raise

            return res.json()

    def get(self, endpoint, **kwargs):
        return self.request('GET', endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.request('PUT', endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request('POST', endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request('DELETE', endpoint, **kwargs)

    def fetch_resource_by_id(self, resource_class, id, params=None, **kwargs):
        """Fetches a given resource class by id

        Args:
            resource_class (child of Resource): The class to fetch
                and return instantiated.
            id (str): The specific instance identifier to fetch.
            params (dict): A dictionary of GET parameters,
                i.e. fields, include. Converted to query args.
            kwargs (dict): A dictionary of optional parameters.

        Returns:
            Resource: Instance of the provided resource_class

        """
        resource_type = resource_class.RESOURCE_TYPE
        body = self.get(f'/{resource_type}/{id}', params=params, **kwargs)

        return resource_class(self, body=body)

    def whoami(self, **kwargs):
        return self.request('GET', '/users/whoami', **kwargs)
