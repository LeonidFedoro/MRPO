from repositories.user_repository import UserRepository
from repositories.pair_repository import PairRepository
from repositories.message_repository import MessageRepository
from repositories.chat_repository import ChatRepository
from repositories.gift_repository import GiftRepository
from services.dating_service import DatingService

class DatingUseCase:
    def __init__(self):
        self.user_repo = UserRepository()
        self.pair_repo = PairRepository()
        self.message_repo = MessageRepository()
        self.chat_repo = ChatRepository()
        self.gift_repo = GiftRepository()
        self.dating_service = DatingService(
            self.user_repo, self.pair_repo, self.message_repo, self.chat_repo, self.gift_repo
        )

    def add_user(self, user):
        self.user_repo.add_user(user)

    def get_user(self, user_id):
        return self.user_repo.get_user(user_id)

    def add_pair(self, pair):
        self.pair_repo.add_pair(pair)

    def get_pairs(self):
        return self.pair_repo.get_pairs()

    def add_message(self, message):
        self.message_repo.add_message(message)

    def get_messages(self):
        return self.message_repo.get_messages()

    def add_chat(self, chat):
        self.chat_repo.add_chat(chat)

    def get_chats(self):
        return self.chat_repo.get_chats()

    def add_gift(self, gift):
        self.gift_repo.add_gift(gift)

    def get_gifts(self):
        return self.gift_repo.get_gifts()

    def can_send_message(self, sender, receiver, chat):
        return self.dating_service.can_send_message(sender, receiver, chat)

    def can_send_gift(self, sender, receiver):
        return self.dating_service.can_send_gift(sender, receiver)

    def create_pair(self, user1, user2):
        return self.dating_service.create_pair(user1, user2)

    def can_send_message_frequency(self, sender):
        return self.dating_service.can_send_message_frequency(sender)

    def can_add_to_chat(self, chat):
        return self.dating_service.can_add_to_chat(chat)

    def can_send_gift_frequency(self, sender):
        return self.dating_service.can_send_gift_frequency(sender)
