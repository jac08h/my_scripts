import xml.etree.ElementTree as ET
from dataclasses import dataclass

from typing import List


@dataclass
class SMSData:
    sender: str
    receiver: str
    text: str
    readable_date: str

    def __repr__(self):
        return f"{self.readable_date:<22}- {self.sender}: {self.text}"

    def __str__(self):
        return self.__repr__()


def parse_single_sms(sms: ET.Element):
    sent = True if sms.attrib['type'] == '2' else False
    return {"text": sms.attrib['body'],
            "readable_date": sms.attrib['readable_date'],
            "sent": sent}


def parse_conversation(path_to_file: str, sender_name: str, receiver_name: str) -> List[SMSData]:
    tree = ET.parse(path_to_file)
    root = tree.getroot()
    all_sms_xml = list(root)
    all_smses = []
    for sms_xml_element in all_sms_xml:
        sms_basic_dict = parse_single_sms(sms_xml_element)
        sender, receiver = (sender_name, receiver_name) if sms_basic_dict['sent'] else (receiver_name, sender_name)
        sms_data = SMSData(sender, receiver, sms_basic_dict['text'], sms_basic_dict['readable_date'])
        all_smses.append(sms_data)
    return all_smses


filename = input("Enter filename")
sender = input("Enter sender's name")
receiver = input("Enter receiver's name")
conv = parse_conversation(filename, sender, receiver)
for msg in conv:
    print(msg)
