import unittest
from models.user import User
from models.pair import Pair
from models.message import Message
from models.chat import Chat
from models.gift import Gift
from use_case.dating_use_case import DatingUseCase
from datetime import datetime

class TestDatingUseCase(unittest.TestCase):
    def setUp(self):
        self.use_case = DatingUseCase()
        self.user1 = User(id=1, username="user1", email="user1@example.com")
        self.user2 = User(id=2, username="user2", email="user2@example.com")

    def test_add_user(self):
        self.use_case.add_user(self.user1)
        self.assertEqual(self.use_case.get_user(1), self.user1)

    def test_add_pair(self):
        self.use_case.add_user(self.user1)
        self.use_case.add_user(self.user2)
        pair = Pair(user1=self.user1, user2=self.user2)
        self.use_case.add_pair(pair)
        self.assertIn(pair, self.use_case.get_pairs())

    def test_add_message(self):
        self.use_case.add_user(self.user1)
        self.use_case.add_user(self.user2)
        message = Message(sender=self.user1, receiver=self.user2, content="Hello!", timestamp=datetime.now())
        self.use_case.add_message(message)
        self.assertIn(message, self.use_case.get_messages())

    def test_add_chat(self):
        self.use_case.add_user(self.user1)
        self.use_case.add_user(self.user2)
        chat = Chat(id=1, participants=[self.user1, self.user2])
        self.use_case.add_chat(chat)
        self.assertIn(chat, self.use_case.get_chats())

    def test_add_gift(self):
        self.use_case.add_user(self.user1)
        gift = Gift(id=1, name="Flowers", value=20.0, timestamp=datetime.now())
        self.use_case.add_gift(gift)
        self.assertIn(gift, self.use_case.get_gifts())

if __name__ == "__main__":
    unittest.main()
