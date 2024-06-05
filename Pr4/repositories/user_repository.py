import xml.etree.ElementTree as ET
from models.user import User
from repositories.xml_repository import XMLRepository

class UserRepository(XMLRepository):
    def __init__(self, xml_file='users.xml'):
        super().__init__(xml_file)

    def add_user(self, user):
        user_element = ET.Element('user')
        user_element.set('id', str(user.id))
        user_element.set('username', user.username)
        user_element.set('email', user.email)
        self.add_element(user_element)

    def get_user(self, user_id):
        user_elements = self.find(f".//user[@id='{user_id}']")
        if not user_elements:
            return None
        user_element = user_elements[0]
        return User(
            id=int(user_element.get('id')),
            username=user_element.get('username'),
            email=user_element.get('email')
        )
