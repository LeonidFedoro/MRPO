import xml.etree.ElementTree as ET
from models.gift import Gift
from repositories.xml_repository import XMLRepository

class GiftRepository(XMLRepository):
    def __init__(self, xml_file='gifts.xml'):
        super().__init__(xml_file)

    def add_gift(self, gift):
        gift_element = ET.Element('gift')
        gift_element.set('id', str(gift.id))
        gift_element.set('name', gift.name)
        gift_element.set('value', str(gift.value))
        gift_element.set('timestamp', gift.timestamp.isoformat())
        self.add_element(gift_element)

    def get_gifts(self):
        gift_elements = self.find(".//gift")
        gifts = []
        for element in gift_elements:
            gifts.append(Gift(
                id=int(element.get('id')),
                name=element.get('name'),
                value=float(element.get('value')),
                timestamp=element.get('timestamp')
            ))
        return gifts
