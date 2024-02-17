from typing import Any, Literal, Iterable
from adaptivecard._base_types import Element, ISelectAction
from adaptivecard._typing import ListLike
from adaptivecard._mixin import Mixin


class Text:
    __slots__ = ("type", "id", "is_multiline", "max_length", "placeholder",
                 "regex", "style", "inline_action", "value", "wrap", "error_message",
                 "is_required", "label", "fallback", "height", "separator", "spacing", "is_visible")

    def __init__(self,
                 id: str,
                 is_multiline: bool = None,
                 max_length: int = None,
                 placeholder : str = None,
                 regex: str = None,
                 style: str = None,
                 inline_action : ISelectAction = None,
                 value: str = None,
                 error_message: str = None,
                 is_required : bool = None,
                 label: str = None,
                 fallback: Element = None,
                 height: Literal["auto", "stretch"] = None,
                 separator: bool = None,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge",
                                  "padding"] = None,
                 is_visible: bool = None,
                 ):
        self.type = "Input.Text"
        self.id = id
        self.is_multiline = is_multiline
        self.max_length = max_length
        self.placeholder = placeholder
        self.regex = regex
        self.style = style
        self.inline_action = inline_action
        self.value = value
        self.error_message = error_message
        self.is_required = is_required
        self.label = label
        self.fallback = fallback
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.is_visible = is_visible


class Number:
    __slots__ = ("type", "id", "max", "min", "placeholder",
                 "value", "wrap", "error_message", "is_required", "label", "fallback",
                 "height", "separator", "spacing", "is_visible")

    def __init__(self,
                 id: str,
                 max: int = None,
                 min: int = None,
                 placeholder: str = None,
                 value: int = None,
                 error_message: str = None,
                 is_required : bool = None,
                 label: str = None,
                 fallback: Element = None,
                 height: Literal["auto", "stretch"] = None,
                 separator: bool = None,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge",
                                  "padding"] = None,
                 is_visible: bool = None,
                 ):

        self.type = "Input.Number"
        self.id = id
        self.max = max
        self.min = min
        self.placeholder = placeholder
        self.value = value
        self.error_message = error_message
        self.is_required = is_required
        self.label = label
        self.fallback = fallback
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.is_visible = is_visible


class Date:
    __slots__ = ("type", "id", "max", "min", "placeholder", "value", "error_message", "is_required",
                 "label", "fallback", "height", "separator", "spacing", "is_visible")
    def __init__(self,
                 id: str,
                 max: str = None,
                 min: str = None,
                 placeholder: str = None,
                 value: str = None,
                 error_message: str = None,
                 is_required : bool = None,
                 label: str = None,
                 fallback: Element = None,
                 height: Literal["auto", "stretch"] = None,
                 separator: bool = None,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge",
                                  "padding"] = None,
                 is_visible: bool = None,) -> None:

        self.type = "Input.Date"
        self.id = id
        self.max = max
        self.min = min
        self.placeholder = placeholder
        self.value = value
        self.error_message = error_message
        self.is_required = is_required
        self.label = label
        self.fallback = fallback
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.is_visible = is_visible


class Time:
    __slots__ = ("type", "id", "max", "min", "placeholder", "value", "error_message", "is_required",
                 "label", "fallback", "height", "separator", "spacing", "is_visible")
    def __init__(self,
                 id: str,
                 max: str = None,
                 min: str = None,
                 placeholder: str = None,
                 value: str = None,
                 error_message: str = None,
                 is_required : bool = None,
                 label: str = None,
                 fallback: Element = None,
                 height: Literal["auto", "stretch"] = None,
                 separator: bool = None,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge",
                                  "padding"] = None,
                 is_visible: bool = None):

        self.type = "Input.Time"
        self.id = id
        self.max = max
        self.min = min
        self.placeholder = placeholder
        self.value = value
        self.error_message = error_message
        self.is_required = is_required
        self.label = label
        self.fallback = fallback
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.is_visible = is_visible        


class DataQuery:
    __slots__ = ("type", "dataset", "count", "skip")
    def __init__(self,
                 dataset: str,
                 count: int = None,
                 skip: int = None
                 ):
        self.type = "Data.Query"
        self.dataset = dataset
        self.count = count
        self.skip = skip


class Choice:
    __slots__ = ("title", "value")
    def __init__(self,
                 title: str,
                 value: str
                 ):
        self.title = title
        self.value = value


class ChoiceSet(Mixin):
    __slots__ = ("type", "id", "choices", "choices_data", "is_multiselect", "style", "value",
                 "placeholder", "wrap", "error_message", "is_required", "label", "fallback",
                 "height", "separator", "spacing", "is_visible")
    def __init__(self,
                 id: str,
                 choices: Choice| ListLike[Choice] = None,
                 choices_data: DataQuery = None,
                 is_multiselect: bool = None,
                 style: Literal["compact", "extended", "filtered"] = None,
                 value: str = None,
                 placeholder: str = None,
                 wrap: bool = None,
                 error_message: str = None,
                 is_required : bool = None,
                 label: str = None,
                 fallback: Element = None,
                 height: Literal["auto", "stretch"] = None,
                 separator: bool = None,
                 spacing: Literal["default", "none", "small", "medium", "large", "extraLarge",
                                  "padding"] = None,
                 is_visible: bool = None,
                 ):

        self.type = "Input.ChoiceSet"
        self.id = id
        self.choices = choices
        self.choices_data = choices_data
        self.is_multiselect = is_multiselect
        self.style = style
        self.value = value
        self.placeholder = placeholder
        self.wrap = wrap
        self.error_message = error_message
        self.is_required = is_required
        self.label = label
        self.fallback = fallback
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.is_visible = is_visible

    def to_dict(self):
        dic = {}
        for attr_name in self.__slots__:
            if hasattr(self, attr_name):
                attr_value = getattr(self, attr_name)
                if attr_value == "choices_data":
                    attr_value = attr_value.replace('_', '.')
                dic[attr_name] = attr_value
        return dic

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "choices":
            choices = __value
            if isinstance(choices, Choice):
                choices = [choices]
            elif isinstance(choices, ListLike) and not isinstance(choices, list):
                choices = list(choices)
            
        return super().__setattr__(__name, __value)

