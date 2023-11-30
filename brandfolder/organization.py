from brandfolder.resource import Resource
from brandfolder.resource_container import ResourceContainer, ModifiedResourceContainer
from brandfolder.asset import Asset
from brandfolder.attachment import Attachment
from brandfolder.brandfolder import Brandfolder


class Organization(Resource):
    RESOURCE_NAME = 'Organization'
    RESOURCE_TYPE = 'organizations'

    def __init__(self, client, **kwargs):
        super().__init__(client, **kwargs)
        self.brandfolders = ResourceContainer(client, Brandfolder, parent=self)
        self.assets = ModifiedResourceContainer(client, Asset, parent=self)
        self.attachments = ModifiedResourceContainer(client, Attachment, parent=self)


    def __repr__(self):
        return f'<{self.resource_name} {self.attributes["slug"]}: {self.id}>'
