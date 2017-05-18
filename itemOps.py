def insertItem(collection, item):
    collection.items.append(item)
    return collection

def editItem(collection, itemId, itemData):
    return collection

def removeItem(collection, itemId):
    collectionLength = len(collection.items)
    itemsIndex = 0;
    for item in collection.items:
        if int(item.id) == itemId:
            del collection.items[itemsIndex]
        itemsIndex += 1
    return collection
