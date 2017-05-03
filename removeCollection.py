import os

def removeCollection(collectionFilePath):
    try:
        os.remove(collectionFilePath)
    except OSError:
        print("Could not remove the collection at path: " + collectionFilePath)
