from updateCollection import getCollection

def editCollection(collectionFilePath, newCollectionName):
    Collection = getCollection(collectionFilePath)
    print(newCollectionName)
