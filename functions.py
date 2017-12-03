import random

types = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def fill_cards(types): # fills/shuffles cards list
    cards = []
    for single_type in types:
        for line in range(4):
            cards.append(single_type)

    random.shuffle(cards)
    return cards


class Player(object): # Player class

    cards = fill_cards(types)

    def __init__(self, name): # Basic Init Function
        self.cards = []
        self.name = name
        self.card_sets = []
        self.player_dict = {}


    def start_cards(self, cards): # Give player 5 cards to start
        """Adds 5 cards to self.cards"""
        for i in range(5):
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


    def inquire(self, player_dict, choice_card, choice_player): # For asking for a card type
        taken = 0
        if choice_card in player_dict[choice_player].cards:

            for card in self.player_dict[choice_player].cards:
                if choice_card in card:
                    self.cards.append(choice_card)
                    self.player_dict[choice_player].cards.remove(choice_card)
                    taken += 1


    def look_for_sets(self): # searches through self.cards for sets of 4
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


        tries = 0

        while looping:

            action = input('Action: ')

            if False: # check if everyone has cards and if the center deck is empty
                pass



            elif action == 'inquire' and tries == 0:
                self.inquire(player_dict)
                tries += 1

            elif action == 'inquire' and tries > 0:
                print("You've already asked for a card.")
                print("Pick you a card instead.")

            elif action == 'pick up card' and tries == 0:
                print("You haven't asked for a card yet.")
                print("Ask one of the other players for a card.")

            elif action == 'pick up card' and tries == 1:
                self.pickup_cards(cards)

            elif action == 'look for set':
                self.look_for_sets()

            elif action == 'show cards':
                self.show_cards()

            elif action == 'sort cards':
                self.sort_cards()
                self.show_cards()

            else:
                print("I don't know what to...")
