from entities.adaptivecard import AdaptiveCard

class Content:
    """Content é o elemento que recebe o AdaptiveCard e é adicionado à lista atachments, atributo de Message"""
    def __init__(self, card: AdaptiveCard):
        self.contentType = "application/vnd.microsoft.card.adaptive"
        self.content = card.__dict__