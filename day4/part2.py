def year_check(year, length, min, max):
    return len(year) == length and (min <= eval(year) <= max)


if __name__ == '__main__':

    with open('passports.txt') as f:
        passports = [x.strip('\n') for x in f]

    old = 0
    new_passports = []
    for index, elem in enumerate(passports):
        if not elem or index == len(passports):
            new = ' '.join(passports[old:index])
            new_passports.append(new)
            old = index + 1

    checklist = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passwords = []

    for passport in new_passports:
        if all(item in passport for item in checklist):
            valid_passwords.append(passport)

    print(valid_passwords)
    dict_passport = {}

    for elem in valid_passwords:
        values = elem.split(" ")
        for pair in values:
            key, value = pair.split(":")
            if key == 'cid':
                continue
            if key in dict_passport:
                dict_passport[key].append(value)
            else:
                dict_passport[key] = [value]

    subcount = 0
    count = 0

    for i in range(len(valid_passwords)):
        # byr
        subcount = 0
        byr = dict_passport['byr'][i]
        if year_check(byr, 4, 1920, 2002):
            subcount += 1

        iyr = dict_passport['iyr'][i]
        if year_check(iyr, 4, 2010, 2020):
            subcount += 1

        eyr = dict_passport['eyr'][i]
        if year_check(eyr, 4, 2020, 2030):
            subcount += 1

        hgt = dict_passport['hgt'][i]
        if hgt[-2:] == 'cm' and 150 <= eval(hgt[:-2]) <= 193:
            subcount += 1

        elif hgt[-2:] == 'in' and 59 <= eval(hgt[:-2]) <= 76:
            subcount += 1

        hcl = dict_passport['hcl'][i]
        if hcl[0] == '#' and len(hcl) == 7 and all(letter in '0123456789abcdef' for letter in hcl[1:]):
            subcount += 1

        ecl = dict_passport['ecl'][i]
        if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            subcount += 1

        pid = dict_passport['pid'][i]
        if len(pid) == 9 and pid[0] == '0':
            subcount += 1

        if subcount == 7:
            count += 1

    print(count)