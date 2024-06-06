from repositories.base_repository import BaseRepository
from models.gift import Gift

class GiftRepository(BaseRepository):
    def __init__(self):
        self.gifts = []

    def add(self, gift: Gift):
        self.gifts.append(gift)

    def get(self, id: int) -> Gift:
        for gift in self.gifts:
            if gift.id == id:
                return gift
        return None

    def update(self, gift: Gift):
        for idx, g in enumerate(self.gifts):
            if g.id == gift.id:
                self.gifts[idx] = gift

    def delete(self, id: int):
        self.gifts = [gift for gift in self.gifts if gift.id != id]
