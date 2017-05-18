def insertItem(collection, item):
    collection.items.append(item)
    return collection

def editItem(collection, itemId, updatedItem):
    itemsIndex = 0;
    for item in collection.items:
        if int(item.id) == itemId:
            collection.items[itemsIndex].name = updatedItem.name
            collection.items[itemsIndex].lastEdit = updatedItem.lastEdit
            if collection.collectionType == 'book':
                collection.items[itemsIndex].author = updatedItem.author
            elif collection.collectionType == 'movie':
                collection.items[itemsIndex].director = updatedItem.director
            elif collection.collectionType == 'album':
                collection.items[itemsIndex].artist = updatedItem.artist
        itemsIndex += 1
    return collection

def removeItem(collection, itemId):
    collectionLength = len(collection.items)
    itemsIndex = 0;
    for item in collection.items:
        if int(item.id) == itemId:
            del collection.items[itemsIndex]
        itemsIndex += 1
    return collection
