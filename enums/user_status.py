import enum


class PlayerStatus(enum.Enum):
    none = 1
    push = 2
    busted = 3
    win = 4
    in_game = 5
    lost = 6
