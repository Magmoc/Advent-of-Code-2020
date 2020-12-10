counter = 0


def recursive_adapter_list(adapters, adapter_list=[], indx=0):
    global counter

    for dif in range(1, 4): # Diffs of 1, 2 or 3 are allowed
        if adapters[indx] + dif in adapters:
            new_indx = adapters.index(adapters[indx] + dif)
            adapter_list.append(adapters[indx])
            recursive_adapter_list(adapters, adapter_list, new_indx)

    if indx == len(adapters)-1:
        counter += 1


def longest_adapter_list(adapters, adapter_list=[], indx=0):
    global counter

    for dif in range(1, 4): # Diffs of 1, 2 or 3 are allowed
        if adapters[indx] + dif in adapters:
            new_indx = adapters.index(adapters[indx] + dif)
            adapter_list.append(adapters[indx])
            if longest_adapter_list(adapters, adapter_list, new_indx):
                return adapter_list

    if indx == len(adapters)-1:
        return adapter_list


if __name__ == '__main__':
    with open('test.txt') as f:
        input_list = [eval(x.strip('\n')) for x in f]

    input_list.append(0) #voltage outlet
    input_list.append(max(input_list)+3) #Built-in adapter
    input_list.sort()

    longest_list = longest_adapter_list(input_list)
    print(longest_list)

# CORRECT!