if __name__ == '__main__':
    with open('input.txt') as f:
        input_list = [eval(x.strip('\n')) for x in f]

    input_list.append(0) #voltage outlet
    input_list.sort()

    counter_1 = 0
    counter_3 = 1 #built-in adapter

    for i in range(len(input_list)-1):
        dif = input_list[i+1] - input_list[i]
        if dif == 1:
            counter_1 += 1
        elif dif == 3:
            counter_3 += 1

    print(f"1 jolt differences: {counter_1}, 3 jolt differences {counter_3}")
    print(f"Answer is {counter_1*counter_3}")

# CORRECT!