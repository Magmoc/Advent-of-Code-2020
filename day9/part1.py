def check_number(inp_list, indx):
    number = inp_list[indx]
    bounded_list = inp_list[indx-25: indx]
    for i, x in enumerate(bounded_list):
        for j, y in enumerate(bounded_list):
            if x+y == number and x != y:
                return True


if __name__ == '__main__':
    with open('input.txt') as f:
        input_list = [eval(x.strip('\n')) for x in f]

    for i in range(25, len(input_list)):
        if not check_number(input_list, i):
            print(input_list[i])

# IT"S ALIVE