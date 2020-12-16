from random import randint
import sys

def next_number(nums):
    last = nums[-1]

    if last[0] in [x[0] for x in nums[:-1]]:
        idx_list = [x for x in nums[:-1] if x[0] == last[0]]
        new_num = (last[1] - idx_list[0][1], last[1]+1)
        nums.remove(idx_list[0])

    else:
        new_num = (0, nums[-1][1]+1)

    nums.append(new_num)

    if len(nums) > 200:
        nums = nums[-200:]

    yield nums
    yield from next_number(nums)


if __name__ == '__main__':
    with open('input.txt') as f:
        nums = [(int(i), pos) for pos, i in enumerate(f.readline().split(','))]

    count = 0
    some_random_int = randint(3*10**3, 24*10**3)

    while nums[-1][1] <= 30000000-1:
        last = nums[-1]

        count += 1
        if count % some_random_int == 0:
            sys.stdout.write("\rCalculating" + "."*(count//some_random_int))
            sys.stdout.flush()

            if count % (some_random_int*10) == 0:
                count = 0

        if last[0] in [x[0] for x in nums[:-1]]:
            idx_list = [x for x in nums[:-1] if x[0] == last[0]]
            new_num = (last[1] - idx_list[0][1], last[1] + 1)
            nums.remove(idx_list[0])

        else:
            new_num = (0, nums[-1][1] + 1)

        nums.append(new_num)

        if len(nums) > 100:
            nums = nums[1:]

    print(nums[-1][0])
