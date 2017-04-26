from DataObjects.album import Album

class AlbumFactory(object):
    def __init__(self):
        return False

    @staticmethod
    def createAlbum(name, addedOn, lastEdit, artist):
        return Album(name, addedOn, lastEdit, artist)
