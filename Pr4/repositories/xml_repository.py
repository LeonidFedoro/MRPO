import xml.etree.ElementTree as ET

class XMLRepository:
    def __init__(self, xml_file):
        self.xml_file = xml_file

    def read_data(self):
        tree = ET.parse(self.xml_file)
        return tree.getroot()

    def write_data(self, root):
        tree = ET.ElementTree(root)
        tree.write(self.xml_file)

    def find(self, xpath):
        root = self.read_data()
        return root.findall(xpath)

    def add_element(self, element):
        root = self.read_data()
        root.append(element)
        self.write_data(root)
