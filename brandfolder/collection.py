from brandfolder.resource import Resource
from brandfolder.resource_container import ResourceContainer
from brandfolder.asset import Asset
from brandfolder.attachment import Attachment


class Collection(Resource):

    def __init__(self, client, data):
        super().__init__(client, data, 'Collection', 'collections')

        self.assets = ResourceContainer(client, Asset, 'assets', parent=self)
        self.attachments = ResourceContainer(client, Attachment, 'attachments', parent=self)

    def __repr__(self):
        return f'<{self.resource_name} {self.attributes["slug"]}>'

    def create_asset(self, attachments_data, section_key, **attributes):
        data = {
          'data': {
            'attributes': [
              {
                **attributes,
                'attachments': attachments_data
              }
            ]
          },
          'section_key': section_key
        }

        res = self.client.post(f'/{self.resource_type}/{self.id}/assets', json=data)
        return Asset(self.client, res['data'][0])
