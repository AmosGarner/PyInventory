from DataObjects.Collection import Collection
from ObjectFactories.ItemFactory import ItemFactory
import os

def main():
    updateCollection(
        Collection('items', 'agarner', []),
        ItemFactory.factory('item', [0, 'someItem', 'date', 'date']),
        'collections/agarner_collections/agarner_items_collection.dat'
    )

def updateCollection(collection, item, fileName):
    collection.items.append(item)
    for item in collection.items:
        print item.name

if __name__ == '__main__':
    main()
