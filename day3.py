def part1(grid, stepright, stepdown):
    i, j, count = 0, 0, 0

    # i is row, j is column

    while i < len(grid):
        if grid[i][j] == '#':
            count += 1

        j = (j+stepright) % len(grid[0])
        i = i+stepdown

    return count


def part2(grid):
    ans = 1
    for elem in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        ans *= part1(grid, elem[0], elem[1])

    return ans


if __name__ == '__main__':
    with open('day3.txt') as f:
        grid = [line.strip('\n') for line in f]

    print(part1(grid, 3, 1))
    print(part2(grid))
