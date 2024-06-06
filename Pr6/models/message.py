from dataclasses import dataclass
from datetime import datetime
from models.user import User

@dataclass
class Message:
    sender: User
    receiver: User
    content: str
    timestamp: datetime
