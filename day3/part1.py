def count_trees(grid, stepright, stepdown):
    i, j, count = 0, 0, 0

    # i is row, j is column

    while i < len(grid):
        if grid[i][j] == '#':
            count += 1

        j = (j+stepright) % len(grid[0])
        i = i+stepdown

    return count


if __name__ == '__main__':
    with open('day3.txt') as f:
        grid = [line.strip('\n') for line in f]

    print(count_trees(grid, 3, 1))

# CORRECT!
