# Figured out!!!! Good night
class Simple(object):

    def __init__(self, name):
        self.name = name
        self.players = {}

    def del_somethin(self):
        self.players = dict(players)
        del self.players[self.name]

player1 = Simple('player1')
player2 = Simple('player2')
player3 = Simple('player3')
player4 = Simple('player4')

players = {'player1': player1, 'player2': player2,
           'player3': player3, 'player4': player4}

player1.del_somethin()
player2.del_somethin()
player3.del_somethin()
player4.del_somethin()
input()
for i in player1.players:
    print(i)
input()
for i in player2.players:
    print(i)
