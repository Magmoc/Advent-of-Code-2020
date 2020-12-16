from pprint import pprint


def mask_bit(num, mask):
    bit = str(bin(num))[2:]
    bit = list('0'*(36-len(bit))+bit)

    mask_list = [(pos, val) for pos, val in enumerate(mask) if val != 'X']
    for pos, val in mask_list:
        bit[pos] = val

    return int('0b'+''.join(bit), 2)


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
        elif isinstance(pos, int):
            masked_bit = mask_bit(bit, mask)
            mem[pos] = masked_bit

    print(sum(mem.values()))

# CORRECT!