# from typing import Union, List
from typing import Union
from entities.mixin import Mixin


class Column(Mixin):
    """O contâiner Column define um elemento de coluna, que é parte de um ColumnSet."""
    def __init__(self, items: Union[None, list] = None, backgroundImage=None, bleed: Union[None, bool] = None, fallback=None,
                 minHeight: Union[None, str] = None, rtl: Union[None, bool] = None, separator: Union[None, bool] = None,
                 spacing: Union[None, str, int] = None, style: Union[None, str] = None, verticalContentAlignment: Union[None, str] = None,
                 width: Union[None, str, int] = None, id: Union[None, str] = None, isVisible: Union[None, bool] = None):
        # como definir os tipos requeridos dentro da lista items?
        if items is None or items == []:
            items = []
        else:
            try:
                items = [obj.__dict__ for obj in items]
            except AttributeError:  # especifica exceção e a trata
                raise Exception("'Items' attribute must be a list of objects")
        self.items = items

        super().create_fields(locals())

    def add_to_items(self, card_element):
        self.items.append(card_element.__dict__)
