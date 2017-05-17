import os

def createDirectory(directoryPath):
    return None

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
