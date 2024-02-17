from typing_extensions import Literal
from adaptivecard import AdaptiveCard
from adaptivecard._mixin import Mixin
from adaptivecard._base_types import Action
from adaptivecard._typing import ListLike


class ShowCard(Mixin, Action):
    __slots__ = ('type', 'title', 'icon_url', 'id', 'style', 'fallback', 'tooltip', 'is_enabled',
                 'mode', 'card')
    def __init__(self,
                 card: AdaptiveCard,
                 title: str = None,
                 icon_url: str = None,
                 id: str = None,
                 style: Literal["default", "positive", "destructive"] | None = None,
                 fallback: Action = None,
                 tooltip: str = None,
                 is_enabled: bool = None,
                 mode: Literal["primary", "secondary"] = None):
        
        self.type = "Action.ShowCard"
        self.title = title
        self.icon_url = icon_url
        self.id = id
        self.style = style
        self.fallback = fallback
        self.tooltip = tooltip
        self.is_enabled = is_enabled
        self.mode = mode
        self.card = card


class OpenUrl:
    __slots__ = ("url", "title", "id", "style", "fallback", "tooltip", "is_enabled", "mode")
    def __init__(self,
                 url: str,
                 title: str = None,
                 id: str = None,
                 style: Literal["default", "positive", "destructive"] | None = None,
                 fallback: Action  = None,
                 tooltip: str = None,
                 is_enabled: bool = None,
                 mode: Literal["primary", "secondary"] | None = None):

        self.type = "Action.OpenUrl"
        self.title = title
        self.url = url
        self.id = id
        self.style = style
        self.fallback = fallback
        self.tooltip = tooltip
        self.is_enabled = is_enabled
        self.mode = mode


class Submit:
    __slots__ = ("data", "associated_inputs", "title", "icon_url", "id", "style", "fallback",
                 "tooltip", "is_enabled", "mode")
    def __init__(self,
                 data: dict,
                 associated_inputs: Literal["auto", "none"], 
                 title: str = None,
                 icon_url: str = None,
                 id: str = None,
                 style: Literal["default", "positive", "destructive"] = None,
                 fallback: Action = None,
                 tooltip: str = None,
                 is_enabled: bool = None,
                 mode: Literal["primary", "secondary"] = None):

        self.type = "Action.ToggleVisibility"
        self.data = data
        self.associated_inputs = associated_inputs
        self.title = title
        self.icon_url = icon_url
        self.id = id
        self.style = style
        self.fallback = fallback
        self.tooltip = tooltip
        self.is_enabled = is_enabled
        self.mode = mode


class TargetElement:
    __slots__ = ("element_id", "is_visible")
    def __init__(self,
                 element_id: str,
                 is_visible: bool):
        self.element_id = element_id
        self.is_visible = is_visible


class ToggleVisibilty:
    __slots__ = ("data", "target_elements", "icon_url", "title", "id", "style", "fallback",
                 "tooltip", "is_enabled", "mode")
    def __init__(self,
                 data: str | dict,
                 target_elements: ListLike[TargetElement],
                 icon_url: str = None,
                 title: str = None,
                 id: str = None,
                 style: Literal["default", "positive", "destructive"] = None,
                 fallback: Action = None,
                 tooltip: str = None,
                 is_enabled: bool = None,
                 mode: Literal["primary", "secondary"] = None):
        self.data = data
        self.target_elements = target_elements
        self.icon_url = icon_url
        self.title = title
        self.id = id
        self.style = style
        self.fallback = fallback
        self.tooltip = tooltip
        self.is_enabled = is_enabled
        self.mode = mode

    
class Execute:
    __slots__ = ()
    def __init__(self,
                 verb: str = None,
                 data: dict = None,
                 associated_inputs: Literal["auto", "none"] = None,
                 title: str = None,
                 icon_url: str = None,
                 id: str = None,
                 style: Literal["default", "positive", "destructive"] = None,
                 fallback: Action = None,
                 tooltip: str = None,
                 is_enabled: bool = None,
                 mode: Literal["primary", "secondary"] = None):
        pass