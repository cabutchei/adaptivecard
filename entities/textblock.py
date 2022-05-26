from typing import Text, Union
from entities.mixin import Mixin
from entities.columnset import ColumnSet
from entities.container import Container


class TextBlock(Mixin):
    """Elemento de texto"""
    def __init__(self, text: str = "", color: Union[None, str] = None, fontType: Union[None, str] = None, horizontalAlignment: Union[None, str] = None,
                isSubtle: Union[None, bool] = None, maxLines: Union[None, int] = None, size: Union[None, str] = None, weight: Union[None, str] = None,
                wrap: Union[None, bool] = None, style: Union[None, str] = None, fallback: Union[None, str, ColumnSet, Container] = None, height: Union[None, str] = None,
                separator: Union[None, bool] = None, spacing: Union[None, str] = None, id: Union[None, str] = None, isVisible: Union[None, bool] = None):
        self.type = "TextBlock"
        self.text = text
        super().create_fields(locals())
