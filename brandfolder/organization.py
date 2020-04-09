from brandfolder.resource import Resource
from brandfolder.resource_container import ResourceContainer
from brandfolder.brandfolder import Brandfolder


class Organization(Resource):
    RESOURCE_NAME = 'Organization'
    RESOURCE_TYPE = 'organizations'

    def __init__(self, client, data):
        super().__init__(client, data)

        self.brandfolders = ResourceContainer(client, Brandfolder, parent=self, include=True)

    def __repr__(self):
        return f'<{self.resource_name} {self.attributes["slug"]}: {self.id}>'
