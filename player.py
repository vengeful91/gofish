# contains the player class
# each function in Player needs to return a list with the responses in it.
import random
from display import screen

def fill_cards(): # fills/shuffles cards list
    types = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cards = []
    for single_type in types:
        for line in range(4):
            cards.append(single_type)

    random.shuffle(cards)
    return cards


class Player(object):

    cards = fill_cards()

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.player_dict = {}

    def inquire(self, current_player):
        response = ['Enter the player and card.', '(Player, Card)',]
        screen(response, current_player)
        player, card = inquire_help()

        taken = 0

        if card in self.player_dict[player].cards:
            for i in self.player_dict[player].cards:
                if i == card:
                    self.cards.append(card)
                    taken += 1

            for i in range(taken):
                self.player_dict[player].cards.remove(card)

            response = [f"You've taken {taken} '{card}' cards from {player}",
                         "Ask again. Press Enter to continue."]

            screen(response, current_player)
            input()
            self.inquire(current_player)

        # broken. Also he might have already taken a card tbh
        elif card not in self.player_dict[player].cards:
            response = ["{} didn't have any '{}' cards.".format(player, card),
                         "Pick up a card instead"]
            return response

        else:
            response = ['Nothing']
            return response


    def pickup_cards(self):
        if Player.cards == []:
            response = ['The main deck is empty.',
                        'It is now the next players turn']
            return response


        elif len(self.cards) == 0 and len(Player.cards) > 5:
            for i in range(5):
                self.cards.append(Player.cards.pop())
            response = ['You picked up 5 cards.']
            return response


        elif len(self.cards) == 0 and len(Player.cards) <= 5:
            for i in range(len(cards)):
                self.cards.append(Player.cards.pop())
            response = ["You picked up {} cards".format(len(Player.cards))]
            return response


        elif len(self.cards) >= 1 and len(Player.cards) >= 1:
            self.cards.append(Player.cards.pop())
            response = ['You picked up 1 card.']
            return response

        else:
            response_list = ['pickup_cards else']
            return response_list

    def show_cards(self):
        self.sort_cards()

        if self.cards == []:
            print('Your deck is empty.')
        else:
            print(f'Cards: {self.cards}\n')

    def sort_cards(self):
        forward_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                        '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                        'J': 11, 'Q': 12, 'K': 13}
        backward_dict = {y:x for x, y in forward_dict.items()}

        output_list = []
        temp_list = []

        # forward
        for i in self.cards:
            temp_list.append(forward_dict[i])

        # sort
        temp_list.sort()

        # backward
        for i in temp_list:
            output_list.append(backward_dict[i])

        del self.cards[:]
        self.cards = output_list[:]

    def start_dict(self, player_dict):
        self.player_dict = dict(player_dict)
        del self.player_dict[self.name]


def test_win():
    pass
    # Tests to see if someone has won.


def inquire_help():
    response = ["Enter the player and card. (Player, Card)"]

    choice = input('> ')

    choices = choice.split(', ')

    player = choices[0].lower()
    card = choices[1].upper()

    return player, card
