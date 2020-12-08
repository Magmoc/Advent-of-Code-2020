def read_input(file):
    with open(file) as f:
        input_list = [x.strip('\n').split(' ') for x in f]

    return input_list
