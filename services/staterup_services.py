# This file will create configuration for Game
from core import logger_services
from core import config_services
from core import print_services
from core import input_services

from services import deck_service
from services import player_service


def startup():
    """  Used as init method for application """
    logger_services.log("Game service Init : Started")
    config_services.init()
    deck_service.init()
    logger_services.log("Game service Init : Completed")


def start():
    config = config_services.get_configuration()
    deck = config.get_deck()
    # deck_service.check_for_winner(deck)
    start_game(deck)


def replay(deck):
    input_val = input_services.get_str_input("Would you like to continue the game? " +
                                             "Press 'Y' to continue anything else to quite \n")

    if input_val == 'Y':
        start_game(deck)


def start_game(deck):
    player_service.place_bets(deck)
    deck_service.deal_cards(deck)
    print_services.print_deck(deck)
    deck_service.start_round(deck)
    replay(deck)

