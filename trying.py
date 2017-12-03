
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
