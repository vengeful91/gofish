import random, os
 
types = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
go_fish_ascii = """
|   _____   ____    ______  _____   _____  _    _    |
|  / ____| / __ \  |  ____||_   _| / ____|| |  | |   |
| | |  __ | |  | | | |__     | |  | (___  | |__| |   |
| | | |_ || |  | | |  __|    | |   \___ \ |  __  |   |
| | |__| || |__| | | |      _| |_  ____) || |  | |   |
|  \_____| \____/  |_|     |_____||_____/ |_|  |_|   |
"""

def fill_cards(types): # fills/shuffles cards list
    cards = []
    for single_type in types:
        for line in range(4):
            cards.append(single_type)

    random.shuffle(cards)
    return cards


class Player(object): # Player class

    cards = fill_cards(types)
     # Basic Init Function
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.card_sets = []
        self.player_dict = {}

    # Gives you 1, 2-4, 5 cards based on the senario
    def pickup_cards(self, cards):
        """Pick up from central deck"""

        if cards == []:
            print("The center deck is empty.")

        elif len(self.cards) == 0 and len(cards) > 5:
            for i in range(5):
                self.cards.append(cards.pop())

        elif len(self.cards) == 0 and len(cards) <= 5:
            for i in range(len(cards)):
                self.cards.append(cards.pop())
            input(f"You've picked up {len(cards)}.")

        elif len(self.cards) >= 1 and len(cards) >= 1:
            self.cards.append(cards.pop())
            input("You've picked up 1 card.")

        else:
            input("Else")

    # Shows the current players cards
    def show_cards(self):
        self.sort_cards()

        if self.cards == []:
            print("Your deck is empty.")

        else:
            print(f"Your Deck: {self.cards}")

    # For asking for a card type
    def inquire(self):
        taken = 0
        print("You can ask any of the other players for a card.")
        choice_card = input('What card do you want to ask for? > ').upper()
        choice_player = input(f'Which player do you want to ask {choice_card} from? > ')

        if choice_card in self.player_dict[choice_player].cards:
            for card in self.player_dict[choice_player].cards:
                if choice_card == card:
                    self.cards.append(choice_card)
                    taken += 1

            for i in range(taken):
                self.player_dict[choice_player].cards.remove(choice_card)

            input(f"You've taken {taken} '{choice_card}' cards from {choice_player}.")

        if taken > 0:
            print("\nSince you've correctly asked for a card.")
            input("You can ask for another one.")
            self.inquire()


        else:
            input(f"{choice_player} didn't have any {choice_card}'s.")

    # searches through self.cards for sets of 4
    def look_for_sets(self):
        for i in types:
            if self.cards.count(i) >= 4:
                for x in range(4):
                    self.cards.remove(i)

                self.card_sets.append(i)

    # Sorts self.cards by card value
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


class Screen(object):

    def __init__(self):
        self.something = ''

    def start_screen(self):
        os.system('cls')

        print('|', '-' * 50, '|')
        print(go_fish_ascii)
        print('|', '-' * 50, '|')
        print(' ' * 12, "PRESS ENTER TO CONTINUE")

    def refresh_screen(self, current_player):
        os.system('cls')

        print("Go Fish")
        print('-' * 50)
        print("Player: ", current_player.name)
        current_player.show_cards()
        print('-' * 50)

    def turn(self, screen, current_player):

        tries = 0
        picked_up = 0
        looping = True

        while looping:
            screen.refresh_screen(current_player)

            choice = input("\n> ")

            if False: # check if everyone has cards and if the center deck is empty
                pass

            elif choice == 'options':
                print("Options:\n'inquire', 'pick up card', 'look for set',")

            elif choice == 'inquire' and tries == 0:
                current_player.inquire()
                tries += 1

            elif choice == 'inquire' and tries > 0:
                print("You've already asked for a card.")
                input("Pick up a card instead.")

            elif choice == 'pick up card' and tries == 0:
                print("You haven't asked for a card yet.")
                input("Ask one of the other players for a card. ")

            elif choice == 'pick up card' and tries == 1 and picked_up == 0:
                current_player.pickup_cards(Player.cards)
                picked_up += 1

            elif choice == 'pick up card' and tries == 1 and picked_up > 0:
                print("You've already picked up card.")
                input("This ends your turn...")
                looping = False

            elif choice == 'look for set':
                current_player.look_for_sets()

            # takes you to the next turn
            elif 'next' in choice:
                looping = False

            else:
                input("I don't know what to...")
