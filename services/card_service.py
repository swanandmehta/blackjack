# This service will work with cards
from enums import card_type

from entity import card

import random


def get_shuffled_cards():
    """
    This will return 1 deck of cards (52 in total)
    :return: list
    """
    card_list = get_cards()
    random.shuffle(card_list)
    return card_list


def get_cards(count=1):
    """
    This will return cards in non shuffled order
    :param count: int | it will return for how many card per deck are required
    for eg 1 will return 12 cards of per suit
    in total 52 cards
    :return: list of cards
    """
    list_of_cards = []

    spades = get_type_of_cards(card_type.CardType.SPADES, count)
    hearts = get_type_of_cards(card_type.CardType.HEARTS, count)
    diamonds = get_type_of_cards(card_type.CardType.DIAMONDS, count)
    clubs = get_type_of_cards(card_type.CardType.CLUBS, count)

    list_of_cards = list_of_cards + spades
    list_of_cards = list_of_cards + hearts
    list_of_cards = list_of_cards + diamonds
    list_of_cards = list_of_cards + clubs

    return list_of_cards


def get_type_of_cards(type_of_card, set_of_deck):
    """
    This function will return 13 cards of given suites * no of decks
    :param type_of_card: CardType
    :param set_of_deck: int
    :return: list of cards
    """

    deck_counter = 0
    list_of_cards = []

    while deck_counter < set_of_deck:
        counter = 0
        while counter < 13:
            card_details = create_card(type_of_card, counter+1)
            list_of_cards.append(card_details)
            counter = counter + 1

        deck_counter = deck_counter + 1

    return list_of_cards


def create_card(type_of_card, value_of_card):
    """
    This function will create the type of cards with the value of card
    :param type_of_card: CardType
    :param value_of_card: int
    :return: Card
    """
    card_details = card.Card(type=type_of_card, value=value_of_card, point=value_of_card if value_of_card < 11 else 10)
    return card_details


def get_card_sum(cards):
    total = 0

    for(index, card_details) in enumerate(cards):
        total = total + card_details.point

    return total
