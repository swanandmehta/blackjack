# This service will deal with deelar functionality
from entity import dealer


def get_dealer():
    dealer_details = dealer.Dealer()
    return dealer_details


def reveal_dealers_hand(deck):
    dealer_details = deck.get_dealer()
    for (index, card) in enumerate(dealer_details.cards):
        card.hidden = False
