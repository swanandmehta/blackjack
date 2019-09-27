from entity import user

from enums import user_status


class Dealer(user.User):

    def __init__(self, **kwargs):
        user.User.__init__(self, name="Dealer", cards=kwargs.get("cards"),
                           status=user_status.PlayerStatus.none)
