def find_val(string, lower, upper, lower_str, upper_str, val=0):
    if string:
        new_upper = upper - 1 - (upper - lower) // 2 if string[0] == lower_str else upper
        new_lower = lower + 1 + (upper - lower) // 2 if string[0] == upper_str else lower

        val = new_lower # at last iteration new_lower = new_upper so it doesn't matter
        string = string[1:]

        val = find_val(string, new_lower, new_upper, lower_str, upper_str, val)

    return val


def find_seat(string):
    row = find_val(string[:7], 0, 127, 'F', 'B')
    col = find_val(string[-4:], 0, 7, 'L', 'R')

    return row, col


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line for line in f]

    id_list = []
    id_list1 = []

    for line in lines:
        row, col = find_seat(line)
        seat_id = row * 8 + col
        id_list.append(seat_id)

    id_list.sort()

    for index, i in enumerate(id_list[:-1]):
        if id_list[index+1] != i + 1:
            your_id = i+1

    print(your_id)

# CORRECT!