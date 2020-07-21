class ResourceContainer:
    def __init__(self, client, resource_class=None, parent=None, include=False):
        self.client = client
        self.resource_class = resource_class or self.__class__
        self.resource_type = self.resource_class.RESOURCE_TYPE

        if parent is None:
            self.endpoint = f'/{self.resource_type}'
        else:
            if include:
                self.endpoint = f'/{parent.resource_type}/{parent.id}'
            else:
                self.endpoint = f'/{parent.resource_type}/{parent.id}/{self.resource_type}'

        self.parent = parent

    def fetch(self, params=None, per=None, page=None, **kwargs):
        if params is None:
            params = {}

        if per:
            params['per'] = per
        if page:
            params['page'] = page

        res = self.client.get(endpoint=self.endpoint, params=params, **kwargs)
        included = res.get('included', [])

        return [self.resource_class(self.client, data=data, included=included)
                for data in res['data']]

    def first(self, params=None, **kwargs):
        if params is None:
            params = {}
        params['per'] = 1
        resources = self.fetch(params)

        return resources[0] if resources else None

    def fetch_by_id(self, id, **kwargs):
        body = self.client.get(endpoint=f'/{self.resource_type}/{id}', **kwargs)

        return self.resource_class(self.client, body=body)

    def search(self, query_params, **kwargs):
        params = {'search': query_params, **kwargs}
        return self.fetch(params=params)
