from DataObjects.Album import Album
from DataObjects.Book import Book
from DataObjects.Movie import Movie
from DataObjects.Item import Item

class ItemFactory:

    def factory(type, itemAttributes):
        if type == 'album':
            return Album(itemAttributes[0], itemAttributes[1], itemAttributes[2], itemAttributes[3], itemAttributes[4])
        elif type == 'book':
            return Book(itemAttributes[0], itemAttributes[1], itemAttributes[2], itemAttributes[3], itemAttributes[4])
        elif type == 'movie':
            return Movie(itemAttributes[0], itemAttributes[1], itemAttributes[2], itemAttributes[3], itemAttributes[4])
        elif type == 'item':
            return Item(itemAttributes[0], itemAttributes[1], itemAttributes[2], itemAttributes[3])
    factory = staticmethod(factory)
