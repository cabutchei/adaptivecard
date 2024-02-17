from typing import Any
from typing_extensions import Literal
from adaptivecard._base_types import Element
from adaptivecard._typing import DefaultNone
from adaptivecard._mixin import Mixin
from adaptivecard.actions import Execute, OpenUrl, Submit, ToggleVisibilty
from adaptivecard._utils import convert_to_pixel_string, raise_invalid_pixel_error



class TextBlock(Mixin, Element):
    """Elemento de texto"""
    __slots__ = ('type', 'text', 'color', 'font_type', 'horizontal_alignment', 'is_subtle',
                 'max_lines', 'size', 'weight', 'wrap', 'style', 'fallback',
                 'height', 'separator', 'spacing', 'id', 'is_visible')
    def __init__(self,
                 text: Any,
                 color: Literal["default", "dark", "light", "accent", "good", "warning", "attention"] = DefaultNone,
                 font_type: Literal["default", "monospace"] = DefaultNone,
                 horizontal_alignment: Literal["left", "center", "right"] = DefaultNone,
                 is_subtle: bool = DefaultNone,
                 max_lines: int = DefaultNone,
                 size: Literal["default", "small", "medium", "large", "extraLarge"] = DefaultNone,
                 weight: Literal["default", "lighter", "bolder"] = DefaultNone,
                 wrap: bool = DefaultNone,
                 style: Literal["default", "heading"] = DefaultNone,
                 fallback: str | Element = DefaultNone,
                 height: Literal["auto", "stretch"] = DefaultNone,
                 separator: bool = DefaultNone,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge", "padding"] = DefaultNone,
                 id: str = DefaultNone,
                 is_visible: bool = DefaultNone):

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
                 alt_text: str = DefaultNone,
                 background_color: str = DefaultNone,
                 height: str | Literal["auto", "stretch"] = DefaultNone,
                 horizontal_alignment: Literal["left", "center", "right"] = DefaultNone,
                 select_action: Execute | OpenUrl | Submit | ToggleVisibilty = DefaultNone,
                 size: Literal["auto", "stretch", "small", "medium", "large"] = DefaultNone,
                 style: Literal["default", "person"] = DefaultNone,
                 width: str = DefaultNone,
                 fallback: Element = DefaultNone,
                 separator: bool = DefaultNone,
                 spacing: Literal["default", "none", "medium", "large", "extraLarge",
                                  "padding"] = DefaultNone,
                 id: str = DefaultNone,
                 is_visible: bool = DefaultNone
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

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "width":
            width = __value
            try:
                width = convert_to_pixel_string(width)
            except ValueError:
                raise_invalid_pixel_error(__name, width)
            __value = width
        return super().__setattr__(__name, __value)