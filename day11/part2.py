from copy import deepcopy


def adjacent(seats, row, col):
    count = 0

    step = 1

    check_list = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
    check_list.remove((0, 0)) # don't count itself as a valid direction

    while check_list:
        for direction in list(check_list): # need to copy list in order to loop over it while removing directions
            a, b = row + step * direction[0], col + step * direction[1]

            if a < 0 or b < 0:
                check_list.remove(direction)
                continue

            try:
                seat = seats[a][b]
                if seat != '.':
                    count += (seat == '#')
                    check_list.remove(direction)
            except:
                check_list.remove(direction)
        step += 1

    return count


def next_round(seats):
    new_seats = deepcopy(seats)

    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] == 'L' and adjacent(seats, i, j) == 0:
                new_seats[i][j] = '#'

            elif seats[i][j] == '#' and adjacent(seats, i, j) >= 5:
                new_seats[i][j] = 'L'

    yield new_seats
    yield from next_round(new_seats)


def print_seats(seats):
    print('-' * 2 * len(seats[0]))
    for row in seats:
        print(*row)


if __name__ == '__main__':
    with open('input.txt') as f:
        seats = [[y for y in x.strip('\n')] for x in f]

    # the border of 0's isn't necessary since you need to keep looking in one direction.
    round_gen = next_round(seats)
    prev_round = []
    current_round = next(round_gen)

    while current_round != prev_round:
        prev_round = current_round
        current_round = next(round_gen)

    # print_seats(current_round)
    print("Final seats: ")
    print_seats(current_round)
    occupied_num = sum(x.count('#') for x in current_round)
    print(f"\nTotal number of occupied seats: {occupied_num}")

# CORRECT!
