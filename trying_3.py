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
