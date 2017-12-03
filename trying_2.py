# Solved!
# I just need to implement this into my Player class
# Should be really easy tbh

from random import randint
input_list = []
types = ['A', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'J', 'Q', 'K']

for i in range(10):
    x = randint(0, 12)
    input_list.append(types[x])
print(input_list)

def sort(unsorted_list):
    forward_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                    'J': 11, 'Q': 12, 'K': 13}

    backward_dict = {y:x for x, y in forward_dict.items()}

    sorted_list = []
    temp_list = []

    # forward
    for i in unsorted_list:
        temp_list.append(forward_dict[i])

    # sort
    temp_list.sort()

    # backward
    for i in temp_list:
        sorted_list.append(backward_dict[i])

    return sorted_list

output_list = sort(input_list)
print(output_list)
