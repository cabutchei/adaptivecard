from typing import Optional
from typing_extensions import Literal
from adaptivecard import AdaptiveCard
from adaptivecard._mixin import Mixin
from adaptivecard._base_types import Action


class ShowCard(Mixin, Action):
    __slots__ = ('type', 'title', 'icon_url', 'id', 'style', 'fallback', 'tooltip', 'is_enabled', 'mode', 'card')
    def __init__(self,
                 card: AdaptiveCard,
                 title: Optional[str] = None,
                 icon_url: Optional[str] = None,
                 id: Optional[str] = None,
                 style: Optional[Literal["default", "positive", "destructive"]] = None,
                 fallback: Optional[Action] = None,
                 tooltip: Optional[str] = None,
                 is_enabled: Optional[bool] = None,
                 mode: Optional[Literal["primary", "secondary"]] = None):
        
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
