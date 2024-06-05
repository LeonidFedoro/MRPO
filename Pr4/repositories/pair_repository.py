import xml.etree.ElementTree as ET
from models.pair import Pair
from repositories.xml_repository import XMLRepository

class PairRepository(XMLRepository):
    def __init__(self, xml_file='pairs.xml'):
        super().__init__(xml_file)

    def add_pair(self, pair):
        pair_element = ET.Element('pair')
        pair_element.set('user1', str(pair.user1.id))
        pair_element.set('user2', str(pair.user2.id))
        self.add_element(pair_element)

    def get_pairs(self):
        pair_elements = self.find(".//pair")
        pairs = []
        for element in pair_elements:
            user1_id = int(element.get('user1'))
            user2_id = int(element.get('user2'))
            user1 = self.user_repo.get_user(user1_id)
            user2 = self.user_repo.get_user(user2_id)
            if user1 and user2:
                pairs.append(Pair(user1, user2))
        return pairs
