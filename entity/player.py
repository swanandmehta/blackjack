from entity import user
from enums import user_status


class Player(user.User):

    def __init__(self, **kwargs):
        """ init method for player """
        player_name = "Player " + str(kwargs.get("name"))
        user.User.__init__(self, name=player_name, cards=kwargs.get("cards"),
                           status=user_status.PlayerStatus.none)
        self.account = kwargs.get("account")
        self.bet = None
