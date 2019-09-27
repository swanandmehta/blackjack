class Deck:

    def __init__(self, **kwargs):
        """  init method for Deck class """
        self.cards = kwargs.get("cards")
        self.players = kwargs.get("players")
        self.dealer = kwargs.get("dealer")

    def get_cards(self):
        """  returns all available cards for individual deck  """
        return self.cards

    def get_players(self):
        """  returns all available players for the individual deck """
        return self.players

    def get_dealer(self):
        """  returns dealer for individual deck """
        return self.dealer

    def get_card(self):
        card = self.cards[0]
        self.cards.remove(card)
        return card
