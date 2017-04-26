from DataObjects.movie import Movie

class MovieFactory(object):
    def __init__(self):
        return False

    @staticmethod
    def createMovie(name, addedOn, lastEdit, director):
        return Movie(name, addedOn, lastEdit, director)
