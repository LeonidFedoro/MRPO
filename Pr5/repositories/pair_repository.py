from repositories.base_repository import BaseRepository
from models.pair import Pair

class PairRepository(BaseRepository):
    def __init__(self):
        self.pairs = []

    def add(self, pair: Pair):
        self.pairs.append(pair)

    def get(self, id: int) -> Pair:
        for pair in self.pairs:
            if pair.id == id:
                return pair
        return None

    def update(self, pair: Pair):
        for idx, p in enumerate(self.pairs):
            if p.id == pair.id:
                self.pairs[idx] = pair

    def delete(self, id: int):
        self.pairs = [pair for pair in self.pairs if pair.id != id]
