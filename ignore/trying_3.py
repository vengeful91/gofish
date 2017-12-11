    def turn(self, player_dict):
        print(f"It is {self.name}'s Turn.")
        self.show_cards()

        self.player_dict = dict(player_dict)
        del self.player_dict[self.name]


        tries = 0
        picked_up = 0
        looping = True

        while looping:

            action = input('Action: ')

            if False: # check if everyone has cards and if the center deck is empty
                pass

            elif action == 'options':
                print("Options:\n'inquire', 'pick up card', 'look for set',", end='')
                print("'look at my cards', 'sort cards'")


            elif action == 'inquire' and tries == 0:
                self.inquire()
                tries += 1

            elif action == 'inquire' and tries > 0:
                print("You've already asked for a card.")
                print("Pick up a card instead.")

            elif action == 'pick up card' and tries == 0:
                print("You haven't asked for a card yet.")
                print("Ask one of the other players for a card.")

            elif action == 'pick up card' and tries == 1:
                self.pickup_cards(Player.cards)
                picked_up += 1

            elif action == 'look for set':
                self.look_for_sets()

            elif action == 'look at my cards':
                self.show_cards()

            elif action == 'sort cards':
                self.show_cards()

            elif action == "show all":
                for k, v in player_dict.items():
                    v.show_cards()

            # takes you to the next turn
            #elif tries > 0 or picked_up > 0:
            #    looping = False

            else:
                print("I don't know what to...")


#################################################################################




else:
    response = ['def inquire(): failed: Nothing']
    return response


# BOLD MOVE YOUNG SKYWALKER

    def inquire(self, current_player):
        taken = 0
        cycle = 0
        while True:
            print('LOCATED IN INQUIRE')
            input()
            cycle += 1

            player, card = inquire_help(current_player)

            if card in self.player_dict[player].cards:
                # take cards from other player
                # you can take another card from someone
                for i in self.player_dict[player].cards:
                    if i == card:
                        self.cards.append(card)
                        taken += 1

                    for i in range(taken):
                        self.player_dict[player].cards.remove(card)

                response = [f"You've taken {taken} '{card}' cards from {player}",
                         "Ask again. Press Enter to continue."]
                screen(response, current_player)


            elif card not in self.player_dict[player].cards and taken == 0:
                response = ["{} didn't have any '{}' cards.".format(player, card),
                            "Pick up a card instead"]
                self.pickup_cards()
                force = ''
                return response, force

            elif card not in self.player_dict[player].cards and taken > 0:
                # you fail at taking a card
                # next turn
                force = 'next'
                return response, force
                break

# crap

while True:
    for player in player_list:
        tryed = False
        force = ''
        while True:
            print("LOCATED IN NEW_MAIN")
            test_win()
            action = input('> ')

            if action == 'inquire' and not tryed:
                response, force = player.inquire(player)
                screen(response, player)
                tryed = True

            elif action == 'inquire' and tryed:
                response = ['You have already asked for a card and failed.',
                            'Pick up a card instead.']
                screen(response, player)

            elif action == 'pick up':
                response = player.pickup_cards()
                screen(response, player)

            elif action == 'c':
                response = ['WE', 'ARE', 'NO', "LONGER"]
                screen(response, player)

            elif action == 'next' or force == 'next':
                screen_next()
                break

            elif action == '':
                response = []
                screen(response, player)

            else:
                response = ['Derp']
                screen(response, player)
