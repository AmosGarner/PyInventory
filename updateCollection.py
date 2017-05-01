from DataObjects.Collection import Collection
from ObjectFactories.ItemFactory import ItemFactory
import json

def updateCollection(fileName, item):
    collection = getCollection(fileName)
    collection.items.append(item)
    writeCollectionToFile(fileName, collection)

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

def getCollectionLength(fileName):
    collectionLength = len(getCollection(fileName).items)
    if collectionLength <= 0:
        return 0
    else:
        return collectionLength

def writeCollectionToFile(fileName, collection):
    collectionFile = open(fileName, 'w')
    collectionFile.write(collection.toJSON())
    collectionFile.close()
