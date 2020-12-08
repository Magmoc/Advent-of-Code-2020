from day8.read_input_file import read_input

accumulator = 0


def iter_jmp_nop(input_list):
    global accumulator

    for i in range(len(input_list)):
        accumulator = 0
        new_input_list = [x[:] for x in input_list]

        if new_input_list[i][0] == 'jmp':
            new_input_list[i][0] = 'nop'
        elif new_input_list[i][0] == 'nop':
            new_input_list[i][0] = 'jmp'

        if read_commands(new_input_list, indx_list=[]):
            return True


def read_commands(command_list, indx=0, indx_list=None):
    global accumulator

    if indx >= len(command_list):
        return True

    command = command_list[indx]

    if indx in indx_list:
        return False

    else:
        indx_list.append(indx)

        if command[0] == 'acc':
            accumulator += eval(command[1])

        elif command[0] == 'jmp':
            indx += eval(command[1]) - 1

        elif command[0] == 'nop':
            pass

        indx += 1
        if read_commands(command_list, indx, indx_list):
            return True


if __name__ == '__main__':
    input_list = read_input('input.txt')
    if iter_jmp_nop(input_list):
        print(accumulator)

# IT'S ALIVE!