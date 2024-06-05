import xml.etree.ElementTree as ET
from models.message import Message
from repositories.xml_repository import XMLRepository

class MessageRepository(XMLRepository):
    def __init__(self, xml_file='messages.xml'):
        super().__init__(xml_file)

    def add_message(self, message):
        message_element = ET.Element('message')
        message_element.set('sender', str(message.sender.id))
        message_element.set('receiver', str(message.receiver.id))
        message_element.set('content', message.content)
        message_element.set('timestamp', message.timestamp.isoformat())
        self.add_element(message_element)

    def get_messages(self):
        message_elements = self.find(".//message")
        messages = []
        for element in message_elements:
            sender_id = int(element.get('sender'))
            receiver_id = int(element.get('receiver'))
            sender = self.user_repo.get_user(sender_id)
            receiver = self.user_repo.get_user(receiver_id)
            if sender and receiver:
                messages.append(Message(
                    sender=sender,
                    receiver=receiver,
                    content=element.get('content'),
                    timestamp=element.get('timestamp')
                ))
        return messages
