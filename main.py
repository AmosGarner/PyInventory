from createCollection import createCollection
from ObjectFactories.ItemFactory import ItemFactory
from DataObjects.Collection import Collection
import datetime, json, os.path, argparse

CONST_COLLECTIONS_NAME = 'collections'

def generateArgumentsFromParser():
    parser = parser = argparse.ArgumentParser(description="Runs the PyInventory utility for creating a collection of items.")
    parser.add_argument('--action', dest='action', required=True)
    parser.add_argument('--user', dest='username', required=True)
    parser.add_argument('--type', dest='collectionType', required=True)
    parser.add_argument('--name', dest='collectionName', required=False)
    return parser.parse_args()

def generateFileName(username, collectionName):
    return CONST_COLLECTIONS_NAME + "/"
    + username + "_" + CONST_COLLECTIONS_NAME + "/"
    + username + "_" + collectionName + "_collection.dat"

def main():
        arguments = generateArgumentsFromParser()

        if arguments.action.lower() == "create":
            print generateFileName(arguments.username, arguments.collectionName)
            createCollection(arguments.username, arguments.collectionName)

if __name__ == '__main__':
    main()
