from typing import Any, Optional, Union, Sequence
from typing_extensions import Literal
from adaptivecard._mixin import Mixin
from adaptivecard._base_types import Element, Action




class Content(Mixin):
    """Content é o elemento que recebe o AdaptiveCard e é adicionado à lista atachments, atributo de Message"""
    __slots__ = ("content_type", "content")
    def __init__(self, content: "AdaptiveCard"):
        self.content_type = "application/vnd.microsoft.card.adaptive"
        self.content = content


class Message(Mixin):
    """"Estrutura de mensagem. Um card precisa estar contido em uma mensagem para ser enviado via Teams."""
    __slots__ = ('type', 'attachments')
    def __init__(self, attachments: Optional[Sequence["Content"]] = None):
        self.type = "message"
        if attachments is None:
            attachments = []
        self.attachments = list(attachments)

    def attach(self, content):
        self.attachments.append(content)


class AdaptiveCard(Mixin):
    """O template principal do card"""  # Essas descrições hão de ficar mais detalhadas à medida que eu desenvolver a lib e sua documentação
    __slots__ = ("type", "version", "schema", "body", "actions", "fallback_text", "background_image", "min_height",
                 "rtl", "speak", "lang", "vertical_content_alignment")
    def __init__(self, version: str = "1.2",
                 schema: str = "http://adaptivecards.io/schemas/adaptive-card.json",
                 body: Optional[Union[Element, Sequence[Element]]] = None,
                 actions: Optional[Union[Action, Sequence[Action]]] = None,
                 fallback_text: Optional[str] = None,
                 background_image: Optional[str] = None,
                 min_height: Optional[str] = None,
                 rtl: Optional[bool] = None,
                 speak: Optional[str] = None,
                 lang: Optional[str] = None,
                 vertical_content_alignment: Optional[Literal["top", "center", "bottom"]] = None):
        
        self.type = "AdaptiveCard"
        self.version = version  
        self.schema = schema
        self.body = body
        self.actions = actions
        self.fallback_text = fallback_text
        self.background_image = background_image
        self.min_height = min_height
        self.rtl = rtl
        self.speak = speak
        self.lang = lang
        self.vertical_content_alignment = vertical_content_alignment

    @property
    def empty(self):
        return len(self.body) == 0

    def append_element(self, element: Element):
        self.body.append(element)

    def append_action(self, action):
        if not hasattr(self, 'actions'):
            self.actions = []
        self.actions.append(action)

    def to_message(self):
        content = Content(content=self)
        msg = Message(attachments=[content])
        return msg
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'body':
            if __value is None:
                __value = []
            elif isinstance(__value, Element):
                __value = [__value]
        if __name == 'actions' and isinstance(__value, Action):
            __value = [__value]
        return super().__setattr__(__name, __value)