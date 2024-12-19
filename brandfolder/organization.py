from brandfolder.resource import Resource
from brandfolder.resource_container import ResourceContainer


class Organization(Resource):
    RESOURCE_NAME = 'Organization'
    RESOURCE_TYPE = 'organizations'

    def __init__(self, client, **kwargs):
        super().__init__(client, **kwargs)

    def __repr__(self):
        return f'<{self.resource_name} {self.attributes["slug"]}: {self.id}>'
