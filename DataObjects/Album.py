from Item import Item

class Album(Item) :
    def __init__(self, itemId, name, addedOn, lastEdit, artist):
        Item.__init__(self, itemId, name, addedOn, lastEdit)
        self.artist = artist
