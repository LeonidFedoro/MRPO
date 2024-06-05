import unittest
from datetime import datetime, timedelta

from models.gift import Gift
from models.user import User
from models.message import Message
from models.chat import Chat
from repositories.user_repository import UserRepository
from repositories.pair_repository import PairRepository
from repositories.message_repository import MessageRepository
from repositories.chat_repository import ChatRepository
from repositories.gift_repository import GiftRepository
from services.dating_service import DatingService

class TestDatingService(unittest.TestCase):

    def setUp(self):
        self.user_repo = UserRepository()
        self.pair_repo = PairRepository()
        self.message_repo = MessageRepository()
        self.chat_repo = ChatRepository()
        self.gift_repo = GiftRepository()
        self.service = DatingService(self.user_repo, self.pair_repo, self.message_repo, self.chat_repo, self.gift_repo)
        self.user1 = User(id=1, username="user1", email="user1@example.com")
        self.user2 = User(id=2, username="user2", email="user2@example.com")
        self.chat = Chat(id=1, participants=[self.user1, self.user2])

    def test_can_send_message(self):
        self.assertTrue(self.service.can_send_message(self.user1, self.user2, self.chat))

    def test_can_send_gift(self):
        self.assertTrue(self.service.can_send_gift(self.user1, self.user2))

    def test_create_pair(self):
        self.assertTrue(self.service.create_pair(self.user1, self.user2))

    def test_can_send_message_frequency(self):
        self.message_repo.messages = [
            Message(sender=self.user1, receiver=self.user2, content="Hi", timestamp=datetime.now() - timedelta(seconds=10))
            for _ in range(4)
        ]
        self.assertTrue(self.service.can_send_message_frequency(self.user1))
        self.message_repo.add_message(Message(sender=self.user1, receiver=self.user2, content="Hi", timestamp=datetime.now()))
        self.assertFalse(self.service.can_send_message_frequency(self.user1))

    def test_can_add_to_chat(self):
        self.assertTrue(self.service.can_add_to_chat(self.chat))
        self.chat.participants = [self.user1 for _ in range(50)]
        self.assertFalse(self.service.can_add_to_chat(self.chat))

    def test_can_send_gift_frequency(self):
        self.gift_repo.gifts = [
            Gift(id=i, name="Gift", value=10.0, timestamp=datetime.now() - timedelta(hours=1))
            for i in range(9)
        ]
        self.assertTrue(self.service.can_send_gift_frequency(self.user1))
        self.gift_repo.add_gift(Gift(id=10, name="Gift", value=10.0, timestamp=datetime.now()))
        self.assertFalse(self.service.can_send_gift_frequency(self.user1))

if __name__ == '__main__':
    unittest.main()
