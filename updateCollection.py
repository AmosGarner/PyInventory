from DataObjects.Collection import Collection
from ObjectFactories.ItemFactory import ItemFactory
import json

def main():
    updateCollection(
        Collection('items', 'agarner', []),
        ItemFactory.factory('item', [0, 'someItem', 'date', 'date']),
        'collections/agarner_collections/agarner_Items_collection.dat'
    )

def getCollection(fileName):
    collectionFile = open(fileName, 'r')
    fileData = json.loads(collectionFile.read())
    itemData = fileData['items']
    collection = Collection(fileData['username'], fileData['collectionName'], fileData['items'])


def updateCollection(collection, item, fileName):
    collection.items.append(item)
    getCollection(fileName)

if __name__ == '__main__':
    main()
