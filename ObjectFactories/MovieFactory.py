from DataObjects.movie import Movie

class movieFactory(object):
    def __init__(self):
        return False

    @staticmethod
    def createmovie(name, addedOn, lastEdit, director):
        return movie(name, addedOn, lastEdit, director)
