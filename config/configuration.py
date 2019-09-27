# This class will deal with configuration of the game


class Configuration:

    def __init__(self, **kwargs):
        """  init method for Configuration class """

        # Total no of user which are playing at table
        self.no_of_users = kwargs.get("no_of_users")

        # min value for user bank account
        self.min_bal = kwargs.get("min_amount")

        # max value for user bank account
        self.max_bal = kwargs.get("max_amount")

        # The deck contains current game details Default to None
        self.deck = None

    def get_printable_values(self):
        """"  List all configuration values on console """
        details = "\nno of users = "+str(self.no_of_users)
        return details

    def get_no_of_users(self):
        """  get no of users playing at Deck """
        return int(self.no_of_users)

    def set_deck(self, deck):
        """  setter method for deck """
        self.deck = deck

    def get_deck(self):
        """  getter method for deck """
        return self.deck

    def get_min_bal(self):
        return int(self.min_bal)

    def get_max_bal(self):
        return int(self.max_bal)
