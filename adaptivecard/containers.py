from typing import Any, Optional, Union, Sequence, List, get_type_hints
from typing_extensions import Literal
from adaptivecard._base_types import Element, Action, Iselect_action
from adaptivecard._mixin import Mixin
from tabulate import tabulate
from typeguard import check_type
from adaptivecard.card_elements import TextBlock



class Container(Mixin, Element):
    """Um contâiner é um agrupamento de elementos"""
    __slots__ = ('type', 'items', 'style', 'vertical_content_alignment', 'bleed', 'min_height', 'rtl',
                                      'height', 'separator', 'spacing', 'id', 'is_visible')
    def __init__(self,
                 items: Optional[Union[Element, Sequence[Element]]] = None,
                 style: Optional[Literal["default", "emphasis", "good", "attention", "warning", "accent"]] = None,
                 vertical_content_alignment: Optional[Literal["top", "center", "bottom"]] = None,
                 bleed: Optional[bool] = None,
                 min_height: Optional[str] = None,
                 rtl: Optional[bool] = None,
                 height: Optional[Literal["auto", "stretch"]] = None,
                 separator: Optional[bool] = None,
                 spacing: Optional[Literal["default", "none", "small", "medium", "large", "extraLarge", "padding"]] = None,
                 id: Optional[str] = None,
                 is_visible: Optional[bool] = None):

        self.type = "Container"
        self.items = items
        self.style = style
        self.vertical_content_alignment = vertical_content_alignment
        self.bleed = bleed
        self.min_height = min_height
        self.rtl = rtl
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.id = id
        self.is_visible = is_visible

    @property
    def empty(self):
        return len(self.items) == 0

    def append_element(self, element: Element):
        self.items.append(element)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(items={self.items})"

    def __str__(self) -> str:
        return "[" + ", ".join([str(item) for item in self.items]) + "]"
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'items':
            if __value is None:
                __value = []
            elif isinstance(__value, Element):
                __value = [__value]
        return super().__setattr__(__name, __value)


class ColumnSet(Mixin, Element):
    """ColumnSet define um grupo de colunas"""
    __slots__ = ('type', 'columns', 'style', 'bleed', 'min_height', 'horizontal_alignment', 'height',
                                      'separator', 'spacing', 'id', 'is_visible')
    def __init__(self, columns: Optional[Sequence["Column"]] = None,
                 style: Optional[Literal["default", "emphasis", "good", "attention", "warning", "accent"]] = None,
                 bleed: Optional[bool] = None,
                 min_height: Optional[str] = None,   # pensar em algum type check para isso
                 horizontal_alignment: Optional[Literal["left", "center", "right"]] = None,
                 height: Optional[Literal["auto", "stretch"]] = None,
                 separator: Optional[bool] = None,
                 spacing: Optional[Literal["default", "none", "small", "medium", "large", "extraLarge", "padding"]] = None,
                 id_: Optional[str] = None,
                 is_visible: Optional[bool] = None):

        if columns is None:
            columns = []

        self.type = 'ColumnSet'
        self.columns = list(columns)
        self.style = style
        self.bleed = bleed
        self.min_height = min_height
        self.horizontal_alignment = horizontal_alignment
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.id = id_
        self.is_visible = is_visible

    def add_to_columns(self, column_element):
        self.columns.append(column_element)


class Column(Mixin, Element):
    """O contâiner Column define um elemento de coluna, que é parte de um ColumnSet."""
    __slots__ = ('type', 'items', 'background_image', 'bleed', 'fallback', 'min_height', 'rtl', 'separator',
                                      'spacing', 'style', 'vertical_content_alignment', 'rtl', 'width', 'id', 'is_visible')
    def __init__(self,
                 items: Optional[Sequence[Element]] = None,
                 background_image=None,
                 bleed: Optional[bool] = None,
                 fallback: Optional["Column"] = None,
                 min_height: Optional[str] = None,
                 rtl: Optional[bool] = None,
                 separator: Optional[bool] = None,
                 spacing: Optional[Union[str, int]] = None,
                 style: Optional[str] = None,
                 vertical_content_alignment: Optional[str] = None,
                 width: Optional[Union[str, int]] = None,
                 id: Optional[str] = None,
                 is_visible: Optional[bool] = None):

        if items is None:
            items = []

        self.type = "Column"
        self.items = list(items)
        self.background_image = background_image
        self.bleed = bleed
        self.fallback = fallback
        self.min_height = min_height
        self.rtl = rtl
        self.separator = separator
        self.spacing = spacing
        self.style = style
        self.vertical_content_alignment = vertical_content_alignment
        self.width = width
        self.id = id
        self.is_visible = is_visible

    def add_to_items(self, card_element):
        self.items.append(card_element)


class TableCell(Mixin):
    __slots__ = ('type', 'items', 'select_action', 'style', 'vertical_alignment', 'bleed', 'background_image', 'min_height', 'rtl')
    def __init__(self,
                 items: Optional[Union[Any, Sequence[Any]]] = None,
                 select_action: Optional[Iselect_action] = None,
                 style: Optional[Literal["default", "emphasis", "good", "attention", "warning", "accent"]] = None,
                 vertical_alignment: Optional[Literal["top", "center", "bottom"]] = None,
                 bleed: Optional[bool] = None,
                 background_image: Optional[str] = None,
                 min_height: Optional[str] = None,
                 rtl: Optional[bool] = None):
      
        if items is None:
            items = []
        elif isinstance(items, Element):
            items = [items]
        elif not self.is_sequence(items):
            items = [TextBlock(text=str(items))]
        else:
            items = list(items)
            for i, item in enumerate(items):
                if not isinstance(item, Element):
                    items[i] = TextBlock(text=str(item))
        self.type = "TableCell"
        self.items = items
        self.select_action = select_action
        self.items = items
        self.style = style
        self.vertical_alignment = vertical_alignment
        self.bleed = bleed
        self.background_image = background_image
        self.min_height = min_height
        self.rtl = rtl

    def add_to_items(self, element: Element):
        self.items.append(element)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(items={[str(item) for item in self.items]})"

    def __str__(self) -> str:
        return "[" + ", ".join([str(item) for item in self.items]) + "]"


class TableRow(Mixin, Sequence):
    __slots__ = ("type", "cells", "style")
    def __init__(self, cells: List, style: Optional[Literal["default", "emphasis", "good", "attention", "warning", "accent"]] = None):
        self.type = "TableRow"
        for i, cell in enumerate(cells):
            if not isinstance(cell, TableCell):
                cells[i] = TableCell(cell)
        self.cells = cells
        self.style = style
    def __getitem__(self, __i):
        if isinstance(__i, slice):
            return self.__class__(cells=self.cells[__i])
        return self.cells.__getitem__(__i)
    def __setitem__(self, __key, __value):
        self.cells.__setitem__(__key, TableCell(__value))
    def __add__(self, __value):
        return self.__class__(self.cells + __value.cells)
    def __len__(self):
        return len(self.cells)
    def __repr__(self):
        return f"{self.__class__.__name__}({str(self.cells)})"
    def __str__(self):
        return "[" + ", ".join([str(cell) for cell in self.cells]) + "]"


class Table(Mixin, Element):
    __slots__ = ('type', '_columns', 'rows', 'firstRowAsHeader', 'showGridLines', 'gridStyle',
                 'horizontal_cell_content_alignment', 'vertical_content_alignment', 'fallback', 'height',
                 'separator', 'spacing', 'id', 'is_visible')
    def __init__(self,
                 rows: Optional[Sequence[Sequence[Union[Element, TableCell]]]] = None,
                 firstRowAsHeader: Optional[bool] = None,
                 columns: Sequence[int] = [],
                 showGridLines: Optional[bool] = None,
                 gridStyle: Optional[Literal["default", "emphasis", "good", "attention", "warning", "accent"]] = None,
                 horizontal_cell_content_alignment: Optional[Literal["left", "center", "right"]] = None,
                 verticalCellContentAlignment: Optional[Literal["top", "center", "bottom"]] = None,
                 fallback: Optional[Element] = None,
                 height: Optional[Literal["auto", "stretch"]] = None,
                 separator: Optional[bool] = None,
                 spacing: Optional[Literal["default", "none", "small", "medium", "large", "extraLarge", "padding"]] = None,
                 id_: Optional[str] = None,
                 is_visible: Optional[bool] = None):

        self.type = "Table"

        self.rows = rows
        self._columns = list(columns)
        self.firstRowAsHeader = firstRowAsHeader
        self.showGridLines = showGridLines
        self.gridStyle = gridStyle
        self.horizontal_cell_content_alignment = horizontal_cell_content_alignment
        self.verticalCellContentAlignment = verticalCellContentAlignment
        self.fallback = fallback
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.id = id_
        self.is_visible = is_visible

    @property
    def columns(self):
        if len(self.rows) > 0:
            if len(self._columns) == 0:
                return [{"width": 1} for _ in self.rows[0]]
            else:
                return [{"width": value} for value in self._columns]

    @columns.setter
    def columns(self, value):
        check_type(value, get_type_hints(self.__init__)['columns'])
        cols = list(value)
        if len(self.rows) > 0 and len(cols) < len(self.rows[0]):
            raise Exception("'length of columns must match the length of rows'")
        self._columns = value

    def __getitem__(self, __i):
        return self.rows.__getitem__(__i)
    
    def append_row(self, row: Sequence):
        if not isinstance(row, Sequence) or isinstance(row, str):
            raise Exception("'row' attribute must be a sequence of some kind")
        row = TableRow(row)
        self.rows.append(row)
    
    def __len__(self):
        return len(self.rows)
    
    def __str__(self):
        rows = [["\n".join([str(item) for item in cell.items]) for cell in row.cells] for row in self.rows]
        if self.firstRowAsHeader:
            headers = rows[0]
            rows = rows[1:]
        else:
            headers = []
        return tabulate(rows, headers=headers, tablefmt='grid')

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'rows':
            rows = __value
            if rows is None:
                rows = []
            elif not self.is_sequence(rows):
                raise TypeError("'rows' attribute must be a sequence of some kind")
            elif len(rows) > 0 and not all(self.is_sequence(row) for row in rows):
                raise TypeError("'rows' attribute must be a sequence of sequences")
            else:
                for i, row in enumerate(rows):
                    for j, cell in enumerate(row):
                        if not isinstance(cell, TableCell):
                            row[j] = TableCell(cell)
                    rows[i] = TableRow(cells=row)

            if len(rows) > 1 and not all([len(rows[i]) == len(rows[i-1]) for i, _ in enumerate(rows[1:])]):
                raise Exception("Length mismatch, all rows must have the same length")
            __value = rows
        return super().__setattr__(__name, __value)


class ActionSet(Mixin, Element):
    __slots__ = ("type", "actions", "fallback", "height", "separator", "spacing", "id", "is_visible")
    def __init__(self,
                 actions: Optional[Union[Action, Sequence[Action]]] = None,
                 fallback: Optional[Element] = None,
                 height: Optional[Any] = None,
                 separator: Optional[bool] = None,
                 spacing: Optional[Literal["default", "none", "small", "medium", "large", "extraLarge", "padding"]] = None,
                 id: Optional[str] = None,
                 is_visible: Optional[bool] = None
                 ) -> None:
        self.type = "ActionSet"
        self.actions = actions
        self.fallback = fallback
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.id = id
        self.is_visible = is_visible

    def append_action(self, action: Action):
        self.actions.append(action)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __value is None:
            __value = []
        elif isinstance(__value, Element):
            __value = [__value]
        return super().__setattr__(__name, __value)