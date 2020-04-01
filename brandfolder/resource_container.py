class ResourceContainer:
    def __init__(self, client, resource_class, resource_type, parent=None, include=False):
        self.client = client
        self.resource_class = resource_class
        self.resource_type = resource_type

        if parent is None:
            self.endpoint = f'/{resource_type}'
        else:
            if include:
                self.endpoint = f'/{parent.resource_type}/{parent.id}'
            else:
                self.endpoint = f'/{parent.resource_type}/{parent.id}/{resource_type}'

        self.parent = parent
        self.include = include

    def fetch(self, params=None, per=None, page=None, **kwargs):
        if params is None:
            params = {}

        if per:
            params['per'] = per
        if page:
            params['page'] = page

        # E.g. to do /organizations/<org_id>?include=brandfolders
        # rather than the typical /brandfolders/<bf_id>/assets
        if self.include:
            if 'include' in params:
                if self.resource_type not in params['include']:
                    params['include'] += f',{self.resource_type}'
            else:
                params['include'] = self.resource_type

        res = self.client.get(endpoint=self.endpoint, params=params, **kwargs)
        if self.include:
            return [self.resource_class(self.client, data)
                    for data in res['included'] if data['type'] == self.resource_type]
        else:
            return [self.resource_class(self.client, data)
                    for data in res['data']]

    def first(self, params=None, **kwargs):
        if params is None:
            params = {}
        params['per'] = 1
        resources = self.fetch(params)

        return resources[0] if resources else None

    def fetch_by_id(self, id, **kwargs):
        data = self.client.get_data(endpoint=f'/{self.resource_type}/{id}', **kwargs)

        return self.resource_class(self.client, data)

    def search(self, query_params, **kwargs):
        params = {'search': query_params, **kwargs}
        return self.fetch(params=params)
