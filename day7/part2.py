from day7.read_input import read_input_file, invert_bag

bag_dict = read_input_file('input.txt')


def count_bags(sub_dict, count=0):
    print(sub_dict)
    if sub_dict:
        for bag, value in sub_dict.items():
            if bag in bag_dict:
                print(count)
                count += value * count_bags(bag_dict[bag], count)
                return count

    else:
        return 1


if __name__ == '__main__':
    print(count_bags(bag_dict['shiny gold']))

