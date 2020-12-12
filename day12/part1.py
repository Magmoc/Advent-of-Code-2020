def move(direction_tuple, value, coord):
    change = (value * direction_tuple[0], value * direction_tuple[1])
    return tuple(sum(x) for x in zip(coord, change))


if __name__ == '__main__':
    with open('input.txt') as f:
        nav_list = [x.strip('\n') for x in f]

    direction = 'E'  # starting direction east
    coord = (0, 0)  # East, North

    NESW_dict = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    rotation = "NESW"

    for instruction in nav_list:
        command = instruction[0]
        value = eval(instruction[1:])

        if command in "NESW":
            direction_tuple = NESW_dict[command]
            coord = move(direction_tuple, value, coord)

        elif command in "RL":
            steps = value//90 if command == "R" else -value//90
            direction = rotation[int((rotation.index(direction) + steps) % 4)]

        elif command == "F":
            coord = move(NESW_dict[direction], value, coord)

    print(f"The final coordinates are {coord}")
    print(f"The Manhattan distance is {abs(coord[0]) + abs(coord[1])}")

# CORRECT!