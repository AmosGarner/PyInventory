from Item import Item

class Book(Item) :
    def __init__(self, name, addedOn, lastEdit, author):
        Item.__init__(self, name, addedOn, lastEdit)
        self.author = author
