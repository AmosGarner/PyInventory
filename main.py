from createCollection import createCollection
from ObjectFactories.ItemFactory import ItemFactory
from DataObjects.Collection import Collection
import datetime, json, os.path, argparse

CONST_COLLECTIONS_NAME = 'collections'

def generateArgumentsFromParser():
    parser = parser = argparse.ArgumentParser(description="Runs PyTriSearch googling utility.")
    return parser.parse_args()

def generateItemsCollection(collectionName, username):
    items = []
    now = datetime.datetime.now()
    for i in range(0,10):
        item = ItemFactory.factory('item', [i, 'item' + str(i), now, now])
        print(item.name)
        items.append(item)
    return Collection(collectionName, username, items)

def main():
        arguments = generateArgumentsFromParser()

        username = 'agarner'
        collectionName = 'Items'

        createCollection(username,collectionName)
        itemCollection = generateItemsCollection(collectionName, username)

        collectionsFilePath = CONST_COLLECTIONS_NAME+'/'+username+'_'+CONST_COLLECTIONS_NAME+'/'+username+'_'+collectionName+'_'+'collection.dat'
        if os.path.isfile(collectionsFilePath):
            collectionFile = open(collectionsFilePath, 'w')
            collectionFile.write(itemCollection.toJSON())
            collectionFile.close()



if __name__ == '__main__':
    main()
