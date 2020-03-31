# The Official Python Brandfolder SDK

[![Brandfolder](https://cdn.brandfolder.io/YUHW9ZNT/as/znoqr595/Primary_Logo.jpg)](https://brandfolder.com)

## Installation

Install latest official build:
```sh
pip install brandfolder
```

Install from source:
```sh
git clone https://github.com/brandfolder/brandfolder-python-sdk.git
cd brandfolder-python-sdk
python setup.py install
```
## Usage
Interation with the Brandfolder API via the Python SDK is client based. The first thing you need to do
is create a client:

`client = Client(api_key=API_KEY)`

A valid Brandfolder API key is required for all actions. Find yours at https://brandfolder.com/profile#integrations.

#### Methods for interacting with Brandfolder:

`fetch()`: Returns all available objects of the provided type.

`first()`: Returns the first object returned of the provided type.

`fetch_by_id()`: Returns the object associated with the provided type and id.

`id()`: Returns the id of the associated object.

`attributes()`: Returns the attributes of the provided object.

`get(<attribute>)`: Returns the provided attribute value of the associated object.

`refresh()`: Updates associated objects attributes with what currently exists in Brandfolder.

`set(<updates>)`: Prepares to apply provided updates to the associated object.

`updates()`: Displays staged updates to the associated object that are ready to apply.

`update()`: Pushes updates to the associated object to Brandfolder.

`delete()`: Deletes the associated object in Brandfolder.

`brandfolder.create_section()`: Creates section in the associated Brandfolder.

`brandfolder.create_collection()`: Creates collection in the associated Brandfolder.

`brandfolder.create_asset()`: Creates asset in the associated Brandfolder. This is also available for a Collection.

`brandfolder.search([parameters])`: Returns assets in the associated Brandfolder that match the list of search parameters provided

#### Examples:
Get all available organizations:
```sh
orgs = client.organizations.fetch()
```

Get a specific Brandfolder:
```sh
bf = client.brandfolders.fetch_by_id(<brandfolder_id)
```

Updating an asset:
```sh
asset = bf.assets.fetch_by_id(<asset_id>)  # Grab an asset
asset.set(name='New Name')  # Can pass attributes as a dict as well {'name': 'New Name'}
asset.update()  # Pushes new attributes to Brandfolder
```

Search for assets:
```sh
# Will return results with a name containing "Sample" of filetype ".png"

bf = client.brandfolders.fetch_by_id(<brandfolder_id)
search_parameters = ['name:sample', 'extension:png`]
results = bf.search(search_parameters)
```
