class Pair:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2

    def __eq__(self, other):
        if not isinstance(other, Pair):
            return NotImplemented
        return {self.user1, self.user2} == {other.user1, other.user2}
