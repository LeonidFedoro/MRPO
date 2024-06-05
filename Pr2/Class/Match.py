from datetime import datetime
from Class.User import User

class Match:
    def __init__(self, match_id: int, user1: User, user2: User, match_date: datetime):
        self.match_id = match_id
        self.user1 = user1
        self.user2 = user2
        self.match_date = match_date
