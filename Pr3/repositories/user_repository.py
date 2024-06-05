class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, user_id):
        return next((user for user in self.users if user.id == user_id), None)
