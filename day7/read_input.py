import re


def read_input_file(file):
    with open('input.txt') as f:
        input_list = [re.split(' bags contain | bags, | bag, ', x.strip(' bags.\n')) for x in f]

    bag_dict = {}
    for elem in input_list:
        bag_dict[elem[0]] = elem[1:]


    print(bag_dict)
