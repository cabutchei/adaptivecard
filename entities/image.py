import requests
from typing import Union
from mixin import Mixin

from adaptivecard import AdaptiveCard
from message  import Message
from content import Content

class Image(Mixin):
    def __init__(self, url: str, altText: Union[None, str] = None, backgroundColor: Union[None, str] = None, height: Union[None, str] = None, horizontalAlignment: Union[None, str] = None, selectAction: Union[None, str] = None) -> None:
        self.type = "Image"
        super().create_fields(locals())
    
    def to_dict(self):
        return self.__dict__

url = "https://images.squarespace-cdn.com/content/v1/54e7a1a6e4b08db9da801ded/7f2dae36-5650-4b84-b184-684f46fe68aa/98.jpg"
image = Image(url = url)
card = AdaptiveCard(body = [image])
content = Content(card)
message = Message([content]).__dict__
x = requests.post(json = message, url = "https://resourceitsolutions.webhook.office.com/webhookb2/aa81c831-b73b-4c92-88a4-7d172d700ad4@65736186-3d24-4583-af75-0a3383d75476/IncomingWebhook/b7ec827e3c9c4705b3cc76fce3989caa/7c61c19e-6105-4c14-94bd-9834a839ec65")
print(x.text)