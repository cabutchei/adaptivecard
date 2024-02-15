from typing import Any
from typing_extensions import Literal
from adaptivecard._mixin import Mixin
from adaptivecard._base_types import Element, Action
from adaptivecard._typing import ListLike




class Content(Mixin):
    """Content é o elemento que recebe o AdaptiveCard e é adicionado à lista atachments, atributo de Message"""
    __slots__ = ("content_type", "content")
    def __init__(self, content: "AdaptiveCard"):
        self.content_type = "application/vnd.microsoft.card.adaptive"
        self.content = content


class Message(Mixin):
    """"Estrutura de mensagem. Um card precisa estar contido em uma mensagem para ser enviado via Teams."""
    __slots__ = ('type', 'attachments')
    def __init__(self, attachments: ListLike["Content"] | None = None):
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
    def __init__(self,
                 version: str | float = "1.2",
                 body: Element | ListLike[Element] | None = None,
                 actions: Action | ListLike[Action] | None = None,
                 fallback_text: str | None = None,
                 background_image: str | None = None,
                 min_height: str | None = None,
                 rtl: bool | None = None,
                 speak: str | None = None,
                 lang: str | None = None,
                 vertical_content_alignment: Literal["top", "center", "bottom"] | None = None):
        
        self.type = "AdaptiveCard"
        self.version = version  
        self.schema = "http://adaptivecards.io/schemas/adaptive-card.json"
        self.body: list = body
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

    def append(self, element: Element):
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
        if __name == 'version':
            version = __value
            if isinstance(version, float):
                version = str(version)
            __value = version
        if __name == 'body':
            if __value is None:
                __value = []
            elif isinstance(__value, Element):
                __value = [__value]
        if __name == 'actions' and isinstance(__value, Action):
            __value = [__value]
        return super().__setattr__(__name, __value)