from createCollection import createCollectionFile
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
    return parser.parse_args()

def generateFileName(username, collectionName):
    return CONST_COLLECTIONS_NAME + "/" + username + "_" + CONST_COLLECTIONS_NAME + "/" + username + "_" + collectionName + "_collection.dat"

def generateNewCollection(username, collectionType, collectionName):
    return Collection(username, collectionType, collectionName, [])

def writeCollectionToFile(collectionFileName, arguments):
    collection = generateNewCollection(arguments.username, arguments.collectionType, arguments.collectionName)
    collectionFile = open(collectionFileName, 'w')
    collectionFile.write(collection.toJSON())
    collectionFile.close()

def main():
        arguments = generateArgumentsFromParser()
        collectionFileName = generateFileName(arguments.username, arguments.collectionName)

        if arguments.action.lower() == "create":
            createCollectionFile(arguments.username, arguments.collectionName)
            writeCollectionToFile(collectionFileName, arguments)

        elif arguments.action.lower() == "update":
            return None

if __name__ == '__main__':
    main()
