class ChatRepository:
    def __init__(self):
        self.chats = []

    def add_chat(self, chat):
        self.chats.append(chat)

    def get_chats(self):
        return self.chats
