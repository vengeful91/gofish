# I'm trying to create go fish! Except i can't remeber ever playing it... smart

import random

print("Welcome to Go Fish!")

def fill_cards(): # fills/shuffles cards list
    types = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cards = []
    for single_type in types:
        for line in range(4):
            cards.append(single_type)

    random.shuffle(cards)
    return cards

class Player(object): # Player class

    def __init__(self, name):
        self.cards = []
        self.name = name
        self.players = {}

    def fill_self_players(self, players): # deletes yourself from the players list/dict
        self.players = dict(players)
        del self.players[self.name]


    def start_cards(self, cards): #this function might be redundant...
        """Adds 5 cards to self.cards"""
        for i in range(5):
            self.cards.append(cards.pop())


    def pickup_cards(self, cards): #
        """Pick up from central deck"""

        if cards == []:
            print("The center deck is empty.")

        elif len(self.cards) == 0 and len(cards) > 5:
            for i in range(5):
                self.cards.append(cards.pop())

        elif len(self.cards) == 0 and len(cards) <= 5:
            for i in range(len(cards)):
                self.cards.append(cards.pop())

        elif len(self.cards) >= 1 and len(cards) >= 1:
            self.cards.append(cards.pop())

        else:
            print("Else")


    def show_cards(self): # should be in player1 only

        if self.cards == []:
            print("Your deck is empty.")

        else:
            print(f"{self.name} Deck: {self.cards}")


    def ask_cards(self, choice):

        for player_cards in self.players:
            for card in player_cards:
                if choice == card:
                    self.cards.append(player_cards.pop(choice))
                    print(f"{player_cards}")
                    again = True
                    self.show_cards()


    # enter what you want
    # search other players cards
    # give their type of cards to you
    # get nothing if they don't have any
    #input(">")




    # def something(): You can only do certain actions a certain amount of time.

def getting_started():
    cards = fill_cards()

    player1 = Player('player1')
    player2 = Player('player2')
    player3 = Player('player3')
    player4 = Player('player4')

    players_list = [player1, player2, player3, player4]
    players_dict = {'player1': player1, 'player2': player2,
                    'player3': player3, 'player4': player4}

    for player in players_list:
        player.fill_self_players(players_dict)
        player.pickup_cards(cards)
        player.show_cards()

    player1.ask_cards('4')

getting_started()
