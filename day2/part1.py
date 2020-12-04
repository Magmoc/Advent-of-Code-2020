import re

if __name__ == '__main__':
    with open('day2.txt') as f:
        passwords = [x for x in f]

    passwords = [re.split('-| |: ', x.strip('\n')) for x in passwords]

    realpasswords = []

    for x in passwords:
        if eval(x[0]) <= x[-1].count(x[-2]) <= eval(x[1]):
            realpasswords.append(x)

    print(len(realpasswords))

# CORRECT!

