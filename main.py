from createCollection import createCollectionFile
from updateCollection import updateCollection, getCollectionLength
from ObjectFactories.ItemFactory import ItemFactory
from DataObjects.Collection import Collection
import datetime, json, os.path, argparse

CONST_COLLECTIONS_NAME = 'collections'

def generateArgumentsFromParser():
    parser = parser = argparse.ArgumentParser(description="Runs the PyInventory utility for creating a collection of items.")
    parser.add_argument('--action', dest='action', required=True)
    parser.add_argument('--user', dest='username', required=True)
    parser.add_argument('--name', dest='collectionName', required=True)
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

def main():
        arguments = generateArgumentsFromParser()
        collectionFilePath = generateFileName(arguments.username, arguments.collectionName)

        if arguments.action.lower() == "create":
            createCollectionFile(arguments.username, arguments.collectionName)
            writeCollectionDataToFile(collectionFilePath, arguments)

        elif arguments.action.lower() == "update":
            collectionLength = getCollectionLength(collectionFilePath)
            itemDataArr = arguments.itemData.split('~')
            if arguments.collectionType.lower() == "item":
                updateCollection(collectionFilePath, ItemFactory.factory(arguments.collectionType, [collectionLength+1, itemDataArr[0], "date", "date"]))
            else:
                updateCollection(collectionFilePath, ItemFactory.factory(arguments.collectionType, [collectionLength+1, itemDataArr[0], "date", "date", itemDataArr[1]]))

if __name__ == '__main__':
    main()
