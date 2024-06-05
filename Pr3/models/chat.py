class Chat:
    def __init__(self, id, participants):
        self.id = id
        self.participants = participants

    def __eq__(self, other):
        if not isinstance(other, Chat):
            return NotImplemented
        return (self.id == other.id and
                self.participants == other.participants)
