
if __name__ == '__main__':
    with open('input.txt') as f:
        input_list = [x.strip('\n') for x in f]

    time = eval(input_list[0])
    bus_ids = [eval(x) for x in input_list[1].split(',') if x != 'x']

    wait_time = max(bus_ids)
    for x in bus_ids:
        bus_wait = (time // x + 1)*x - time
        if bus_wait < wait_time:
            wait_time = bus_wait
            earliest_bus = x

    print(f"Take bus {earliest_bus} and wait {wait_time}: {wait_time*earliest_bus}")
# CORRECT!
