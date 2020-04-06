from brandfolder.resource import Resource
# from resource_container import ResourceContainer


class Attachment(Resource):
    RESOURCE_NAME = 'Attachment'
    RESOURCE_TYPE = 'attachments'

    def __repr__(self):
        return f'<{self.resource_name} {self.attributes["filename"]}>'
