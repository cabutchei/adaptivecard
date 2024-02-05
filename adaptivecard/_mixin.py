import json
from typing import Any, Iterable, get_type_hints
from adaptivecard._utils import check_type
from functools import partial


class Mixin:

    def to_dict(self):
        """
        Returns a json/dictionary representative of the card element
        """
        dic = {}
        for attr_name, attr_value in zip(self.__slots__, map(partial(getattr, self), self.__slots__)):
            if hasattr(attr_value, "__slots__"):
                dic[attr_name] = attr_value.to_dict()
            elif isinstance(attr_value, Iterable) and not isinstance(attr_value, str):
                dic[attr_name] = [inner_value.to_dict() for inner_value in attr_value if hasattr(inner_value, "__slots__")]
            elif attr_value is not None:
                dic[attr_name] = attr_value
        return dic

    def __setattr__(self, __name: str, __value: Any) -> None:
        type_hints = get_type_hints(self.__init__)
        check_type(__name, __value, type_hints.get(__name, Any))
        super().__setattr__(__name, __value)
