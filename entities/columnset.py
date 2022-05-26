# from typing import Union, List
from typing import Union
from entities.mixin import Mixin
from entities.column import Column


class ColumnSet(Mixin):
    """ColumnSet define um grupo de colunas"""
    def __init__(self, columns: Union[None, Column] = None, style: Union[None, str] = None, bleed: Union[None, bool] = None,
                 minHeight: Union[None, str] = None, horizontalAlignment: Union[None, str] = None):
        self.type = "ColumnSet"
        if columns is None or columns == []:
            columns = []
        else:
            try:
                columns = [obj.__dict__ for obj in columns]
            except AttributeError:  # especifica exceção e a trata
                raise Exception("'Columns' attribute must be a list of objects")
        self.columns = columns
        super().create_fields(locals())

    def add_to_columns(self, column_element):
        self.columns.append(column_element.__dict__)