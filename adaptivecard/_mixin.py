from typing import Any, Iterable, get_type_hints, get_args
from types import NoneType
from adaptivecard._typing import ListLike
from adaptivecard._utils import check_type, snake_to_camel
from functools import partial


class Mixin:
    __slots__ = ()

    def to_dict(self):
        dic = {}
        for attr_name, attr_value in zip(self.__slots__, map(partial(getattr, self), self.__slots__)):
            camel_formated_attr_name = snake_to_camel(attr_name)
            if hasattr(attr_value, "__slots__"):
                dic[camel_formated_attr_name] = attr_value.to_dict()
            elif isinstance(attr_value, ListLike):
                dic[camel_formated_attr_name] = [inner_value.to_dict() for inner_value in attr_value if hasattr(inner_value, "__slots__")]
            else:
                attr_value = attr_value if attr_value is not None else "none"
                dic[camel_formated_attr_name] = attr_value
        return dic

    def __setattr__(self, __name: str, __value: Any) -> None:
        type_hints = get_type_hints(self.__init__)
        # ignoring attributes that are set to default None
        if __value is None and not ((expected_type := type_hints.get(__name, Any) is NoneType)
                                or NoneType in get_args(expected_type)):
            return
        check_type(__name, __value, type_hints.get(__name, Any))
        super().__setattr__(__name, __value)
