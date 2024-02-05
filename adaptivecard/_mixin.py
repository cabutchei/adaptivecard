import json
from typing import Any, get_type_hints, Sequence
from typeguard import check_type
from adaptivecard._base_types import Element


class Mixin:

    protected_attributes = frozenset(('json_fields', 'type'))

    def to_dict(self):
        """
        Returns a json/dictionary representative of the card element
        """

        def get_json_dic(obj):
            return {attr_name: attr_value for attr_name in obj.__slots__ if hasattr(obj, attr_name)
                    and (attr_value := getattr(obj, attr_name)) is not None}

        # possível problema de circular reference ao passar o mesmo objeto em dois lugares diferentes do card. Averiguar depois.
        dic = json.loads(json.dumps(self, default=lambda obj: get_json_dic(obj)))
        return dic
    
    def is_sequence(self, value):
        if isinstance(value, Sequence) and not isinstance(value, str):
            return True
        return False

    def __setattr__(self, __name: str, __value: Any) -> None:
        type_hints = get_type_hints(self.__init__)
        if __name in type_hints:
                check_type(__value, type_hints[__name])
        if __name in self.protected_attributes and hasattr(self, __name):
            raise AttributeError(f"Can't set '{__name}' attribute")
        super().__setattr__(__name, __value)

    def __delattr__(self, __name: str) -> None:
        if __name in self.protected_attributes or hasattr(self, 'json_fields') and __name in self.json_fields:
            raise AttributeError(f"Cannot delete '{__name}' attribute")
