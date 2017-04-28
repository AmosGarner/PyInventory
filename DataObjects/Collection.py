import json

class Collection:
    def __init__(self, collectionType, collectionName, username, items):
        self.collectionType = collectionType
        self.collectionName = collectionName
        self.username = username
        self.items = items

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
