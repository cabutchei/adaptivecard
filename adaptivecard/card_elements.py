from typing import Any, Optional, Union
from typing_extensions import Literal
from adaptivecard._base_types import Element
from adaptivecard._mixin import Mixin



class TextBlock(Mixin, Element):
    """Elemento de texto"""
    __slots__ = ('type', 'text', 'color', 'font_type', 'horizontal_alignment', 'is_subtle', 'max_lines', 'size', 'weight', 'wrap', 'style', 'fallback',
                            'height', 'separator', 'spacing', 'id', 'is_visible')
    def __init__(self,
                 text: Any = "",
                 color: Optional[Literal["default", "dark", "light", "accent", "good", "warning", "attention"]] = None,
                 font_type: Optional[Literal["default", "monospace"]] = None,
                 horizontal_alignment: Optional[Literal["left", "center", "right"]] = None,
                 is_subtle: Optional[bool] = None,
                 max_lines: Optional[int] = None,
                 size: Optional[Literal["default", "small", "medium", "large", "extraLarge"]] = None,
                 weight: Optional[Literal["default", "lighter", "bolder"]] = None,
                 wrap: Optional[bool] = None,
                 style: Optional[Literal["default", "heading"]] = None,
                 fallback: Optional[Union[str, Element]] = None,
                 height: Optional[Literal["auto", "stretch"]] = None,
                 separator: Optional[bool] = None,
                 spacing: Optional[Literal["default", "none", "small", "medium", "large", "extraLarge", "padding"]] = None,
                 id: Optional[str] = None,
                 is_visible: Optional[bool] = None):

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
    __slots__ = ('url', 'alt_text', 'background_color', 'height', 'horizontal_alignment', 'select_action')
    def __init__(self,
                 url: str,
                 alt_text: Optional[str] = None,
                 background_color: Optional[str] = None,
                 height: Optional[str] = None,
                 horizontal_alignment: Optional[Literal["left", "center", "right"]] = None,
                 select_action: Optional[str] = None):
        self.type = "Image"