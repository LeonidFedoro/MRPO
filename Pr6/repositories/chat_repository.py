from repositories.base_repository import BaseRepository
from models.chat import Chat

class ChatRepository(BaseRepository):
    def __init__(self):
        self.chats = []

    def add(self, chat: Chat):
        self.chats.append(chat)

    def get(self, id: int) -> Chat:
        for chat in self.chats:
            if chat.id == id:
                return chat
        return None

    def update(self, chat: Chat):
        for idx, c in enumerate(self.chats):
            if c.id == chat.id:
                self.chats[idx] = chat

    def delete(self, id: int):
        self.chats = [chat for chat in self.chats if chat.id != id]
