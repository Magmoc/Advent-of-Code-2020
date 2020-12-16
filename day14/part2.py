from pprint import pprint


def mask_bit(pos, mask):
    adress = '{0:036b}'.format(pos)
    adress_list = [""]

    for i, mbit in enumerate(mask):
        if mbit == '0':
            adress_list = [x + adress[i] for x in adress_list]

        elif mbit == '1':
            adress_list = [x + '1' for x in adress_list]

        else:
            adress_list = [x + str(i) for i in range(2) for x in adress_list]

    return [int(pos, 2) for pos in adress_list] # convert to dec


if __name__ == '__main__':
    with open('input.txt') as f:
        input_list = [x.strip('\n').split(" = ") for x in f]
        input_list = [[eval(key.strip('mem[').strip(']')), eval(val)] if key != 'mask' else [key, val]
                      for key, val in input_list]

    mem = {}
    mask = 'X'*36
    for pos, bit in input_list:
        if pos == 'mask':
            mask = bit
        else:
            pos_list = mask_bit(pos, mask)
            for adress in pos_list:
                mem[adress] = bit

    print(sum(mem.values()))

# CORRECT!