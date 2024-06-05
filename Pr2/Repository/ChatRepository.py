from Class.Chat import Chat

class ChatRepository:
    def __init__(self):
        self.chats = []

    def add_chat(self, chat: Chat):
        self.chats.append(chat)

    def get_chat(self, chat_id: int):
        for chat in self.chats:
            if chat.chat_id == chat_id:
                return chat
        return None
