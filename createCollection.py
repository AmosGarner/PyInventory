import argparse, os

CONST_COLLECTIONS_NAME = 'collections'

def main():
    createCollection('agarner', 'books')


def createCollection(username, fileName):

    createCollectionsDirectory(CONST_COLLECTIONS_NAME)
    createCollectionDirectory(username)

    # try:
    #     f = open(arguments.collection_name +".dat", 'r')
    #     print f
    # except IOError:
    #     print 'Error: file %s no found.' % (arguments.collection_name)
    #     fileCreateInput = raw_input('Would you like to create it? (y/n) ')
    #     if fileCreateInput.lower() == 'y' or fileCreateInput.lower() == 'yes':
    #         try:
    #             f = open(arguments.collection_name+'.dat', 'w+')
    #             f.close()
    #         except:
    #             print 'Error: file %s could not be created.' % (arguments.collection_name)
    #             print 'Exiting Program'

def createCollectionsDirectory(collectionsName):
    if os.path.isdir(collectionsName) is False and os.path.exists(collectionsName) is False:
        try:
            os.makedirs(collectionsName)
        except:
            print 'Error: Could not create directory: %s' %(collectionsName)

def createCollectionDirectory(username):
    collectionsPath = CONST_COLLECTIONS_NAME+'/'+username+'_collections'
    if os.path.isdir(collectionsPath) is False and os.path.exists(collectionsPath) is False:
        try:
            os.makedirs(collectionPath)
        except:
            print 'Error: Could not create collections directory for user: %s' %(username)

def createCollectionFile(fileName):
    return False

if __name__ == '__main__':
    main()
