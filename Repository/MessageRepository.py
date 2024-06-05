from Class.Message import Message

class MessageRepository:
    def __init__(self):
        self.messages = []

    def add_message(self, message: Message):
        self.messages.append(message)

    def get_message(self, message_id: int):
        for message in self.messages:
            if message.message_id == message_id:
                return message
        return None
