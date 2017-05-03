import os

CONST_COLLECTIONS_NAME = 'collections'

def createCollectionFile(collectionFilePath):
    generateCollectionFile(collectionFilePath)

def generateCollectionFile(collectionFilePath):
    try:
        collectionFile = open(collectionFilePath, 'w+')
        collectionFile.close()
    except IOError:
        print 'Error: collection file could not be created at: ' + collectionFilePath
