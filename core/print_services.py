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


def print_card(card, player):
    card_details = "\n------------------------------------------------\n"
    card_details = card_details + player.name + " "
    card_details = card_details + "drew "
    card_details = card_details + str(card.value) + " "
    card_details = card_details + "of "
    card_details = card_details + card.type.name + " "
    card_details = card_details + "worth " + str(card.point) + " points.\n"
    card_details = card_details + "------------------------------------------------\n"
    print(card_details)


def reveal_dealers_hand():
    card_details = "\n------------------------------------------------\n"
    card_details = card_details + "Dealer hand is revealed. \n"
    card_details = card_details + "------------------------------------------------\n"
    print(card_details)


def print_winner(player):
    card_details = "\n------------------------------------------------\n"
    card_details = card_details + "Congratulation " + player.name + "! You have won the round\n"
    card_details = card_details + "Updated bal : "+str(player.account.bal) + "\n"
    card_details = card_details + "------------------------------------------------\n"
    print(card_details)


def print_loser(player):
    card_details = "\n------------------------------------------------\n"
    card_details = card_details + "Sorry " + player.name + "! You have lost the round\n"
    card_details = card_details + "Updated bal : "+str(player.account.bal) + "\n"
    card_details = card_details + "------------------------------------------------\n"
    print(card_details)


def print_drew(player):
    card_details = "\n------------------------------------------------\n"
    card_details = card_details + player.name + "Round is drew\n"
    card_details = card_details + "Updated bal : "+str(player.account.bal) + "\n"
    card_details = card_details + "------------------------------------------------\n"
    print(card_details)
