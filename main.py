from createCollection import createCollection
from ObjectFactories.ItemFactory import ItemFactory
from DataObjects.Collection import Collection
import datetime
import json

def main():
        #createCollection('agarner','books')
        now = datetime.datetime.now()
        items = []
        for i in range(0,10):
            item = ItemFactory.factory('item', [i, 'item' + str(i), now, now])
            print(item.name)
            items.append(item)
        itemCollection = Collection('Items', 'agarner', items)
        print itemCollection.toJSON()

if __name__ == '__main__':
    main()
