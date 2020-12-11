from copy import deepcopy


def adjacent(seats, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            a = row + i
            b = col + j

            if seats[a+1][b+1] == '#' and not (a == row and b == col):
                count += 1

    return count


def next_round(seats):
    # print_seats(seats)
    new_seats = deepcopy(seats)

    for i in range(len(seats)-2): # -2 to account for the border of 0's
        for j in range(len(seats[0])-2):
            if seats[i+1][j+1] == 'L' and adjacent(seats, i, j) == 0:
                new_seats[i+1][j+1] = '#'

            elif seats[i+1][j+1] == '#' and adjacent(seats, i, j) >= 4:
                new_seats[i+1][j+1] = 'L'

    yield new_seats
    yield from next_round(new_seats)


def print_seats(seats):
    print('-' * 2 * len(seats[0]))
    for row in seats[1:-1]:
        print(*row[1:-1])


if __name__ == '__main__':
    with open('input.txt') as f:
        seats = [[y for y in x.strip('\n')] for x in f]

    # add border of 0's to easily look at eacht adjacent seat
    seats.insert(0, ['0' for i in range(len(seats[0]))])
    seats.append(['0' for i in range(len(seats[0]))])

    for row in seats:
        row.insert(0, '0')
        row.append('0')

    round_gen = next_round(seats)
    prev_round = []
    current_round = next(round_gen)

    while current_round != prev_round:
        prev_round = current_round
        current_round = next(round_gen)

    print("Final seats: ")
    print_seats(current_round)
    occupied_num = sum(x.count('#') for x in current_round)
    print(f"\nTotal number of occupied seats: {occupied_num}")

# CORRECT !