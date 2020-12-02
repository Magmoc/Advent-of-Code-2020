import re


def part1(passwords):
    realpasswords = []

    for x in passwords:
        if eval(x[0]) <= x[-1].count(x[-2]) <= eval(x[1]):
            realpasswords.append(x)

    print(len(realpasswords))


def part2(passwords):
    realpasswords = []

    for x in passwords:
        low, up, letter, string = x
        low, up = eval(low), eval(up)
        if (string[low-1] == letter and string[up-1] != letter) or (string[low-1] != letter and string[up-1] == letter):
            realpasswords.append(x)

    print(len(realpasswords))


if __name__ == '__main__':
    with open('day2.txt') as f:
        passwords = [x for x in f]

    passwords = [re.split('-| |: ', x.strip('\n')) for x in passwords]

    part1(passwords)
    part2(passwords)
