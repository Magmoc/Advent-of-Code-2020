
if __name__ == '__main__':
    with open('passports.txt') as f:
        passports = [x.strip('\n') for x in f]

    old = 0
    new_passports = []
    for index, elem in enumerate(passports):
        if not elem or index == len(passports):
            new = ' '.join(passports[old:index])
            new_passports.append(new)
            old = index+1

    checklist = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    count = 0
    invalid = 0
    for idx, passport in enumerate(new_passports):
        if all(item in passport for item in checklist):
            count += 1

    dict_passport = {}
    for key in checklist:
        dict_passport[key] = []

    for elem in new_passports:
        values = elem.split(" ")
        for pair in values:
            key, value = pair.split(":")
            if key == 'cid':
                continue
            if key in dict_passport:
                dict_passport[key].append(value)
            else:
                dict_passport[key] = [value]

    for i in range(len(new_passports)):
        pass

    print(dict_passport)