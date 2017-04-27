from createCollection import createCollection
from ObjectFactories.ItemFactory import ItemFactory
from DataObjects.Collection import Collection
import datetime, json, os.path

CONST_COLLECTIONS_NAME = 'collections'
CONST_USERNAME = 'agarner'
CONST_COLLECTION = 'Items'

def generateItemsCollection():
    items = []
    now = datetime.datetime.now()
    for i in range(0,10):
        item = ItemFactory.factory('item', [i, 'item' + str(i), now, now])
        print(item.name)
        items.append(item)
    return Collection(CONST_COLLECTION, CONST_USERNAME, items)

def main():
        createCollection(CONST_USERNAME,CONST_COLLECTION)
        itemCollection = generateItemsCollection()

        collectionsFilePath = CONST_COLLECTIONS_NAME+'/'+CONST_USERNAME+'_'+CONST_COLLECTIONS_NAME+'/'+CONST_USERNAME+'_'+CONST_COLLECTION+'_'+'collection.dat'
        if os.path.isfile(collectionsFilePath):
            collectionFile = open(collectionsFilePath, 'w')
            collectionFile.write(itemCollection.toJSON())
            collectionFile.close()



if __name__ == '__main__':
    main()
