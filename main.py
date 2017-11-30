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


    def inquire(self, player_dict):

        asking_player = 'player1'
        choice_card = input('Enter the card: ').upper()
        choice_player = input("Which player would you like to ask?")

        for card in player_dict[choice_player].cards:
            if choice_card in card:
                player_dict[asking_player].cards.append(choice_card)
                player_dict[choice_player].cards.remove(choice_card)

        player_dict[asking_player].show_cards()
        player_dict[choice_player].show_cards()


    # def something(): You can only do certain actions a certain amount of time.


cards = fill_cards()

player1 = Player('player1')
player2 = Player('player2')
player3 = Player('player3')
player4 = Player('player4')

player_dict = {'player1': player1, 'player2': player2,
               'player3': player3, 'player4': player4}

for i in player_dict:
    player_dict[i].start_cards(cards)
    player_dict[i].show_cards()


# make this thing possible for each player instance

player_dict['player1'].inquire(player_dict)
