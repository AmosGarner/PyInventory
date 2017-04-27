from DataObjects.Album import Album
from DataObjects.Book import Book
from DataObjects.Movie import Movie
from DataObjects.Item import Item

class ItemFactory:

    def factory(objectType, itemAttributes):
        objectType = objectType.lower()
        if objectType == 'album':
            return Album(itemAttributes[0], itemAttributes[1], itemAttributes[2], itemAttributes[3], itemAttributes[4])
        elif objectType == 'book':
            return Book(itemAttributes[0], itemAttributes[1], itemAttributes[2], itemAttributes[3], itemAttributes[4])
        elif objectType == 'movie':
            return Movie(itemAttributes[0], itemAttributes[1], itemAttributes[2], itemAttributes[3], itemAttributes[4])
        elif objectType == 'item':
            return Item(itemAttributes[0], itemAttributes[1], itemAttributes[2], itemAttributes[3])
    factory = staticmethod(factory)
