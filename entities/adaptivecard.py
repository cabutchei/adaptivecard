from typing import Union, List
from entities.mixin import Mixin
from entities.columnset import ColumnSet
from entities.container import Container
from entities.textblock import TextBlock

class AdaptiveCard(Mixin):
    """O template principal do card"""  # Essas descrições hão de ficar mais detalhadas à medida que eu desenvolver a lib e sua documentação
    def __init__(self, type: str = "AdaptiveCard", version = "1.2", schema: str = "http://adaptivecards.io/schemas/adaptive-card.json", body: Union[None, List[Union[ColumnSet, Container, TextBlock]]] = None, falbackText: Union[None, str] = None, backgroundImage = None, minHeight = None, rtl = None, speak = None, lang = None, verticalContentAlignment = None):
        self.type = type
        self.version = version
        super().set_version(self.version)
        self.schema = schema

        if body == None or body == []:
            body = []
        else:
            try:
                body = [obj.__dict__ for obj in body]
            except:
                raise Exception("'Body' attribute must be a list of objects")
        self.body = body
        super().create_fields(locals())
    
        
    def add_to_body(self, card_element):
        self.body.append(card_element.__dict__)
