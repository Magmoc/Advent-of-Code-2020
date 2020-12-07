from day7.read_input import read_input_file, invert_bag

bag_dict = read_input_file('input.txt')


def count_bags(sub_dict):
    count = 0

    if sub_dict:
        for bag, value in sub_dict.items():
            count += value * (1 + count_bags(bag_dict[bag]))
    else:
        return 0

    return count


if __name__ == '__main__':
    print(count_bags(bag_dict['shiny gold']))

