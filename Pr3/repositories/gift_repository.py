class GiftRepository:
    def __init__(self):
        self.gifts = []

    def add_gift(self, gift):
        self.gifts.append(gift)

    def get_gifts(self):
        return self.gifts
