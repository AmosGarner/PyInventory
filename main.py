from ObjectFactories.ItemFactory import ItemFactory
from osOps import *
from collectionOps import *
from itemOps import *
import datetime, argparse

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

def installCollectionsDirectory(username):
    createDirectory(CONST_COLLECTIONS_NAME + '/' + username)

def main():
        arguments = generateArgumentsFromParser()

        if arguments.action.lower() == "install":
            installCollectionsDirectory(arguments.username)
            return None

        collectionFilePath = generateFileName(arguments.username, arguments.collectionName)

        if arguments.action.lower() == "create_collection":
            baseCollection = Collection(arguments.username, arguments.collectionName, arguments.collectionType)
            writeCollectionToFile(collectionFilePath, baseCollection)

        elif arguments.action.lower() == "edit_collection":
            collection = getCollection(collectionFilePath)
            removeFile(collectionFilePath)
            editCollection(collection, collectionFilePath, arguments.inputData)

        elif arguments.action.lower() == "remove_collection":
            removeFile(collectionFilePath)

        elif arguments.action.lower() == "insert_item":
            collectionLength = len(getCollection(collectionFilePath).items)
            dateTime = datetime.datetime.now()

            if arguments.collectionType.lower() == "item":
                newItem = ItemFactory.factory(arguments.collectionType, [collectionLength+1, arguments.inputData, str(dateTime), str(dateTime)])
                collection = insertItem(getCollection(collectionFilePath), newItem)
            else:
                inputDataArr = arguments.inputData.split('~')
                newItem = ItemFactory.factory(arguments.collectionType, [collectionLength+1, inputDataArr[0], str(dateTime), str(dateTime), inputDataArr[1]])
                collection = insertItem(getCollection(collectionFilePath), newItem)

            writeCollectionToFile(collectionFilePath, collection)



if __name__ == '__main__':
    main()
