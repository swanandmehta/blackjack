class Card:

    def __init__(self, **kwargs):
        self.type = kwargs.get("type")
        self.value = kwargs.get("value")
        self.point = kwargs.get("point")
        self.hidden = True

