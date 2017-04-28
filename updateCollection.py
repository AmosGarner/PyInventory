from DataObjects.Collection import Collection
from ObjectFactories.ItemFactory import ItemFactory
import json

def main():
    updateCollection(
        Collection('item','Items', 'agarner', []),
        ItemFactory.factory('item', [0, 'someItem', 'date', 'date']),
        'collections/agarner_collections/agarner_Item_collection.dat'
    )

def getCollection(fileName):
    collectionFile = open(fileName, 'r')
    fileData = json.loads(collectionFile.read())
    itemData = fileData['items']

    itemArr = []
    for value in itemData:
        item = ItemFactory.factory(
            fileData['collectionType'],
            value.values()
        )
        itemArr.append(item)

    collection = Collection(fileData['collectionType'], fileData['collectionName'], fileData['username'], itemArr)
    for item in collection.items:
        print(item.id)


def updateCollection(collection, item, fileName):
    collection.items.append(item)
    getCollection(fileName)

if __name__ == '__main__':
    main()
