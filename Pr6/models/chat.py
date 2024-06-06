from dataclasses import dataclass
from models.user import User
from typing import List

@dataclass
class Chat:
    id: int
    participants: List[User]
