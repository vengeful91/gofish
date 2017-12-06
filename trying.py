# basics for the display system
 
import os

def screen(response_list):
    os.system('cls')
    print('Go fish')
    print('- ' * 10)
    for response in response_list:
        print(response)

response_list = []
screen(response_list)

while True:
    action = input('> ')

    if action == 'a':
        response_list = ['Yeah!', 'You did it!']
        screen(response_list)

    elif action == 'b':
        response_list = ['Nope!', 'You got it wrong!']
        screen(response_list)

    elif action == 'c':
        response_list = ['WE', 'ARE', 'NO', "LONGER"]
        screen(response_list)

    else:
        response_list = ["I'm sorry what?"]
        screen(response_list)
