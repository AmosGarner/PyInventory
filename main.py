from updateCollection import updateCollection, getCollectionLength
from removeCollection import removeCollection
from editCollection import editCollection
from ObjectFactories.ItemFactory import ItemFactory
from DataObjects.Collection import Collection
from osOps import *
from collectionOps import *
import datetime, json, os, argparse

CONST_COLLECTIONS_NAME = 'collections'

def generateArgumentsFromParser():
    parser = parser = argparse.ArgumentParser(description="Runs the PyInventory utility for creating a collection of items.")
    parser.add_argument('--action', dest='action', required=True)
    parser.add_argument('--user', dest='username', required=False)
    parser.add_argument('--name', dest='collectionName', required=False)
    parser.add_argument('--type', dest='collectionType', required=False)
    parser.add_argument('--input', dest='inputData', required=False)
    return parser.parse_args()

def generateFileName(username, collectionName):
    return CONST_COLLECTIONS_NAME + "/" + username + "/" + username + "_" + collectionName + "_collection.dat"

def generateNewCollection(username, collectionType, collectionName):
    return Collection(username, collectionType, collectionName, [])

def installCollectionsDirectory(username):
    createDirectory(CONST_COLLECTIONS_NAME + '/' + username)

def main():
        arguments = generateArgumentsFromParser()

        if arguments.action.lower() == "install":
            installCollectionsDirectory(arguments.username)
            return None
        #placed this code here because I want this to run only if the user is not installing the program directories.
        collectionFilePath = generateFileName(arguments.username, arguments.collectionName)

        if arguments.action.lower() == "create_collection":
            baseCollection = Collection(arguments.username, arguments.collectionName, arguments.collectionType)
            writeCollectionToFile(collectionFilePath, baseCollection)

        elif arguments.action.lower() == "edit_collection":
            editCollection(collectionFilePath, arguments.inputData)

        elif arguments.action.lower() == "insert_item":
            collectionLength = len(getCollection(collectionFilePath).items)
            dateTime = datetime.datetime.now()

            if arguments.collectionType.lower() == "item":
                updateCollection(collectionFilePath, ItemFactory.factory(arguments.collectionType, [collectionLength+1, arguments.inputData, str(dateTime), str(dateTime)]))
            else:
                inputDataArr = arguments.inputData.split('~')
                updateCollection(collectionFilePath, ItemFactory.factory(arguments.collectionType, [collectionLength+1, inputDataArr[0], str(dateTime), str(dateTime), inputDataArr[1]]))

        elif arguments.action.lower() == "remove_collection":
            removeFile(collectionFilePath)

if __name__ == '__main__':
    main()
