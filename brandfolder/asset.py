from brandfolder.resource import Resource
from brandfolder.resource_container import ResourceContainer

from brandfolder.attachment import Attachment


class Asset(Resource):
    RESOURCE_NAME = 'Asset'
    RESOURCE_TYPE = 'assets'

    def __init__(self, client, data):
        super().__init__(client, data)

        self.attachments = ResourceContainer(client, Attachment, 'attachments', parent=self)

    def __repr__(self):
        return f'<{self.resource_name} {self.attributes["name"]}>'
