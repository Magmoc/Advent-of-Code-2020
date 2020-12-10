# REDUNDANT because sorted input_list is longest list
def longest_adapter_list(adapters, adapter_list=[], indx=0):
    global counter

    for dif in range(1, 4): # Diffs of 1, 2 or 3 are allowed
        if adapters[indx] + dif in adapters:
            new_indx = adapters.index(adapters[indx] + dif)
            adapter_list.append(adapters[indx])
            if longest_adapter_list(adapters, adapter_list, new_indx):
                return adapter_list

    if indx == len(adapters)-1:
        adapter_list.append(adapters[indx])
        return adapter_list


counter = 0

# WONT WORK FOR INPUT SIZE THIS BIG
def recursive_adapter_list(adapters, adapter_list=[], indx=0):
    global counter

    for dif in range(1, 4): # Diffs of 1, 2 or 3 are allowed
        if adapters[indx] + dif in adapters:
            new_indx = adapters.index(adapters[indx] + dif)
            adapter_list.append(adapters[indx])
            recursive_adapter_list(adapters, adapter_list, new_indx)

    if indx == len(adapters)-1:
        counter += 1