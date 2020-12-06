if __name__ == '__main__':
    with open('input.txt') as f:
        input_list = [x.strip('\n') for x in f]

    old = 0
    answers = []
    for index, elem in enumerate(input_list):
        if not elem:
            new = input_list[old:index]
            answers.append(new)
            old = index + 1

    total = 0
    for group in answers:
        set_list = [set(person) for person in group]

        intersect_set = set.intersection(*set_list)

        total += len(intersect_set)

        del intersect_set, set_list

    print(total)

# CORRECT!
