import json

class JsonRepository:
    def __init__(self, filename):
        self.filename = filename

    def save_all(self, items):
        with open(self.filename, 'w') as file:
            json.dump([item.to_dict() for item in items], file)

    def load_all(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [self.from_dict(item) for item in data]
        except FileNotFoundError:
            return []

    def from_dict(self, item_dict):
        raise NotImplementedError("Must be implemented in subclasses")

    def add(self, item):
        items = self.load_all()
        items.append(item)
        self.save_all(items)

    def get(self, id):
        items = self.load_all()
        for item in items:
            if item.id == id:
                return item
        return None
