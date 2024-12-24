def run_program(registers, program):
    ip = 0  # Instruction pointer
    output = []

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        ip += 2  # Move to next instruction after opcode and operand

        if opcode == 0:  # adv
            # A // (2^operand), result stored in A
            registers['A'] //= 2 ** operand

        elif opcode == 1:  # bxl
            # Bitwise XOR between B and operand, store in B
            registers['B'] ^= operand

        elif opcode == 2:  # bst
            # Store operand % 8 in B
            registers['B'] = operand % 8

        elif opcode == 3:  # jnz
            # Jump to operand if A != 0
            if registers['A'] != 0:
                ip = operand
            # Otherwise, instruction pointer increases by 2, already handled.

        elif opcode == 4:  # bxc
            # Bitwise XOR between B and C, store in B
            registers['B'] ^= registers['C']

        elif opcode == 5:  # out
            # Output operand % 8
            # Handle combo operand
            if operand == 4:
                output.append(registers['A'] % 8)
            elif operand == 5:
                output.append(registers['B'] % 8)
            elif operand == 6:
                output.append(registers['C'] % 8)
            else:
                output.append(operand % 8)

        elif opcode == 6:  # bdv
            # A // (2^operand), store result in B
            registers['B'] = registers['A'] // (2 ** operand)

        elif opcode == 7:  # cdv
            # A // (2^operand), store result in C
            registers['C'] = registers['A'] // (2 ** operand)

    return output

# Example usage
registers = {'A': 65804993, 'B': 0, 'C': 0}
program = [2,4,1,1,7,5,1,4,0,3,4,5,5,5,3,0]  # Example program from the question

# Run the program and get the output
output = run_program(registers, program)

# Print the output as a comma-separated string
print(','.join(map(str, output)))
