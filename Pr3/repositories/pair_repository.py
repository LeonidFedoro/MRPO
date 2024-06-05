class PairRepository:
    def __init__(self):
        self.pairs = []

    def add_pair(self, pair):
        self.pairs.append(pair)

    def get_pairs(self):
        return self.pairs
