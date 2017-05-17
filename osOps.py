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

def openFile(filePath):
    try:
        fileEntity = open(filePath, 'r')
        return fileEntity
    except IOError:
        print "Error: could not open file at location: " + filePath
        return False

def removeFile(filePath):
    try:
        os.remove(filePath)
    except OSError:
        print "Error: could not remove file at location: " + filePath

def removeDirectory(directoryPath):
    try:
        os.removedirs(directoryPath)
    except OSError:
        print "Error: could not remove directory at location: " + directoryPath

def getFileContents(filePath):
    try:
        fileData = openFile(filePath).read()
        return fileData
    except IOError:
        print "Error: could find file data located in file at location: " + filePath
        return False
