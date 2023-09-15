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

    def paginated_fetch(self, params=None, per=None, page=None, **kwargs):
        if params is None:
            params = {}

        if per:
            params['per'] = per
        if page:
            params['page'] = page

        res = self.client.get(endpoint=self.endpoint, params=params, **kwargs)
        included = res.get('included', [])

        return [self.resource_class(self.client, data=data, included=included)
                for data in res['data']], res['meta']

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


class ModifiedResourceContainer(ResourceContainer):
    """
    ModifiedResourceContainer is a modified resource container for organizations to fetch assets and attachments
    without using the deprecated endpoints /organizations/{id}/assets and /organizations/{id}/attachments
    """
    restricted = ['assets', 'attachments']

    def fetch(self, params=None, per=100, page=1, **kwargs):
        total_resources_to_fetch = per * page

        if self.parent \
            and self.parent.resource_type == 'organizations' \
            and self.resource_type in self.restricted:

            resources = []
            stop_op = False

            brandfolders = self.parent.brandfolders.fetch()

            while len(resources) < total_resources_to_fetch and not stop_op:
                for i, brandfolder in enumerate(brandfolders):
                    method = getattr(brandfolder, 'assets') if self.resource_type == 'assets' else getattr(brandfolder,
                                                                                                           'attachments')

                    stop_page_for_this_bf = False
                    p = 1
                    while stop_page_for_this_bf is False:
                        fetched_resources, meta = method.paginated_fetch(per=100, page=p, **kwargs)
                        resources.extend(fetched_resources)
                        if len(resources) >= total_resources_to_fetch or len(fetched_resources) == 0 or meta[
                            'total_pages'] == p:
                            stop_page_for_this_bf = True
                        else:
                            p += 1

                    if i == len(brandfolders) - 1:
                        stop_op = True
                        break

                if len(resources) >= total_resources_to_fetch:
                    resources = resources[:total_resources_to_fetch]
                    break

            return resources[-per:]

        res = self.client.get(endpoint=self.endpoint, params=params, **kwargs)
        included = res.get('included', [])

        return [self.resource_class(self.client, data=data, included=included)
                for data in res['data']]
