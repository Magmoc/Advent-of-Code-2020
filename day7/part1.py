from day7.read_input import read_input_file, invert_bag

bag_dict = read_input_file('input.txt')
inv_bag = invert_bag(bag_dict)
gold_bag_set = set()


def check_bags(bag_list):
    global bag_dict

    for bag in bag_list:
        gold_bag_set.add(bag)
        if bag in inv_bag:
            check_bags(inv_bag[bag])


if __name__ == '__main__':
    check_bags(inv_bag['shiny gold'])
    print(len(gold_bag_set))

# CORRECT!