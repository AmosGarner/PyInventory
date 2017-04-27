from Item import Item

class Album(Item) :
    def __init__(self, name, addedOn, lastEdit, artist):
        Item.__init__(self, name, addedOn, lastEdit)
        self.artist = artist
