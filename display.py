# basics for the display system

import os

def screen(response_list, player):
    os.system('cls')
    print('Go fish')
    print('-' * 20)
    print("Player: ", player.name)
    print('- ' * 10)
    player.show_cards()
    for i in response_list:
        print(i)

def screen_next():
    os.system('cls')
    print('Go fish')
    print('- ' * 10)
    print("STARTING NEXT TURN!")

def start_screen():
    os.system('cls')
    print('Go fish')
    print('Starting Screen')
    print('Press ENTER to continue')


#response = []
#screen(response, player)
