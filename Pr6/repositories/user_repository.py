from repositories.base_repository import BaseRepository
from models.user import User

class UserRepository(BaseRepository):
    def __init__(self):
        self.users = []

    def add(self, user: User):
        self.users.append(user)

    def get(self, id: int) -> User:
        for user in self.users:
            if user.id == id:
                return user
        return None

    def update(self, user: User):
        for idx, u in enumerate(self.users):
            if u.id == user.id:
                self.users[idx] = user

    def delete(self, id: int):
        self.users = [user for user in self.users if user.id != id]
