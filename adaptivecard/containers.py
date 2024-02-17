from typing import Any, get_type_hints
from typing_extensions import Literal
from adaptivecard._base_types import Element, Action, BaseColumnSet, BaseColumn, Execute, OpenUrl, Submit, ToggleVisibility
from adaptivecard._mixin import Mixin
from adaptivecard.card_elements import TextBlock
from adaptivecard._utils import check_type, convert_to_pixel_string, raise_invalid_pixel_error
from adaptivecard._typing import ListLike, DefaultNone
from tabulate import tabulate



class Container(Mixin, Element):
    """Um contâiner é um agrupamento de elementos"""
    __slots__ = ('type', 'items', 'style', 'vertical_content_alignment', 'bleed', 'min_height',
                 'rtl', 'height', 'separator', 'spacing', 'id', 'is_visible')
    def __init__(self,
                 items: Element | ListLike[Element] = DefaultNone,
                 style: Literal["default", "emphasis", "good", "attention", "warning", "accent"] = DefaultNone,
                 vertical_content_alignment: Literal["top", "center", "bottom"] = DefaultNone,
                 bleed: bool = DefaultNone,
                 min_height: str = DefaultNone,
                 rtl: bool = DefaultNone,
                 height: Literal["auto", "stretch"] = DefaultNone,
                 separator: bool = DefaultNone,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge",
                                  "padding"] | None = DefaultNone,
                 id: str = DefaultNone,
                 is_visible: bool = DefaultNone):

        self.type = "Container"
        if items is DefaultNone:
            items = []
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
        if __name == 'items' and isinstance(__value, Element):
            __value = [__value]
        return super().__setattr__(__name, __value)


class Column(Mixin, Element, BaseColumn):
    """O contâiner Column define um elemento de coluna, que é parte de um ColumnSet."""
    __slots__ = ('type', 'items', 'background_image', 'bleed', 'fallback', 'min_height',
                 'rtl', 'separator', 'spacing', 'style', 'vertical_content_alignment', 'rtl',
                 'width', 'id', 'is_visible')
    def __init__(self,
                 items: ListLike[Element] = DefaultNone,
                 background_image = DefaultNone,
                 bleed: bool = DefaultNone,
                 fallback: "Column" = DefaultNone,
                 min_height: str | int = DefaultNone,
                 rtl: bool = DefaultNone,
                 separator: bool = DefaultNone,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge",
                                  "padding"] | None = DefaultNone,
                 select_action: Execute | OpenUrl | Submit | ToggleVisibility = DefaultNone,
                 style: Literal["default", "emphasis", "good", "attention", "warning",
                                "accent"] = DefaultNone,
                 vertical_content_alignment: Literal["top", "center", "bottom"] = DefaultNone,
                 width: str | int = DefaultNone,
                 id: str = DefaultNone,
                 is_visible: bool = DefaultNone):

        self.type = "Column"
        if items is DefaultNone:
            items = []
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
            if not isinstance(items, list):
                __value = list(items)
        elif __name == "min_height":
            min_height = __value
            if isinstance(min_height, int):
                __value = str(min_height) + "px"
        elif __name == "width":
            width = __value
            if isinstance(width, int):
                __value = str(width) + "px"
        return super().__setattr__(__name, __value)


class ColumnSet(Mixin, Element, BaseColumnSet):
    """ColumnSet define um grupo de colunas"""
    __slots__ = ('type', 'columns', 'style', 'bleed', 'min_height', 'horizontal_alignment', 'height',
                 'separator', 'spacing', 'id', 'is_visible')
    def __init__(self,
                 columns: ListLike[Column] = DefaultNone,
                 select_action: Execute | OpenUrl | Submit | ToggleVisibility = DefaultNone,
                 style: Literal["default", "emphasis", "good", "attention", "warning",
                                "accent"] = DefaultNone,
                 bleed: bool = DefaultNone,
                 min_height: str | int = DefaultNone,   # adicionar condicao de casting
                 horizontal_alignment: Literal["left", "center", "right"] | None = DefaultNone,
                 fallback: Element = DefaultNone,
                 height: Literal["auto", "stretch"] | None = DefaultNone,
                 separator: bool | None = DefaultNone,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge",
                                  "padding"] | None = DefaultNone,
                 id: str = DefaultNone,
                 is_visible: bool = DefaultNone):

        self.type = 'ColumnSet'
        if columns is DefaultNone:
            columns = []
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
            if not isinstance(columns, list):
                columns = list(columns)
        elif __name == "min_height":
            min_height = __value
            try:
                min_height = convert_to_pixel_string(min_height)
            except ValueError:
                raise_invalid_pixel_error(__name, min_height)
        return super().__setattr__(__name, __value)



class TableCell(Mixin):
    __slots__ = ('type', 'items', 'select_action', 'style', 'vertical_alignment', 'bleed',
                 'background_image', 'min_height', 'rtl')
    def __init__(self,
                 items: Any | ListLike[Any] = DefaultNone,
                 select_action: Execute | OpenUrl | Submit | ToggleVisibility = DefaultNone,
                 style: Literal["default", "emphasis", "good", "attention", "warning",
                                "accent"] = DefaultNone,
                 vertical_alignment: Literal["top", "center", "bottom"] = DefaultNone,
                 bleed: bool = DefaultNone,
                 background_image: str = DefaultNone,
                 min_height: str | int = DefaultNone,
                 rtl: bool = DefaultNone):

        self.type = "TableCell"
        if items is DefaultNone:
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
            if isinstance(items, Element):
                items = [items]
            elif isinstance(items, ListLike):
                items = [item if isinstance(item, Element) else TextBlock(item) for item in items]
            else:
                items = [TextBlock(items)]
            __value = items
        elif __name == "min_height":
            min_height = __value
            try:
                min_height = convert_to_pixel_string(min_height)
            except ValueError:
                raise_invalid_pixel_error(__name, min_height)
            __value = min_height
        return super().__setattr__(__name, __value)


class TableRow(Mixin, ListLike):
    __slots__ = ("type", "cells", "style")
    def __init__(self,
                 cells: ListLike[Any],
                 style: Literal["default", "emphasis", "good", "attention", "warning",
                                "accent"] = DefaultNone):
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
                 rows: ListLike[ListLike[Element | TableCell]] = DefaultNone,
                 first_row_as_header: bool = DefaultNone,
                 columns: ListLike[int] = DefaultNone,
                 show_grid_lines: bool = DefaultNone,
                 grid_style: Literal["default", "emphasis", "good", "attention", "warning",
                                     "accent"] = DefaultNone,
                 horizontal_cell_content_alignment: Literal["left", "center", "right"] = DefaultNone,
                 vertical_cell_content_alignment: Literal["top", "center", "bottom"] = DefaultNone,
                 fallback: Element = DefaultNone,
                 height: Literal["auto", "stretch"] = DefaultNone,
                 separator: bool = DefaultNone,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge",
                                  "padding"] | None = DefaultNone,
                 id: str = DefaultNone,
                 is_visible: bool = DefaultNone):

        self.type = "Table"
        if rows is DefaultNone:
            rows = []
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
    
    def __add__(self, value: ListLike):
        if not isinstance(value, ListLike):
            raise TypeError
        value = list(value)
        attrs = {getattr(self, attr_name)
                 if attr_name != "rows"
                 else getattr(self, attr_name) + value
                 for attr_name in self.__slots__
                 if hasattr(self, attr_name)}
        return self.__class__(**attrs)
    
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
                 actions: Action | ListLike[Action] = DefaultNone,
                 fallback: Element = DefaultNone,
                 height: Literal["auto", "stretch"] = DefaultNone,
                 separator: bool = DefaultNone,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge",
                                  "padding"] | None = DefaultNone,
                 id: str = DefaultNone,
                 is_visible: bool = DefaultNone
                 ):
        self.type = "ActionSet"
        if actions is DefaultNone:
            actions = []
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
            if isinstance(actions, Action):
                actions = [actions]
            elif not isinstance(actions, list):
                actions = list(actions)
            return super().__setattr__(__name, __value)