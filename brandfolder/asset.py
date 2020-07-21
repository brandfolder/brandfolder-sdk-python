from brandfolder.resource import Resource
from brandfolder.resource_container import ResourceContainer

from brandfolder.attachment import Attachment


class Asset(Resource):
    RESOURCE_NAME = 'Asset'
    RESOURCE_TYPE = 'assets'

    def __init__(self, client, **kwargs):
        super().__init__(client, **kwargs)

        self.attachments = ResourceContainer(client, Attachment, parent=self)

    def __repr__(self):
        return f'<{self.resource_name} {self.attributes["name"]}>'
