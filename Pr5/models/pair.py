from dataclasses import dataclass
from models.user import User

@dataclass
class Pair:
    user1: User
    user2: User
