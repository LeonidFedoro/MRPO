from Class.User import User

class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def get_user(self, user_id: int):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
