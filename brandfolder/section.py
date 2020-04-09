from brandfolder.resource import Resource
from brandfolder.resource_container import ResourceContainer
from brandfolder.asset import Asset


class Section(Resource):
    RESOURCE_NAME = 'Section'
    RESOURCE_TYPE = 'sections'

    def __init__(self, client, data):
        super().__init__(client, data)

        self.assets = ResourceContainer(client, Asset, parent=self, include=True)

    def __repr__(self):
        return f'<{self.resource_name} {self.attributes["name"]}>'
