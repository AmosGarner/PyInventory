from DataObjects.Collection import Collection
from ObjectFactories.ItemFactory import ItemFactory
from collections import OrderedDict
import json

def main():
    collectionFileName = 'collections/agarner_collections/agarner_Item_collection.dat'
    item = ItemFactory.factory('item', [0, 'someItem', 'date', 'date'])
    updateCollection(collectionFileName, item)

def getCollection(fileName):
    collectionFile = open(fileName, 'r')
    fileData = json.loads(collectionFile.read())
    collectionFile.close()

    collectionType = fileData['collectionType']
    collectionName = fileData['collectionName']
    username = fileData['username']
    itemData = fileData['items']

    itemArr = []
    for value in itemData:
        if fileData['collectionType'] == 'item':
            item = ItemFactory.factory(collectionType,[value['id'], value['name'], value['addedOn'], value['lastEdit']])
            itemArr.append(item)
        elif fileData['collectionType'] == 'album':
            item = ItemFactory.factory(collectionType,[value['id'], value['name'], value['addedOn'], value['lastEdit'], value['artist']])
            itemArr.append(item)
        elif fileData['collectionType'] == 'book':
            item = ItemFactory.factory(collectionType,[value['id'], value['name'], value['addedOn'], value['lastEdit'], value['author']])
            itemArr.append(item)
        elif fileData['collectionType'] == 'movie':
            item = ItemFactory.factory(collectionType,[value['id'], value['name'], value['addedOn'], value['lastEdit'], value['director']])
            itemArr.append(item)

    return Collection(fileData['collectionType'], fileData['collectionName'], fileData['username'], itemArr)

def writeCollectionToFile(fileName, collection):
    collectionFile = open(fileName, 'w')
    collectionFile.write(collection.toJSON())
    collectionFile.close()


def updateCollection(fileName, item):
    collection = getCollection(fileName)
    collection.items.append(item)
    writeCollectionToFile(fileName, collection)


if __name__ == '__main__':
    main()
