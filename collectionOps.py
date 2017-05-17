from osOps import getFileContents
from DataObjects.Collection import Collection
from ObjectFactories.ItemFactory import ItemFactory
import json

def getCollection(filePath):
    try:
        fileData = getFileContents(filePath)
        fileJSON = json.loads(fileData)
        return generateCollectionOnFileData(fileJSON)
    except:
        print('Error: Could not load collection data from file.')

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

def writeCollectionToFile(collectionFilePath, collection):
    collectionFile = open(collectionFilePath, 'w+')
    collectionFile.write(collection.toJSON())
    collectionFile.close()
