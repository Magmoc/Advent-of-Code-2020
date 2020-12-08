from day8.read_input_file import read_input

accumulator = 0
indx_set = set()


def read_commands(command_list, indx=0):
    global accumulator, indx_set

    command = command_list[indx]

    if indx in indx_set:
        pass

    else:
        if command[0] == 'acc':
            accumulator += eval(command[1])

        elif command[0] == 'jmp':
            indx += eval(command[1]) - 1

        elif command[0] == 'nop':
            pass

        indx_set.add(indx)
        indx += 1
        read_commands(command_list, indx)


if __name__ == '__main__':
    input_list = read_input('input.txt')
    print(input_list)
    read_commands(input_list)
    print(accumulator)

# CORRECT!
