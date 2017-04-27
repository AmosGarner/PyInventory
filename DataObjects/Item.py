import json

class Item:
    def __init__(self, itemId, name, addedOn, lastEdit):
        self.id = itemId
        self.name = name
        self.addedOn = str(addedOn)
        self.lastEdit = str(lastEdit)
