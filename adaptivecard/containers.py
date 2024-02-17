from typing import Any, get_type_hints
from typing_extensions import Literal
from adaptivecard._base_types import Element, Action, ISelectAction, BaseColumnSet, BaseColumn, Execute, OpenUrl, Submit, ToggleVisibility
from adaptivecard._mixin import Mixin
from tabulate import tabulate
from adaptivecard.card_elements import TextBlock
from adaptivecard._utils import check_type
from adaptivecard._typing import ListLike



class Container(Mixin, Element):
    """Um contâiner é um agrupamento de elementos"""
    __slots__ = ('type', 'items', 'style', 'vertical_content_alignment', 'bleed', 'min_height',
                 'rtl', 'height', 'separator', 'spacing', 'id', 'is_visible')
    def __init__(self,
                 items: Element | ListLike[Element] = None,
                 style: Literal["default", "emphasis", "good", "attention", "warning", "accent"] = None,
                 vertical_content_alignment: Literal["top", "center", "bottom"] = None,
                 bleed: bool = None,
                 min_height: str = None,
                 rtl: bool = None,
                 height: Literal["auto", "stretch"] = None,
                 separator: bool = None,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge", "padding"] = None,
                 id: str = None,
                 is_visible: bool = None):

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

    def __iter__(self):
        return iter(self.items)

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


class Column(Mixin, Element, BaseColumn):
    """O contâiner Column define um elemento de coluna, que é parte de um ColumnSet."""
    __slots__ = ('type', 'items', 'background_image', 'bleed', 'fallback', 'min_height', 'rtl', 'separator',
                                      'spacing', 'style', 'vertical_content_alignment', 'rtl', 'width', 'id', 'is_visible')
    def __init__(self,
                 items: ListLike[Element] = None,
                 background_image = None,
                 bleed: bool = None,
                 fallback: "Column" = None,
                 min_height: str | int = None, # criar condição de casting
                 rtl: bool = None,
                 separator: bool = None,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge", "padding"] = None,
                 select_action: Execute | OpenUrl | Submit | ToggleVisibility = None,
                 style: Literal["default", "emphasis", "good", "attention", "warning",
                                "accent"] = None,
                 vertical_content_alignment: Literal["top", "center", "bottom"] = None,
                 width: str | int = None, # adicionar condicao de casting
                 id: str = None,
                 is_visible: bool = None):

        self.type = "Column"
        self.items: list = items
        self.background_image = background_image
        self.bleed = bleed
        self.fallback = fallback
        self.min_height = min_height
        self.rtl = rtl
        self.separator = separator
        self.spacing = spacing
        self.select_action = select_action
        self.style = style
        self.vertical_content_alignment = vertical_content_alignment
        self.width = width
        self.id = id
        self.is_visible = is_visible

    def append(self, card_element: Element):
        self.items.append(card_element)

    def __iter__(self):
        return iter(self.items)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "items":
            items = __value
            if items is None:
                items = []
            elif not isinstance(items, list):
                items = list(items)
            __value = items
        return super().__setattr__(__name, __value)


class ColumnSet(Mixin, Element, BaseColumnSet):
    """ColumnSet define um grupo de colunas"""
    __slots__ = ('type', 'columns', 'style', 'bleed', 'min_height', 'horizontal_alignment', 'height',
                 'separator', 'spacing', 'id', 'is_visible')
    def __init__(self,
                 columns: ListLike[Column] = None,
                 select_action: Execute | OpenUrl | Submit | ToggleVisibility = None,
                 style: Literal["default", "emphasis", "good", "attention", "warning",
                                "accent"] = None,
                 bleed: bool = None,
                 min_height: str | int = None,   # adicionar condicao de casting
                 horizontal_alignment: Literal["left", "center", "right"] | None = None,
                 fallback: Element = None,
                 height: Literal["auto", "stretch"] | None = None,
                 separator: bool | None = None,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge",
                                  "padding"] = None,
                 id: str = None,
                 is_visible: bool = None):

        self.type = 'ColumnSet'
        self.columns = columns
        self.style = style
        self.bleed = bleed
        self.min_height = min_height
        self.horizontal_alignment = horizontal_alignment
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.id = id
        self.is_visible = is_visible

    def append(self, column_element: Column):
        # check_type() aceitar lista tbm?
        self.columns.append(column_element)

    def __iter__(self):
        return iter(self.columns)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "columns":
            columns = __value
            if columns is None:
                columns = []
            elif not isinstance(columns, list):
                columns = list(columns)
        return super().__setattr__(__name, __value)



class TableCell(Mixin):
    __slots__ = ('type', 'items', 'select_action', 'style', 'vertical_alignment', 'bleed', 'background_image', 'min_height', 'rtl')
    def __init__(self,
                 items: Any | ListLike[Any] = None,
                 select_action: Execute | OpenUrl | Submit | ToggleVisibility = None,
                 style: Literal["default", "emphasis", "good", "attention", "warning",
                                "accent"] = None,
                 vertical_alignment: Literal["top", "center", "bottom"] = None,
                 bleed: bool = None,
                 background_image: str | None = None,
                 min_height: str | int = None, # adicionar condicao de casting
                 rtl: bool = None):

        self.type = "TableCell"
        if items is None:
            items = []
        self.items: list = items
        self.select_action = select_action
        self.items = items
        self.style = style
        self.vertical_alignment = vertical_alignment
        self.bleed = bleed
        self.background_image = background_image
        self.min_height = min_height
        self.rtl = rtl

    def append(self, element: Element):
        self.items.append(element)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(items={[item for item in self.items]})"

    def __str__(self) -> str:
        return "[" + ", ".join([str(item) for item in self.items]) + "]"

    def __iter__(self):
        return iter(self.items)
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "items":
            items = __value
            if items is None:
                items = []
            elif isinstance(items, Element):
                items = [items]
            elif isinstance(items, ListLike):
                items = [item if isinstance(item, Element) else TextBlock(str(item)) for item in items]
            else:
                items = [TextBlock(str(items))]
            __value = items
        return super().__setattr__(__name, __value)


class TableRow(Mixin, ListLike):
    __slots__ = ("type", "cells", "style")
    def __init__(self,
                 cells: ListLike[Any],
                 style: Literal["default", "emphasis", "good", "attention", "warning",
                                "accent"] = None):
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

    def __iter__(self):
        return iter(self.cells)

    def __repr__(self):
        return f"{self.__class__.__name__}({str(self.cells)})"

    def __str__(self):
        return "[" + ", ".join([str(cell) for cell in self.cells]) + "]"


class Table(Mixin, Element):
    __slots__ = ('type', 'columns', 'rows', 'first_row_as_header', 'show_grid_lines', 'grid_style',
                 'horizontal_cell_content_alignment', 'vertical_content_alignment', 'fallback', 'height',
                 'separator', 'spacing', 'id', 'is_visible')
    def __init__(self,
                 rows: ListLike[ListLike[Element | TableCell]] = None,
                 first_row_as_header: bool = None,
                 columns: ListLike[int] = None,
                 show_grid_lines: bool = None,
                 grid_style: Literal["default", "emphasis", "good", "attention", "warning",
                                     "accent"] = None,
                 horizontal_cell_content_alignment: Literal["left", "center", "right"] = None,
                 vertical_cell_content_alignment: Literal["top", "center", "bottom"] = None,
                 fallback: Element = None,
                 height: Literal["auto", "stretch"] = None,
                 separator: bool = None,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge",
                                  "padding"] = None,
                 id: str = None,
                 is_visible: bool = None):

        self.type = "Table"
        self.rows: list = rows
        self.columns = columns if columns is not None else []
        self.first_row_as_header = first_row_as_header
        self.show_grid_lines = show_grid_lines
        self.grid_style = grid_style
        self.horizontal_cell_content_alignment = horizontal_cell_content_alignment
        self.vertical_cell_content_alignment = vertical_cell_content_alignment
        self.fallback = fallback
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.id = id
        self.is_visible = is_visible

    def __getitem__(self, __i):
        return self.rows.__getitem__(__i)
    
    def append(self, row: ListLike):
        type_hints = get_type_hints(self.__init__)
        check_type('row', row, type_hints.get('row', Any))
        if not isinstance(row, TableRow):
            row = TableRow(row)
        self.rows.append(row)
    
    # custom to_dict para lidar com o formato atípico do atributo columns dentro do json
    def to_dict(self):
        dic = super().to_dict()
        if self.columns:
            json_columns = [{"width": width} for width in self.columns]
        elif self.rows:
            json_columns = [{"width": 1} for _ in self.rows[0]]
        else:
            json_columns = dic["columns"]
        dic["columns"] = json_columns
        return dic
    
    def __len__(self):
        return len(self.rows)
    
    def __str__(self):
        rows = [["\n".join([str(item) for item in cell.items]) for cell in row.cells] for row in self.rows]
        if self.first_row_as_header:
            headers = rows[0]
            rows = rows[1:]
        else:
            headers = []
        return tabulate(rows, headers=headers, tablefmt='grid')

    def __iter__(self):
        return iter(self.rows)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "rows":
            rows = __value
            if rows is None:
                rows = []
            for i, row in enumerate(rows):
                for j, cell in enumerate(row):
                    if not isinstance(cell, TableCell):
                        row[j] = TableCell(cell)
                if not isinstance(row, TableRow):
                    rows[i] = TableRow(cells=row)
            __value = rows
        return super().__setattr__(__name, __value)


class ActionSet(Mixin, Element):
    __slots__ = ("type", "actions", "fallback", "height", "separator", "spacing", "id", "is_visible")
    def __init__(self,
                 actions: Action | ListLike[Action] = None,
                 fallback: Element = None,
                 height: Literal["auto", "stretch"] = None,
                 separator: bool = None,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge", "padding"] | None = None,
                 id: str = None,
                 is_visible: bool = None
                 ):
        self.type = "ActionSet"
        self.actions: list = actions
        self.fallback = fallback
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.id = id
        self.is_visible = is_visible

    def append(self, action: Action) -> None:
        self.actions.append(action)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "actions":
            actions = __value
            if actions is None:
                actions = []
            elif isinstance(actions, Action):
                actions = [actions]
            elif not isinstance(actions, list):
                actions = list(actions)
            return super().__setattr__(__name, __value)