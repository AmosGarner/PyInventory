from DataObjects.Collection import Collection
from ObjectFactories.ItemFactory import ItemFactory
import json

def updateCollection(collectionFilePath, item):
    collection = getCollection(collectionFilePath)
    collection.items.append(item)
    writeCollectionToFile(collectionFilePath, collection)

def getCollection(collectionFilePath):
    collectionFile = open(collectionFilePath, 'r')
    fileData = json.loads(collectionFile.read())
    collectionFile.close()

    return generateCollectionOnFileData(fileData)

def generateCollectionOnFileData(fileData):
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

    return Collection(fileData['username'], fileData['collectionName'], fileData['collectionType'], itemArr)

def getCollectionLength(collectionFilePath):
    collectionLength = len(getCollection(collectionFilePath).items)
    if collectionLength <= 0:
        return 0
    else:
        return collectionLength

def writeCollectionToFile(collectionFilePath, collection):
    collectionFile = open(collectionFilePath, 'w')
    collectionFile.write(collection.toJSON())
    collectionFile.close()
