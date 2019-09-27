class User:

    def __init__(self, **kwargs):
        """  init method for user sets name of the user """
        self.name = kwargs.get("name")
        self.cards = kwargs.get("cards")
        self.status = kwargs.get("status")

