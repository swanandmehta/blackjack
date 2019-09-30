# This service will manage the deck
from core import config_services
from core import logger_services
from core import input_services
from core import print_services

from services import player_service
from services import card_service
from services import dealer_service
from services import account_services

from entity import deck

from enums import user_status

from errors import invalid_choice
from errors import user_busted


def init():
    """  This is init method for deck service this allow us to setup deck at init of game """
    logger_services.log("Deck service Init : Started")
    game_config = config_services.get_configuration()

    no_of_users = game_config.get_no_of_users()

    players = player_service.get_players(no_of_users)

    cards = card_service.get_shuffled_cards()

    dealer = dealer_service.get_dealer()

    created_deck = create_deck(cards, players, dealer)

    game_config.set_deck(created_deck)

    logger_services.log("Deck service Init : Completed")


def create_deck(cards, players, dealer):
    """  This method will set up deck for usage """
    game_deck = deck.Deck(cards=cards, players=players, dealer=dealer)
    return game_deck


def deal_cards(deck_details):
    list_of_players = deck_details.get_players()

    for(index, player) in enumerate(list_of_players):
        card1 = deck_details.get_card()
        card2 = deck_details.get_card()
        card1.hidden = False
        card2.hidden = False
        player.cards = [card1, card2]
        player.status = user_status.PlayerStatus.in_game

    dealer = deck_details.get_dealer()

    card1 = deck_details.get_card()
    card2 = deck_details.get_card()

    card1.hidden = False
    card2.hidden = True
    dealer.cards = [card1, card2]


def start_round(deck_details):
    deal_player(deck_details)
    deal_dealer(deck_details)
    calculate_winner(deck_details)


def calculate_winner(deck_details):
    dealer = deck_details.get_dealer()
    list_of_players = deck_details.get_players()

    for (index, player) in enumerate(list_of_players):
        if dealer.status == user_status.PlayerStatus.busted and player.status != user_status.PlayerStatus.busted:
            account_services.update_normal_winning(player)
            print_services.print_winner(player)

        elif dealer.status != user_status.PlayerStatus.busted and player.status == user_status.PlayerStatus.busted:
            account_services.update_normal_losing(player)
            print_services.print_loser(player)
        elif dealer.status != user_status.PlayerStatus.busted and player.status != user_status.PlayerStatus.busted:
            if card_service.get_card_sum(dealer.cards) < card_service.get_card_sum(player.cards) < 21:
                account_services.update_normal_winning(player)
                print_services.print_winner(player)
            elif card_service.get_card_sum(dealer.cards) < card_service.get_card_sum(player.cards) == 21:
                account_services.update_blackjack_winning(player)
                print_services.print_winner(player)
            elif card_service.get_card_sum(dealer.cards) > card_service.get_card_sum(player.cards):
                account_services.update_normal_losing(player)
                print_services.print_loser(player)
            else:
                account_services.update_normal_drew(player)
                print_services.print_drew(player)


def deal_dealer(deck_details):
    dealer_service.reveal_dealers_hand(deck_details)

    print_services.reveal_dealers_hand()
    print_services.print_deck(deck_details)

    dealer = deck_details.get_dealer()
    list_of_players = deck_details.get_players()

    for (index, player) in enumerate(list_of_players):
        if player.status != user_status.PlayerStatus.busted and \
                card_service.get_card_sum(player.cards) > card_service.get_card_sum(dealer.cards):
            while True:
                try:
                    total = card_service.get_card_sum(dealer.cards)
                    input_val = "S"

                    if total < 17:
                        input_val = "H"

                    response = handle_input(input_val, deck_details, dealer)

                    if response:
                        break

                except user_busted.UserBusted:
                    print("Total is more then 21 dealer lost the game")
                    dealer.status = user_status.PlayerStatus.busted


def deal_player(deck_details):
    list_of_players = deck_details.get_players()
    for (index, player) in enumerate(list_of_players):
        while True:
            input_val = input_services.get_str_input("Would you like to hit or stay "
                                                     "\nEnter 'H' for Hit and 'S' for Stay and 'V' to view table\n")
            try:
                response = handle_input(input_val, deck_details, player)

                if response:
                    break

            except invalid_choice.InvalidChoice:
                print("Invalid Input please try again")
                pass
            except user_busted.UserBusted:
                print("Total is more then 21 You lost the game")
                player.status = user_status.PlayerStatus.busted
                break


def handle_input(input_val, deck_details, player):
    if input_val == 'H':
        card = deck_details.get_card()
        print_services.print_card(card, player)
        card.hidden = False
        player.cards.append(card)
        print_services.print_deck(deck_details)
        if card_service.get_card_sum(player.cards) > 21:
            raise user_busted.UserBusted
        return False
    elif input_val == 'S':
        return True
    elif input_val == 'V':
        print_services.print_deck(deck_details)
        return False
    else:
        raise invalid_choice.InvalidChoice


def check_for_winner(deck_details):
    list_of_players = deck_details.get_players()
    dealer_details = deck_details.get_dealer()

    dealer_sum = card_service.get_card_sum(dealer_details.cards)

    for(index, player) in enumerate(list_of_players):
        if 21 == card_service.get_card_sum(player.cards) and dealer_sum != 21:
            player.status = user_status.PlayerStatus.win
            player.account.bal = player.account.bal + (player.bet * 2)
        elif 21 == dealer_sum and card_service.get_card_sum(player.cards) < 21:
            player.status = user_status.PlayerStatus.lost
        elif 21 == dealer_sum and card_service.get_card_sum(player.cards) == 21:
            player.status = user_status.PlayerStatus.push
            player.account.bal = player.account.bal + (player.bet * 1)
