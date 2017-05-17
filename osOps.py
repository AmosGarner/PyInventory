import os

def createDirectory(directoryPath):
    if os.path.isdir(directoryPath) is False and os.path.exists(directoryPath) is False:
        try:
            os.makedirs(directoryPath)
        except OSError:
            print 'Error: Could not create directory at location: ' + directoryPath

def createFile(filePath):
    try:
        createdFile = open(filePath, 'w+')
        createdFile.close()
    except IOError:
        print "Error: could not create file at location: " + filePath

def getFileContents(filePath):
    return None

def deleteFile(filePath):
    return None

def deleteDirectory(directoryPath):
    return None
