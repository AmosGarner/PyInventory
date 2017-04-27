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
    objectArray = []
    now = datetime.datetime.now()

    if collectionType.lower() == 'item':
        for i in range(0,length):
            item = ItemFactory.factory('item', [i, 'item' + str(i), now, now])
            objectArray.append(item)
    elif collectionType.lower() == 'album':
        for i in range(0,length):
            item = ItemFactory.factory('album', [i, 'album' + str(i), now, now, 'artist_' + str(i)])
            objectArray.append(item)
    elif collectionType.lower() == 'book':
        for i in range(0,length):
            item = ItemFactory.factory('book', [i, 'book' + str(i), now, now, 'author_' + str(i)])
            objectArray.append(item)
    elif collectionType.lower() == 'movie':
        for i in range(0,length):
            item = ItemFactory.factory('movie', [i, 'movie' + str(i), now, now, 'movie_' + str(i)])
            objectArray.append(item)

    return Collection(collectionName, username, objectArray)

def main():
        arguments = generateArgumentsFromParser()

        createCollection(arguments.username, arguments.collectionName)
        itemCollection = generateCollection(arguments.collectionType.lower(), arguments.collectionName, arguments.username, int(arguments.length))

        collectionsFilePath = CONST_COLLECTIONS_NAME+'/'+arguments.username+'_'+CONST_COLLECTIONS_NAME+'/'+arguments.username+'_'+arguments.collectionName+'_'+'collection.dat'

        if os.path.isfile(collectionsFilePath):
            collectionFile = open(collectionsFilePath, 'w')
            collectionFile.write(itemCollection.toJSON())
            collectionFile.close()

if __name__ == '__main__':
    main()
