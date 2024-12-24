import time

def read_line_from_file(filename):
    with open(filename, 'r') as file:
        # Read the single line and strip any surrounding whitespace or newline characters
        line = file.readline().strip()
    return line


def separate_odd_even_positions(elements):
    odd_position_string = []
    even_position_string = []

    for i, element in enumerate(elements):
        if i % 2 == 0:  # Even index (0-based), which is odd position (1-based)
            odd_position_string.append(element)
        else:  # Odd index (0-based), which is even position (1-based)
            even_position_string.append(element)

    return odd_position_string, even_position_string

# Example usage
filename = 'input.txt'  # Replace with your file path
line = read_line_from_file(filename)

disk_string = []
id = 0
for char in line:
    disk_string.append(int(char))
data_blocks, spaces = separate_odd_even_positions(disk_string)

goal_string = []
for index, data_block in enumerate(data_blocks):
    for index_elements in range(data_blocks[index]):
        goal_string.append(index)

    if index < len(data_blocks) - 1:
        for index_elements in range(spaces[index]):
            goal_string.append('.')

index_element = 0

for index_element, element in enumerate(goal_string):
    # print(f'Assessing index {index_element}')
    while goal_string[-1] == '.':
        goal_string = goal_string[:-1]

    # print(f'index_element is {index_element} and len(goal_string) is {len(goal_string)}')
    if index_element < len(goal_string) and element == '.':
        goal_string[index_element] = goal_string[-1]
        goal_string = goal_string[:-1]

    if index_element >= len(goal_string):
        print('Procedure completed')
        break
    index_element += 1

total_checksum = 0
for index_element, element in enumerate(goal_string):
    total_checksum += index_element*element
print(f'Total checksum is {total_checksum}')