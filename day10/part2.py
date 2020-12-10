def create_diff_list(x):
    return [x[i+1]-x[i] for i in range(len(x)-1)]


def count_steps(input_list):
    ones_list = []
    old_idx = 0
    count = 1

    for i in range(len(input_list)):
        if input_list[i] == 3:
            ones_list.append(len(input_list[old_idx:i]))
            old_idx = i+1

    ones_multiplier = [1, 2, 4, 7]
    for i in ones_list:
        if i:
            count *= ones_multiplier[i-1]

    # 1 1 1 1
    # 1 1 2
    # 1 2 1
    # 2 1 1
    # 2 2
    # 1 3
    # 3 1
    #
    # 4 1's total = 7

    # 1 1 1
    # 1 2
    # 2 1
    # 3
    # 3 1's total = 4

    # 1 1
    # 2
    # 2 1's total = 2

    return count


if __name__ == '__main__':
    with open('input.txt') as f:
        input_list = [eval(x.strip('\n')) for x in f]

    input_list.append(0) #voltage outlet
    input_list.append(max(input_list)+3) #Built-in adapter
    input_list.sort()

    diff_list = create_diff_list(input_list)
    print(count_steps(diff_list))

# CORRECT!