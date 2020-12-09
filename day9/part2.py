def find_weakness(inp_list, num_2_b_found):
    number = num_2_b_found

    for i in range(len(inp_list)):
        sum_list_sum = 0
        for j in range(i, len(inp_list)):
            sum_list_sum = sum(inp_list[i:j])
            if sum_list_sum > number:
                break

            if sum_list_sum == number:
                print(f"List from {inp_list[i]} to {inp_list[j]} with max {max(inp_list[i:j])} and min {min(inp_list[i:j])}")
                return max(inp_list[i:j]) + min(inp_list[i:j])


if __name__ == '__main__':
    with open('input.txt') as f:
        input_list = [eval(x.strip('\n')) for x in f]

    number_to_be_found = 731031916

    input_list = input_list[:input_list.index(number_to_be_found)]

    print(find_weakness(input_list, number_to_be_found))

# CORRECT