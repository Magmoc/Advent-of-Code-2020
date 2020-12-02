with open('day1.txt') as f:
    nums = [int(x) for x in f]

for loc, i in enumerate(nums):
    for j in nums[loc:]:
        if i + j == 2020:
            print(i*j)