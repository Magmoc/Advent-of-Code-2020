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
    col = find_val(string[-3:], 0, 7, 'L', 'R')

    return row, col


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line for line in f]

    max_id = 0

    for line in lines:
        row, col = find_seat(line)
        if row * 8 + col > max_id:
            max_id = row * 8 + col

    print(max_id)
