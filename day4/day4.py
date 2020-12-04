

if __name__ == '__main__':
    with open('passports.txt') as f:
        passports = [x for x in f]

    print(passports)

    passports = [x.strip('\n') for x in passports]
    print(passports)