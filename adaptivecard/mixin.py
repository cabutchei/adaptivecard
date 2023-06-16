import json
from typing import Any, get_type_hints
from typeguard import check_type


class Mixin:    # essa é uma classe do tipo mixin. Não tem funcionalidade própria, serve para fornecer funcionalidade a outras classes.

    def to_dict(self):
        """
        Returns a json/dictionary representative of the card element
        """

        def remove_null_values(dic: dict) -> dict:
            return {key: dic[key] for key in dic if dic[key] is not None}

        def get_json_dic(obj):
            return {key for key in obj.__dict__ if key in obj.json_fields}

        dic = json.loads(json.dumps(self, default=lambda obj: remove_null_values(get_json_dic(obj))))
        return dic

    def get_local_vars(self) -> list:
        variables = [var for var in vars(self).keys() if var != 'self']
        return variables

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in (type_hints := get_type_hints(self.__init__)):
            check_type(__name, __value, type_hints[__name])
        if __name == 'type' and hasattr(self, __name):
            raise AttributeError(f"Can't set '{__name}' attribute")
        super().__setattr__(__name, __value)

    def __delattr__(self, __name: str) -> None:
        if __name == 'json_fields':
            raise AttributeError(f"Cannot delete '{__name}' attribute")
        if __name in self.json_fields:
            raise AttributeError('Cannot delete any card element attributes')
