### SHITTT SHIT i cant figure this out its not even that difficult
# lets get this going with only two sets of cards

player1 = ['A', '2', '10', 'J', '5']
player2 = ['3', '6', '7', '9', 'K']

players = {'player1': player1, 'player2': player2}

card = '3'

def inquire():
    while True:
        player = input('player')
        card = input('card: ')

        if card in player2:
            for i in player2:
                if i == card:
                    player1.append(i)
                    player2.remove(i)

        elif card not in player2:
            input("player2 has no such cards")
            break

        else:
            print("FAILURE")

print("START")
print(f'player1 cards: {player1}')
print(f'player2 cards: {player2}')

current_cards = len(player1)
inquire_run = 0

while True:
    action = input('> ')

    if action == 'inquire':

        if len(player1) == current_cards and inquire_run > 0:
            print("You have already asked and failed. Pick up a card instead.")

        elif len(player1) == current_cards and inquire_run == 0:
            inquire()
            inquire_run += 1

            if len(player1) > current_cards:
                input("NEXT TURN")
                break

        else:
            print("inquire NONE")


    elif action == 'pick':

        if len(player1) == current_cards and inquire_run == 0:
            print("You first have to ask for a card...")

        elif len(player1) == current_cards and inquire_run > 0:
            player1.append('2')
            print('Picked up one card.')

        elif len(player1) > current_cards and inquire_run == 1:
            print('Cant pick up anthing')
            input("NEXT TURN")
            break
        else:
            print('pick NONE')


    else:
        print("action NONE")

print("FINISH")
print(f'player1 cards: {player1}')
print(f'player2 cards: {player2}')
