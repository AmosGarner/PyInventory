from osOps import getFileContents
from DataObjects.Collection import Collection
from ObjectFactories.ItemFactory import ItemFactory
import json
import datetime

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

def editCollection(collection, collectionFilePath, newCollectionName):
    collection.collectionName = newCollectionName

    pathArr = collectionFilePath.split('/')
    fileNameArr = pathArr[2].split('_')
    fileNameArr[1] = newCollectionName
    newFileName = '_'.join(fileNameArr)
    newCollectionFilePath = pathArr[0] + '/' + pathArr[1] + '/' + newFileName

    writeCollectionToFile(newCollectionFilePath, collection)

def displayCollection(collection):
    print '|-----------------------------------------------------------'
    print '|    Collection Name: ' + collection.collectionName
    print '|    Created By: ' + collection.username
    print '|    Item Types: ' + collection.collectionType
    print '|    Number of Items: ' + str(len(collection.items))
    print '|-----------------------------------------------------------'
    print '|    Items:'
    if len(collection.items) >= 1:
        for item in collection.items:
            print '|==========================================================='
            print '|        ' + str(item.id) + '). ' + item.name
            print '|            Added On: ' + item.addedOn
            print '|            Last Edited: ' + item.lastEdit
            if collection.collectionType == 'book':
                print '|            Author: ' + item.author
            elif collection.collectionType == 'movie':
                print '|            Director: ' + item.director
            elif collection.collectionType == 'album':
                print '|            Artist: ' + item.artist
            print '|==========================================================='

    print '|-----------------------------------------------------------'
    return None
