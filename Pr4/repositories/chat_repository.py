import xml.etree.ElementTree as ET
from models.chat import Chat
from repositories.xml_repository import XMLRepository

class ChatRepository(XMLRepository):
    def __init__(self, xml_file='chats.xml'):
        super().__init__(xml_file)

    def add_chat(self, chat):
        chat_element = ET.Element('chat')
        chat_element.set('id', str(chat.id))
        participants_element = ET.SubElement(chat_element, 'participants')
        for participant in chat.participants:
            participant_element = ET.SubElement(participants_element, 'participant')
            participant_element.set('id', str(participant.id))
        self.add_element(chat_element)

    def get_chats(self):
        chat_elements = self.find(".//chat")
        chats = []
        for element in chat_elements:
            chat_id = int(element.get('id'))
            participants = []
            for participant_element in element.find('participants'):
                participant_id = int(participant_element.get('id'))
                participant = self.user_repo.get_user(participant_id)
                if participant:
                    participants.append(participant)
            chats.append(Chat(id=chat_id, participants=participants))
        return chats
