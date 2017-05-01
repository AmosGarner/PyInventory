import json

class Collection:
    def __init__(self, username, collectionName, collectionType, items = []):
        self.username = username
        self.collectionName = collectionName
        self.collectionType = collectionType
        self.items = items

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
