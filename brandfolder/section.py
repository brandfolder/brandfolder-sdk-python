from brandfolder.resource import Resource
from brandfolder.resource_container import ResourceContainer
from brandfolder.asset import Asset
from brandfolder.attachment import Attachment


class Section(Resource):
    RESOURCE_NAME = 'Section'
    RESOURCE_TYPE = 'sections'

    def __init__(self, client, **kwargs):
        super().__init__(client, **kwargs)

        self.assets = ResourceContainer(client, Asset, parent=self)
        self.attachments = ResourceContainer(client, Attachment, parent=self)

    def __repr__(self):
        return f'<{self.resource_name} {self.attributes["name"]}>'
