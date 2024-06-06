from datetime import datetime
from models.user import User
from models.pair import Pair
from models.message import Message
from models.chat import Chat
from models.gift import Gift
from use_case.dating_use_case import DatingUseCase

def main():
    # Initialize use case
    use_case = DatingUseCase()

    # Example usage
    user1 = User(id=1, username="user1", email="user1@example.com")
    user2 = User(id=2, username="user2", email="user2@example.com")

    use_case.add_user(user1)
    use_case.add_user(user2)

    pair = Pair(user1=user1, user2=user2)
    use_case.add_pair(pair)

    message = Message(sender=user1, receiver=user2, content="Hello!", timestamp=datetime.now())
    use_case.add_message(message)

    chat = Chat(id=1, participants=[user1, user2])
    use_case.add_chat(chat)

    gift = Gift(id=1, name="Flowers", value=20.0, timestamp=datetime.now())
    use_case.add_gift(gift)

if __name__ == "__main__":
    main()
