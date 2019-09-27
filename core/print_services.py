# This service will deal with printing or showing output to user


def print_deck(deck):
    dealer = deck.get_dealer()

    for (index, player) in enumerate(deck.get_players()):
        deck_details = ""
        deck_details = deck_details + "------------------------------------------------\n"

        deck_details = deck_details + get_card_details("Dealer", dealer.cards)
        deck_details = deck_details + "\n"
        deck_details = deck_details + get_card_details(player.name, player.cards)
        deck_details = deck_details + "\n"
        deck_details = deck_details + "Players bet : "+str(player.bet)+"\n"
        deck_details = deck_details + "Players bal : "+str(player.account.bal)+"\n"
        deck_details = deck_details + "------------------------------------------------\n"

        print(deck_details)


def get_card_details(name, cards):
    details = ""
    sum_of_points = 0
    for(index, card) in enumerate(cards):
        details = details + name
        details = details + " card "
        details = details + str(index+1)
        details = details + " is "
        if card.hidden is True:
            details = details + "*Hidden*"
            sum_of_points = sum_of_points + 0
        else:
            details = details + str(card.value) + " of " + card.type.name + " worth " + str(card.point) + " points"
            sum_of_points = sum_of_points + card.point

        details = details + "\n"

    details = details + "Sum of total points for "+name+" is " + str(sum_of_points) + " \n"

    return details

