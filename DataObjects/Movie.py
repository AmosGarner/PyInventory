from Item import Item

class Movie(Item) :
    def __init__(self, itemId, name, addedOn, lastEdit, director):
        Item.__init__(self, itemId, name, addedOn, lastEdit)
        self.director = director
