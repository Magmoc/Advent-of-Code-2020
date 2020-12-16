from math import gcd


def find_earliest(busses, n=1):
    lowest_multiple = n*(busses[0]['id'] - busses[0]['pos'])
    skip = False

    for bus in busses[1:]:
        if (lowest_multiple + bus['pos']) % bus['id'] != 0:
            skip = True
            break

    if skip:
        lowest_multiple = find_earliest(busses, n+1)

    return lowest_multiple


if __name__ == '__main__':
    with open('test.txt') as f:
        input_list = [x.strip('\n') for x in f]

    bus_pos = [indx for indx, x in enumerate(input_list[1].split(',')) if x != 'x']
    bus_ids = [eval(x) for x in input_list[1].split(',') if x != 'x']
    busses = [{'id': bus, 'pos': pos} for (bus, pos) in zip(bus_ids, bus_pos)]

    print(busses)

    for i in busses:
        print(i)

    break_loop = False
    earliest_time = busses[0]['id'] - busses[0]['pos']
    while True:
        for bus in busses[1:]:
            bus_id = bus['id']
            if (earliest_time + bus['pos']) % bus_id != 0:
                break

        if bus_id == busses[-1]['id']:
            break

        earliest_time += earliest_time

    print(earliest_time)
# CORRECT!
