go_fish_ascii = """
|   _____   ____    ______  _____   _____  _    _    |
|  / ____| / __ \  |  ____||_   _| / ____|| |  | |   |
| | |  __ | |  | | | |__     | |  | (___  | |__| |   |
| | | |_ || |  | | |  __|    | |   \___ \ |  __  |   |
| | |__| || |__| | | |      _| |_  ____) || |  | |   |
|  \_____| \____/  |_|     |_____||_____/ |_|  |_|   |
"""

class Simple(object):
    v1 = [3, 2, 1]

    def __init__(self, name):
        self.name = name
        self.v1 = ['different']

    def print_something(self):
        print(Simple.v1)

    def remove_something(self):
        destroy = Simple.v1.pop()
        self.v1.append(destroy)


first = Simple('first')
second = Simple('second')

first.print_something()
second.print_something()

first.remove_something()

first.print_something()
second.print_something()
