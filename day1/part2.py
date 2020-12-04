if __name__ == '__main__':
    with open('day1.txt') as f:
        nums = [int(x) for x in f]

    for loc, i in enumerate(nums):
        for loc2, j in enumerate(nums[loc:]):
            for loc3, k in enumerate(nums[loc2:]):
                if i + j + k == 2020:
                    print(i * j * k)

# CORRECT!
