from day8.read_input_file import read_input


def read_commands(command_list, accumulator=0, indx=0, indx_set=None, indx_set_indx=1):
    command = command_list[indx]

    if indx in indx_set:
        last_idx = list(indx_set)[-indx_set_indx]

        print("index, lastindex: ", indx, last_idx)

        old_command = command_list[last_idx]
        print("Old command: ", old_command)

        if old_command[0] == 'jmp': # if jmp it should nop
            accumulator = read_commands(command_list, accumulator, last_idx+1, indx_set, indx_set_indx)

        elif old_command[0] == 'nop': # if nop it should jmp
            accumulator = read_commands(command_list, accumulator, last_idx+eval(old_command[1]), indx_set, indx_set_indx)

        elif old_command[0] == 'acc': # if acc should evaluate previous old command
            indx_set_indx += 1
            accumulator = read_commands(command_list, accumulator, last_idx, indx_set, indx_set_indx)

    else:
        if command[0] == 'acc':
            accumulator += eval(command[1])

        elif command[0] == 'jmp':
            indx += eval(command[1]) - 1

        elif command[0] == 'nop':
            pass

        indx_set.add(indx)
        indx += 1
        accumulator = read_commands(command_list, accumulator, indx, indx_set, indx_set_indx)

    return accumulator

if __name__ == '__main__':
    input_list = read_input('input.txt')
    print(input_list)
    accumulator = read_commands(input_list, indx_set=set())
    print(accumulator)
