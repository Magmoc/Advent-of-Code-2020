from day7.read_input import read_input_file, invert_bag

bag_dict = read_input_file('input.txt')


def check_bags(bag, val=0):
    global bag_dict

    for bag, value in bag.items():
        # print(bag, value)
        if isinstance(value, int):
            if bag == 'shiny gold':
                val += 1
                break

            if bag in bag_dict:
                val = check_bags(bag_dict[bag], val)

        if isinstance(value, dict):
            val = check_bags(value, val)

    return val


if __name__ == '__main__':
    print(bag_dict)
    inv_bag = invert_bag(bag_dict)
    print(inv_bag)
    print(len(inv_bag))

    print(inv_bag['shiny gold'])
    # bag_dict = read_input_file('test.txt')
    # for key, value in bag_dict.items():
    #     print(key, value)
    # print("")
    # print(check_bags(bag_dict))
