# This service will deal with players
from entity import player

from services import account_services

from core import config_services
from core import input_services

from errors import insuffciant_bal


def get_players(no_of_players):
    """
        This method will create no of players as per input
        And return the list of player objects
    """
    counter = 0
    no_of_players = int(no_of_players)
    list_of_players = []

    config = config_services.get_configuration()

    while counter < no_of_players:
        game_player = get_player(counter+1, config)
        list_of_players.append(game_player)
        counter = counter + 1

    return list_of_players


def get_player(counter, config):
    """
    This will take parameter of game config and counter to generate random name and account bal
    :param counter: int
    :param config: Configuration
    :return: Player
    """
    account = account_services.get_account(config.get_min_bal(), config.get_max_bal())
    game_player = player.Player(name=counter, cards=None, account=account)
    return game_player


def update_player_bet(player_details, bet):
    account_details = player_details.account
    try:
        if account_details.bal < bet:
            raise insuffciant_bal.InsuffciantBal
    except insuffciant_bal.InsuffciantBal :
        print("Invalid user bal setting it to max available bal")
        player_details.bet = account_details.bal
    else:
        player_details.bet = bet


def place_bets(deck):
    list_of_players = deck.get_players()
    for (index, player_details) in enumerate(list_of_players):
        bet = input_services.get_int_input("Please provide bet for the round\n")
        update_player_bet(player_details, bet)
