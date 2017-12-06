# New main file
from player import Player, test_win, inquire_help
from display import screen, start_screen, screen_next

start_screen()

player1 = Player('player1')
player2 = Player('player2')
player3 = Player('player3')

player_list = [player1, player2, player3]
player_dict = {'player1': player1, 'player2': player2, 'player3': player3}

for player in player_list:
    player.start_dict(player_dict)
    response = player.pickup_cards()

while True:
    for player in player_list:
        while True:
            test_win()
            action = input('> ')

            if action == 'inquire':
                response = player.inquire(player)
                screen(response, player)

            elif action == 'pick up':
                response = player.pickup_cards()
                screen(response, player)

            elif action == 'c':
                response = ['WE', 'ARE', 'NO', "LONGER"]
                screen(response, player)

            elif action == 'next':
                screen_next()
                break

            elif action == '':
                response = []
                screen(response, player)

            else:
                response = ['Derp']
                screen(response, player)
