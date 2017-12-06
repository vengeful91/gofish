# I'm trying to create go fish! Except i can't remeber ever playing it... smart
from functions import types, Player, Screen, fill_cards
import os

# # # # #
player1 = Player('player1')
player2 = Player('player2')
#player3 = Player('player3')
#player4 = Player('player4')

screen = Screen()

player_list = [player1, player2] #, player3, player4]
top_player_dict = {'player1': player1, 'player2': player2}
                   #,'player3': player3, 'player4': player4}

for i in player_list:
    i.pickup_cards(Player.cards)
    i.start_dict(top_player_dict)
# # # # #

screen.start_screen()
input()

try:
    while True:
        for i in player_list:
            screen.turn(screen, i)


except KeyboardInterrupt:
    print("\nExiting...")
<<<<<<< HEAD:old/main.py
 
=======
# https://youtu.be/psiq5imRIj8 Welcome to Earth
>>>>>>> 9c982fa09618558bd0f2d0dd3ab860d0ab6e1ba5:main.py
