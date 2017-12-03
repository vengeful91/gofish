# I'm trying to create go fish! Except i can't remeber ever playing it... smart
from functions import types, Player, fill_cards

# # # # #
print("Welcome to Go Fish!\n")

player1 = Player('player1')
player2 = Player('player2')
player3 = Player('player3')
player4 = Player('player4')

player_list = [player1, player2, player3, player4]
top_player_dict = {'player1': player1, 'player2': player2,
                   'player3': player3, 'player4': player4}

for i in player_list:
    i.start_cards(Player.cards)
# # # # #


try:
    while True:
        player1.turn(top_player_dict)
        player2.turn(top_player_dict)
        player3.turn(top_player_dict)
        player4.turn(top_player_dict)

except KeyboardInterrupt:
    print("\nExiting...")
