from typing import Union, List
from entities.content import Content

class Message:
    """"Estrutura final do card tal como se requer para envio a um canal do Teams"""
    def __init__(self, attachments: Union[None, List[Content]] = None):
        self.type = "message"
        if attachments == None or attachments == []:
            attachments = []
        else:
            try:
                attachments = [obj.__dict__ for obj in attachments]
            except:
                raise Exception("'Attachments' attribute must be a list of objects")
        self.attachments = attachments

    def attach(self, content):
        self.attachments.append(content.__dict__)
