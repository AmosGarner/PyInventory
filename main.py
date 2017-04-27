from createCollection import createCollection
from ObjectFactories.ItemFactory import ItemFactory
from DataObjects.Collection import Collection
import datetime, json, os.path, argparse

CONST_COLLECTIONS_NAME = 'collections'

def generateArgumentsFromParser():
    parser = parser = argparse.ArgumentParser(description="Runs the PyInventory utility for creating a collection of items.")
    parser.add_argument('--user', dest='username', required=True)
    parser.add_argument('--type', dest='collectionType', required=True)
    parser.add_argument('--name', dest='collectionName', required=True)
    parser.add_argument('--length', dest='length', required=True)
    return parser.parse_args()

def generateCollection(collectionType, collectionName, username, length):
    items = []
    now = datetime.datetime.now()

    if collectionType.lower() == 'item':
        for i in range(0,length):
            item = ItemFactory.factory('item', [i, 'item' + str(i), now, now])
            items.append(item)

    return Collection(collectionName, username, items)

def main():
        arguments = generateArgumentsFromParser()

        createCollection(arguments.username, arguments.collectionName)
        itemCollection = generateCollection('item', arguments.collectionName, arguments.username, int(arguments.length))

        collectionsFilePath = CONST_COLLECTIONS_NAME+'/'+arguments.username+'_'+CONST_COLLECTIONS_NAME+'/'+arguments.username+'_'+arguments.collectionName+'_'+'collection.dat'

        if os.path.isfile(collectionsFilePath):
            collectionFile = open(collectionsFilePath, 'w')
            collectionFile.write(itemCollection.toJSON())
            collectionFile.close()

if __name__ == '__main__':
    main()
