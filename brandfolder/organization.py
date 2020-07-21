from brandfolder.resource import Resource
from brandfolder.resource_container import ResourceContainer
from brandfolder.brandfolder import Brandfolder
from brandfolder.asset import Asset
from brandfolder.attachment import Attachment


class Organization(Resource):
    RESOURCE_NAME = 'Organization'
    RESOURCE_TYPE = 'organizations'

    def __init__(self, client, **kwargs):
        super().__init__(client, **kwargs)

        self.assets = ResourceContainer(client, Asset, parent=self)
        self.attachments = ResourceContainer(client, Attachment, parent=self)

    def __repr__(self):
        return f'<{self.resource_name} {self.attributes["slug"]}: {self.id}>'
