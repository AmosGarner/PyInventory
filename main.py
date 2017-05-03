from createCollection import createCollectionFile
from updateCollection import updateCollection, getCollectionLength
from removeCollection import removeCollection
from ObjectFactories.ItemFactory import ItemFactory
from DataObjects.Collection import Collection
import datetime, json, os, argparse

CONST_COLLECTIONS_NAME = 'collections'

def generateArgumentsFromParser():
    parser = parser = argparse.ArgumentParser(description="Runs the PyInventory utility for creating a collection of items.")
    parser.add_argument('--action', dest='action', required=True)
    parser.add_argument('--user', dest='username', required=False)
    parser.add_argument('--name', dest='collectionName', required=False)
    parser.add_argument('--type', dest='collectionType', required=False)
    parser.add_argument('--input', dest='itemData', required=False)
    return parser.parse_args()

def generateFileName(username, collectionName):
    return CONST_COLLECTIONS_NAME + "/" + username + "_" + CONST_COLLECTIONS_NAME + "/" + username + "_" + collectionName + "_collection.dat"

def generateNewCollection(username, collectionType, collectionName):
    return Collection(username, collectionType, collectionName, [])

def writeCollectionDataToFile(collectionFilePath, arguments):
    collection = generateNewCollection(arguments.username, arguments.collectionName, arguments.collectionType)
    collectionFile = open(collectionFilePath, 'w')
    collectionFile.write(collection.toJSON())
    collectionFile.close()

def createCollectionsDirectory():
    if os.path.isdir(CONST_COLLECTIONS_NAME) is False and os.path.exists(CONST_COLLECTIONS_NAME) is False:
        try:
            os.makedirs(CONST_COLLECTIONS_NAME)
        except:
            print 'Error: Could not create directory: %s' %(collectionsName)

def main():
        arguments = generateArgumentsFromParser()

        if arguments.action.lower() == "install":
            createCollectionsDirectory()
            return None

        collectionFilePath = generateFileName(arguments.username, arguments.collectionName)

        if arguments.action.lower() == "create_collection":
            createCollectionFile(arguments.username, arguments.collectionName)
            writeCollectionDataToFile(collectionFilePath, arguments)

        elif arguments.action.lower() == "insert_item":
            collectionLength = getCollectionLength(collectionFilePath)
            itemDataArr = arguments.itemData.split('~')
            dateTime = datetime.datetime.now()
            if arguments.collectionType.lower() == "item":
                updateCollection(collectionFilePath, ItemFactory.factory(arguments.collectionType, [collectionLength+1, itemDataArr[0], str(dateTime), str(dateTime)]))
            else:
                updateCollection(collectionFilePath, ItemFactory.factory(arguments.collectionType, [collectionLength+1, itemDataArr[0], str(dateTime), str(dateTime), itemDataArr[1]]))

        elif arguments.action.lower() == "remove_collection":
            removeCollection(collectionFilePath)

if __name__ == '__main__':
    main()
