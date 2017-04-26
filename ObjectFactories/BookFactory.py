from DataObjects.book import Book

class BookFactory(object):
    def __init__(self):
        return False

    @staticmethod
    def createBook(name, addedOn, lastEdit, author):
        return Book(name, addedOn, lastEdit, author)
