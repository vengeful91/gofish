import random

types = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Player(object): # Player class
    center_deck = fill_cards(types)

    def __init__(self, name): # Basic Init Function
        self.cards = []
        self.name = name
        self.card_sets = []
        self.player_dict = {}


    def start_cards(self, cards): # Give player 5 cards to start
        """Adds 5 cards to self.cards"""
        for i in range(13):
            self.cards.append(cards.pop())


    def pickup_cards(self, cards): # Gives you 1, 2-4, 5 cards based on the senario
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


    def show_cards(self): # Shows the current players cards

        if self.cards == []:
            print("Your deck is empty.")

        else:
            print(f"{self.name}'s Deck: {self.cards}")


    def inquire(self, player_dict): # For asking for a card type
        #shoif asking_times
        choice_card = input('Enter the card:').upper()
        choice_player = input("Enter the player: ").lower()

        take = 0

        for card in self.player_dict[choice_player].cards:
            if choice_card in card:
                self.cards.append(choice_card)
                self.player_dict[choice_player].cards.remove(choice_card)
                take += 1

        if take > 0:
            self.inquire(self.player_dict)


    def set_of_cards(self):
        for i in types:
            if self.cards.count(i) >= 4:
                for x in range(4):
                    self.cards.remove(i)

                self.card_sets.append(i)


    def sort_cards(self): # Sorts self.cards by card value
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


    def turn(self, player_dict):

        self.player_dict = dict(player_dict)
        del self.player_dict[self.name]

        looping = True
        tries = 0

        while looping:

            if something: # check if everyone has cards and if the center deck is empty
                pass
            action = input('Action: ')

            elif action == 'inquire':
                inquire(player_dict)

            elif action == 'pick up cards' and tries == 1:
                pickup_cards(cards)






def fill_cards(types): # fills/shuffles cards list
    cards = []
    for single_type in types:
        for line in range(4):
            cards.append(single_type)

    random.shuffle(cards)
    return cards
