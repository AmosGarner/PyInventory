import os

CONST_COLLECTIONS_NAME = 'collections'

def createCollectionFile(username, collectionName):
    createCollectionsDirectory(CONST_COLLECTIONS_NAME)
    collectionPath = createCollectionDirectory(username)
    generateCollectionFile(collectionPath, username, collectionName)

def createCollectionsDirectory(collectionsName):
    if os.path.isdir(collectionsName) is False and os.path.exists(collectionsName) is False:
        try:
            os.makedirs(collectionsName)
        except:
            print 'Error: Could not create directory: %s' %(collectionsName)

def createCollectionDirectory(username):
    collectionPath = CONST_COLLECTIONS_NAME+'/'+username+'_collections'
    if os.path.isdir(collectionPath) is False and os.path.exists(collectionPath) is False:
        try:
            os.makedirs(collectionPath)
        except OSError:
            print 'Error: Could not create collections directory for user: %s' %(username)
    return collectionPath

def generateCollectionFile(collectionPath, username, collectionName):
    try:
        collectionFile = open(collectionPath+'/'+username+'_'+collectionName+'_collection.dat', 'w+')
        collectionFile.close()
    except IOError:
        print 'Error: file %s could not be created.' % (collectionPath+'/'+username+'_'+collectionName+'_collection.dat')
