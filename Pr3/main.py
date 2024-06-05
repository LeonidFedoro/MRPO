from datetime import datetime
from models.pair import Pair
from models.gift import Gift
from models.user import User
from models.message import Message
from models.chat import Chat
from repositories.user_repository import UserRepository
from repositories.pair_repository import PairRepository
from repositories.message_repository import MessageRepository
from repositories.chat_repository import ChatRepository
from repositories.gift_repository import GiftRepository

# Создание репозиториев
user_repo = UserRepository()
match_repo = PairRepository()
message_repo = MessageRepository()
chat_repo = ChatRepository()
gift_repo = GiftRepository()

# Создание объектов
user1 = User(user_id=1, name="Alice", age=25, gender="Female", email="alice@example.com")
user2 = User(user_id=2, name="Bob", age=27, gender="Male", email="bob@example.com")

match1 = Pair(match_id=1, user1=user1, user2=user2, match_date=datetime.now())

message1 = Message(message_id=1, sender=user1, receiver=user2, content="Hi Bob!", timestamp=datetime.now())

chat1 = Chat(chat_id=1, participants=[user1, user2])
chat1.add_message(message1)

gift1 = Gift(gift_id=1, sender=user1, receiver=user2, gift_type="Flowers", timestamp=datetime.now())

# Добавление объектов в репозиторий
user_repo.add_user(user1)
user_repo.add_user(user2)
match_repo.add_match(match1)
message_repo.add_message(message1)
chat_repo.add_chat(chat1)
gift_repo.add_gift(gift1)

# Получение объектов из репозитория
retrieved_user = user_repo.get_user(1)
retrieved_match = match_repo.get_match(1)
retrieved_message = message_repo.get_message(1)
retrieved_chat = chat_repo.get_chat(1)
retrieved_gift = gift_repo.get_gift(1)

# Вывод результатов
print(retrieved_user.name)  # Output: Alice
print(retrieved_chat.participants[1].name)  # Output: Bob
