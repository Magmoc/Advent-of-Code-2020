if __name__ == '__main__':
    with open('input.txt') as f:
        input_list = [x.strip('\n') for x in f]

    old = 0
    answers = []
    for index, elem in enumerate(input_list):
        if not elem:
            new = ''.join(input_list[old:index])
            answers.append(new)
            old = index + 1

    total = 0
    for elem in answers:
        s = set(elem)
        total += len(s)

    print(total)

# CORRECT!
