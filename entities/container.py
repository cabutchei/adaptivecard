from typing import Union, List
from entities.mixin import Mixin

class Container(Mixin):
    """Um contâiner é um agrupamento de elementos"""
    def __init__(self, items = None, style: Union[None, str] = None, verticalContentAlignment: Union[None, str] = None, bleed: Union[None, bool] = None, minHeight: Union[None, str] = None, rtl: Union[None, bool] = None):
        self.type = "Container"

        if items == None or items == []:
            items = []
        else:
            try:
                items = [obj.__dict__ for obj in items]
            except:
                raise Exception("'Items' attribute must be a list of objects")
        self.items = items

        super().create_fields(locals())

        # attributes = [x for x in list(self.__init__.__code__.co_varnames) if x not in ["self", "attribute", "attributes", "items", "x"]]


        # for attribute in attributes:
        #     if locals()[attribute] != None:
        #         self.__dict__[attribute] = locals()[attribute]
        # print(self.__dict__)
        # self.__dict__.pop("attribute")
    def add_to_items(self, card_element):
        self.items.append(card_element.__dict__)