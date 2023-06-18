from adaptivecard.classes import AdaptiveCard
from typing import Optional
from adaptivecard.mixin import Mixin


class ShowCard(Mixin):
    def __init__(self,
                 card: AdaptiveCard,
                 title: Optional[str] = None,
                 iconUrl: Optional[str] = None,
                 id_: Optional[str] = None,
                 style: Optional[str] = None,
                 fallback = None,
                 tooltip: Optional[str] = None,
                 isEnabled: Optional[bool] = None,
                 mode: Optional[str] = None):
        
        self.type = "Action.ShowCard"
        self.title = title
        self.iconUrl = iconUrl
        self.id_ = id_
        self.style = style
        self.fallback = fallback
        self.tooltip = tooltip
        self.isEnabled = isEnabled
        self.mode = mode
        self.card = card
        self.json_fields = ('type', 'title', 'iconUrl', 'id_', 'style', 'fallback', 'tooltip', 'isEnabled', 'mode', 'card')
