class Message:
    def __init__(self, sender, receiver, content, timestamp):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = timestamp

    def __eq__(self, other):
        if not isinstance(other, Message):
            return NotImplemented
        return (self.sender == other.sender and
                self.receiver == other.receiver and
                self.content == other.content and
                self.timestamp == other.timestamp)
