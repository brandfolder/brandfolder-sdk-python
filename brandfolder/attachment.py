from brandfolder.resource import Resource
# from resource_container import ResourceContainer


class Attachment(Resource):

    def __init__(self, client, data):
        super().__init__(client, data, 'Attachment', 'attachments')

    def __repr__(self):
        return f'<{self.resource_name} {self.attributes["filename"]}>'
