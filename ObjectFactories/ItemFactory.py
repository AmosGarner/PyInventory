from DataObjects.item import Item

class ItemFactory(object):
    def __init__(self):
        return False

    @staticmethod
    def createItem(name, addedOn, lastEdit):
        return Item(name, addedOn, lastEdit)
