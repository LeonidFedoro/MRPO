from typing import List
from Class.User import User
from Class.Message import Message

class Chat:
    def __init__(self, chat_id: int, participants: List[User]):
        self.chat_id = chat_id
        self.participants = participants
        self.messages = []

    def add_message(self, message: Message):
        self.messages.append(message)
