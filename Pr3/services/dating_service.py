from datetime import datetime, timedelta
from models.pair import Pair

class DatingService:
    def __init__(self, user_repo, pair_repo, message_repo, chat_repo, gift_repo):
        self.user_repo = user_repo
        self.pair_repo = pair_repo
        self.message_repo = message_repo
        self.chat_repo = chat_repo
        self.gift_repo = gift_repo

    def can_send_message(self, sender, receiver, chat):
        return sender in chat.participants and receiver in chat.participants

    def can_send_gift(self, sender, receiver):
        return not self.is_user_blocked(sender, receiver)

    def create_pair(self, user1, user2):
        if self.has_mutual_like(user1, user2):
            self.pair_repo.add_pair(Pair(user1, user2))
            return True
        return False

    def can_send_message_frequency(self, sender):
        one_minute_ago = datetime.now() - timedelta(minutes=1)
        recent_messages = [msg for msg in self.message_repo.get_messages() if msg.sender == sender and msg.timestamp > one_minute_ago]
        return len(recent_messages) < 5

    def can_add_to_chat(self, chat):
        return len(chat.participants) < 50

    def can_send_gift_frequency(self, sender):
        today = datetime.now().date()
        today_gifts = [gift for gift in self.gift_repo.get_gifts() if gift.sender == sender and gift.timestamp.date() == today]
        return len(today_gifts) < 10

    def is_user_blocked(self, sender, receiver):
        return False

    def has_mutual_like(self, user1, user2):
        return True
