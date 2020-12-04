

if __name__ == '__main__':
    with open('passports.txt') as f:
        passports = [x.strip('\n') for x in f]

    print(passports)
    old = 0
    new_passports = []
    for index, elem in enumerate(passports):
        if not elem or index == len(passports):
            new = ' '.join(passports[old:index])
            new_passports.append(new)
            old = index

    print(new_passports)
    checklist = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    count = 0
    invalid = 0
    for idx, passport in enumerate(new_passports):
        if all(item in passport for item in checklist):
            count += 1

       # print('cid' in passport, passport.count(':'), all(item in passport for item in checklist))

    print(len(new_passports))
    print(count)
