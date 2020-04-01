# The Official Python Brandfolder SDK

[![Brandfolder](https://cdn.brandfolder.io/YUHW9ZNT/as/znoqr595/Primary_Brandfolder_Logo.png)](https://brandfolder.com)

## Installation

Install latest official build:
```sh
pip install brandfolder
```

Install from source:
```sh
git clone git@github.com:brandfolder/sdk-python.git
cd sdk-python
python setup.py install
```

## Usage
Interaction with the Brandfolder API via the Python SDK is client based. The first thing you need to do
is create a client:

`client = Client(api_key=API_KEY)`

A valid Brandfolder API key is required for all actions. Find yours at https://brandfolder.com/profile#integrations.

#### Methods for interacting with resource objects from Brandfolder:

`obj.fetch()`: Returns a list from the first page of available objects of the provided type.

`obj.first()`: Returns the first object returned of the provided type.

`obj.fetch_by_id(<resource_id>)`: Returns the object associated with the provided type and id.

`obj.get(<attribute>)`: Returns the provided attribute value of the associated object.

`obj.refresh()`: Updates local object attributes with what currently exists in Brandfolder.

`obj.set(<updates>)`: Prepares to apply provided updates to the associated object.

`obj.update()`: Pushes updates to the associated object to Brandfolder.

`obj.delete()`: Deletes the associated object in Brandfolder.

`brandfolder_obj.create_section()`: Creates section in the associated Brandfolder.

`brandfolder_obj.create_collection()`: Creates collection in the associated Brandfolder.

`brandfolder_obj.create_asset(attachments_data, section_key, **attributes)`: Creates asset in the associated Brandfolder. This is also available for a Collection.

`brandfolder_obj.search(query)`: Returns assets in the associated Brandfolder that match the query parameters provided.

#### Fields on resource objects:
`obj.id`: The id of the associated object.

`obj.attributes`: The attributes of the provided object.

`obj.updates`: A dict of staged updates to the associated object that are ready to apply.


#### Examples:
See the complete API documentation at https://developer.brandfolder.com for more examples.

Get all available organizations:
```python
orgs = client.organizations.fetch()
```

Get a specific Brandfolder:
```python
bf = client.brandfolders.fetch_by_id(<brandfolder_id>)
```

Updating an asset:
```python
asset = bf.assets.fetch_by_id(<asset_id>)  # Grab an asset
asset.set(name='New Name')
asset.update()  # Pushes new attributes to Brandfolder
```

Search for assets within a Brandfolder:
```python
# Will return results with a name containing "Sample" of filetype ".png"

bf = client.brandfolders.fetch_by_id(<brandfolder_id>)
search_parameters = ['name:sample', 'extension:png']
results = bf.assets.search(search_parameters)
```
