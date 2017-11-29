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
            print(f"{self.name}'s Deck: {self.cards}")


    def inquire(self):
        pass # later



    # def something(): You can only do certain actions a certain amount of time.

def getting_started():
    cards = fill_cards()

    player1 = Player('player1')
    player2 = Player('player2')
    player3 = Player('player3')
    player4 = Player('player4')

    player_list = [player1, player2, player3, player4]

    for i in player_list:
        i.start_cards(cards)
    player1.show_cards()

    choice = input('Enter the card: ')

    # make this thing possible for each player instance
    
    temp = player_list[1:]
    for player in temp:
        for i in player.cards:
            if i == choice:
                player1.cards.append(i)

    player1.show_cards()


getting_started()
