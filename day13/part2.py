from math import gcd


def find_earliest(busses, lcm, time, n):
    lowest_multiple = n*lcm
    skip = False

    for bus, pos in busses[1:]:
        if (lowest_multiple + pos) % bus != 0:
            skip = True
            break

    if skip:
        lowest_multiple = find_earliest(busses, lcm, time, n+1)

    return lowest_multiple


if __name__ == '__main__':
    with open('test.txt') as f:
        input_list = [x.strip('\n') for x in f]

    time = eval(input_list[0])
    bus_pos = [indx for indx, x in enumerate(input_list[1].split(',')) if x != 'x']
    bus_ids = [eval(x) for x in input_list[1].split(',') if x != 'x']
    busses = list(zip(bus_ids, bus_pos))

    print(busses)

    lcm = bus_ids[0]
    for i, pos in busses[1:]:
        lcm = lcm * i // gcd(lcm, i)

    for i, pos in busses[1:]:
        print(f"i : {i} pos : {pos}")

    a = 3417
    for i, pos in busses[1:]:
        print((a+pos) % i)

    n = (time // lcm + 1)*lcm
    print(n)
    # earliest_time = find_earliest(busses, lcm, time, n)

    # print(earliest_time)
# CORRECT!
