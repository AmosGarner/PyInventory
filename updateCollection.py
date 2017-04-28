from DataObjects.Collection import Collection
from ObjectFactories.ItemFactory import ItemFactory
from collections import OrderedDict
import json

def main():
    updateCollection(
        Collection('item','Items', 'agarner', []),
        ItemFactory.factory('item', [0, 'someItem', 'date', 'date']),
        'collections/TestUser_collections/TestUser_album_collection.dat'
    )

def getCollection(fileName):
    collectionFile = open(fileName, 'r')
    fileData = json.loads(collectionFile.read())

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

    collection = Collection(fileData['collectionType'], fileData['collectionName'], fileData['username'], itemArr)

    print collection.collectionType
    print collection.collectionName
    print collection.username
    print collection.items


def updateCollection(collection, item, fileName):
    collection.items.append(item)
    getCollection(fileName)

if __name__ == '__main__':
    main()
