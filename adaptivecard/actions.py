from typing import Optional
from typing_extensions import Literal
from adaptivecard import AdaptiveCard
from adaptivecard._mixin import Mixin
from adaptivecard._base_types import Action


class ShowCard(Mixin, Action):
    __slots__ = ('type', 'title', 'icon_url', 'id', 'style', 'fallback', 'tooltip', 'is_enabled', 'mode', 'card')
    def __init__(self,
                 card: AdaptiveCard,
                 title: str | None = None,
                 icon_url: str | None = None,
                 id: str | None = None,
                 style: Literal["default", "positive", "destructive"] | None = None,
                 fallback: Action | None = None,
                 tooltip: str | None = None,
                 is_enabled: bool | None = None,
                 mode: Literal["primary", "secondary"] | None = None):
        
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
    def __init__(self,
                 url: str,
                 title: str | None = None,
                 id: str | None = None,
                 style: Literal["default", "positive", "destructive"] | None = None,
                 fallback: Action | None = None,
                 tooltip: str | None = None,
                 is_enabled: bool | None = None,
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
    def __init__(self,
                 data: str | dict | None,
                 associated_inputs: Literal["auto", "none"],
                 icon_url: str | None = None,
                 title: str | None = None,
                 id: str | None = None,
                 style: Literal["default", "positive", "destructive"] | None = None,
                 fallback: Action | None = None,
                 tooltip: str | None = None,
                 is_enabled: bool | None = None,
                 mode: Literal["primary", "secondary"] | None = None):

        self.type = "Action.Submit"
        self.data = data
        self.associated_inputs = associated_inputs
        self.icon_url = icon_url
        self.title = title
        self.id = id
        self.style = style
        self.fallback = fallback
        self.tooltip = tooltip
        self.is_enabled = is_enabled
        self.mode = mode