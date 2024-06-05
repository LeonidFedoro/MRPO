from datetime import datetime
from Class.User import User

class Message:
    def __init__(self, message_id: int, sender: User, receiver: User, content: str, timestamp: datetime):
        self.message_id = message_id
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = timestamp
