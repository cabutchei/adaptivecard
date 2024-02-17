from typing import Any, Optional, Union
from typing_extensions import Literal
from adaptivecard._base_types import Element
from adaptivecard._mixin import Mixin
from adaptivecard.actions import Execute, OpenUrl, Submit, ToggleVisibilty



class TextBlock(Mixin, Element):
    """Elemento de texto"""
    __slots__ = ('type', 'text', 'color', 'font_type', 'horizontal_alignment', 'is_subtle',
                 'max_lines', 'size', 'weight', 'wrap', 'style', 'fallback',
                 'height', 'separator', 'spacing', 'id', 'is_visible')
    def __init__(self,
                 text: Any,
                 color: Literal["default", "dark", "light", "accent", "good", "warning", "attention"] = None,
                 font_type: Literal["default", "monospace"] = None,
                 horizontal_alignment: Literal["left", "center", "right"] = None,
                 is_subtle: bool = None,
                 max_lines: int = None,
                 size: Literal["default", "small", "medium", "large", "extraLarge"] = None,
                 weight: Literal["default", "lighter", "bolder"] = None,
                 wrap: bool = None,
                 style: Literal["default", "heading"] = None,
                 fallback: str | Element = None,
                 height: Literal["auto", "stretch"] = None,
                 separator: bool = None,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge", "padding"] = None,
                 id: str = None,
                 is_visible: bool = None):

        self.type = "TextBlock"
        self.text = text
        self.color = color
        self.font_type = font_type
        self.horizontal_alignment = horizontal_alignment
        self.is_subtle = is_subtle
        self.max_lines = max_lines
        self.size = size
        self.weight = weight
        self.wrap = wrap
        self.style = style
        self.fallback = fallback
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.id = id
        self.is_visible = is_visible

    def __repr__(self):
        return f"{self.__class__.__name__}(text='{self.text}')"

    def __str__(self):
        return self.text

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'text' and isinstance(__name, str):
            __value = str(__value)
        return super().__setattr__(__name, __value)


class Image(Mixin, Element):
    __slots__ = ("type", "url", "alt_text", "background_color", "height", "horizontal_alignment",
                 "select_action", "size", "style", "width", "fallback", "separator", "spacing",
                 "id", "is_visible")
    def __init__(self,
                 url: str,
                 alt_text: str = None,
                 background_color: str = None,
                 height: str | Literal["auto", "stretch"] = None,
                 horizontal_alignment: Literal["left", "center", "right"] = None,
                 select_action: Execute | OpenUrl | Submit | ToggleVisibilty = None,
                 size: Literal["auto", "stretch", "small", "medium", "large"] = None,
                 style: Literal["default", "person"] = None,
                 width: str = None,
                 fallback: Element = None,
                 separator: bool = None,
                 spacing: Literal["default", "none", "medium", "large", "extraLarge",
                                  "padding"] = None,
                 id: str = None,
                 is_visible: bool = None
                ):

        self.type = "Image"
        self.url = url
        self.alt_text = alt_text
        self.background_color = background_color
        self.height = height
        self.horizontal_alignment = horizontal_alignment
        self.select_action = select_action
        self.size = size
        self.style = style
        self.width = width
        self.fallback = fallback
        self.separator = separator
        self.spacing = spacing
        self.id = id
        self.is_visible = is_visible