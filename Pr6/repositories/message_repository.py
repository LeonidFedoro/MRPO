from repositories.base_repository import BaseRepository
from models.message import Message

class MessageRepository(BaseRepository):
    def __init__(self):
        self.messages = []

    def add(self, message: Message):
        self.messages.append(message)

    def get(self, id: int) -> Message:
        for message in self.messages:
            if message.id == id:
                return message
        return None

    def update(self, message: Message):
        for idx, m in enumerate(self.messages):
            if m.id == message.id:
                self.messages[idx] = message

    def delete(self, id: int):
        self.messages = [message for message in self.messages if message.id != id]
