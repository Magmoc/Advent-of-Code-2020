from copy import deepcopy

def adjacent_empty(seats, row, col):
    for i in range(-1, 2):
        for j in range(-1, 2):
            a = row + i
            b = col + j

            if seats[a+1][b+1] == '#' and not (a == row and b == col):
                return False

    return True


def next_round(seats):
    new_seats = deepcopy(seats)

    for i in range(len(seats)-2): # -2 to account for the border of 0's
        for j in range(len(seats[0])-2):
            if seats[i+1][j+1] == 'L' and adjacent_empty(seats, i, j):
                new_seats[i+1][j+1] = '#'

    yield new_seats
    yield from next_round(new_seats)


def print_seats(seats):
    print('-' * 2 * len(seats[0]))
    for row in seats[1:-1]:
        print(*row[1:-1])


if __name__ == '__main__':
    with open('test.txt') as f:
        seats = [[y for y in x.strip('\n')] for x in f]

    # add border of 0's
    seats.insert(0, ['0' for i in range(len(seats[0]))])
    seats.append(['0' for i in range(len(seats[0]))])

    for row in seats:
        row.insert(0, '0')
        row.append('0')

    round_gen = next_round(seats)
    print_seats(next(round_gen))
    print_seats(next(round_gen))
