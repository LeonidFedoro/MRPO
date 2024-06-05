from datetime import datetime
from Class.User import User

class Gift:
    def __init__(self, gift_id: int, sender: User, receiver: User, gift_type: str, timestamp: datetime):
        self.gift_id = gift_id
        self.sender = sender
        self.receiver = receiver
        self.gift_type = gift_type
        self.timestamp = timestamp
