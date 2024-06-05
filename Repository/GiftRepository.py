from Class.Gift import Gift

class GiftRepository:
    def __init__(self):
        self.gifts = []

    def add_gift(self, gift: Gift):
        self.gifts.append(gift)

    def get_gift(self, gift_id: int):
        for gift in self.gifts:
            if gift.gift_id == gift_id:
                return gift
        return None
