# models/gift.py

from datetime import datetime

class Gift:
    def __init__(self, id, name, value, timestamp=None):
        self.id = id
        self.name = name
        self.value = value
        self.timestamp = timestamp if timestamp is not None else datetime.now()
