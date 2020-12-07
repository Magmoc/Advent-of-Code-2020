import re


def read_input_file(file):
    with open(file) as f:
        input_list = [re.split(' bags contain | bags, | bag, | bags.| bag.', x.strip('\n')) for x in f]
        for elem in input_list:
            elem.remove('')

    bag_dict = {}
    for elem in input_list:
        sub_dict = {}

        for sub_elem in elem[1:]:
            if sub_elem == 'no other':
                sub_dict = {'empty': 0}

            else:
                value, key = sub_elem.split(' ', 1)
                sub_dict[key] = eval(value)

        bag_dict[elem[0]] = sub_dict

    return bag_dict


def invert_bag(bag_dict):
    inverted_bag_dict = {}

    for bag, value in bag_dict.items():
        for loop_bag, loop_value in bag_dict.items():
            if bag in loop_value:
                if bag in inverted_bag_dict:
                    inverted_bag_dict[bag].append(loop_bag)
                else:
                    inverted_bag_dict[bag] = [loop_bag]

    return inverted_bag_dict
