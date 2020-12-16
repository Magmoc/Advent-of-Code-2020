import sys

sys.setrecursionlimit(2020+1)


def next_number(nums):
    last = nums[-1]

    if last in nums[:-1]:
        reverse_num = nums[::-1][1:]
        new_num = reverse_num.index(last)+1

    else:
        new_num = 0

    nums.append(new_num)

    yield nums
    yield from next_number(nums)


if __name__ == '__main__':
    with open('input.txt') as f:
        nums = [int(i) for i in f.readline().split(',')]

    num_gen = next_number(nums)
    nums = next(num_gen)

    while len(nums) != 2020:
        nums = next(num_gen)

    print(nums[-1])