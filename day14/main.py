import sys
import time

rows = 103
cols = 101

def create_blank_matrix(rows, cols):
    matrix = [['.' for _ in range(cols)] for _ in range(rows)]
    return matrix

positions = []
velocities = []

def read_input_from_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            p = parts[0].split('=')[1]  # Extract "0,4" from "p=0,4"
            v = parts[1].split('=')[1]  # Extract "3,-3" from "v=3,-3"
            positions.append(tuple(map(int, p.split(',')))[::-1])
            velocities.append(tuple(map(int, v.split(',')))[::-1])
    return positions, velocities

def sum_quadrants(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Find the middle row and column (integer division for odd dimensions)
    mid_row = rows // 2
    mid_col = cols // 2

    # Split into quadrants
    top_left = [row[:mid_col] for row in matrix[:mid_row]]
    top_right = [row[mid_col + 1:] for row in matrix[:mid_row]]
    bottom_left = [row[:mid_col] for row in matrix[mid_row + 1:]]
    bottom_right = [row[mid_col + 1:] for row in matrix[mid_row + 1:]]

    def safe_sum(submatrix):
        return sum(sum(0 if cell == "." else cell for cell in row) for row in submatrix)

    sum_top_left = safe_sum(top_left)
    sum_top_right = safe_sum(top_right)
    sum_bottom_left = safe_sum(bottom_left)
    sum_bottom_right = safe_sum(bottom_right)
    return sum_top_left*sum_top_right*sum_bottom_left*sum_bottom_right

def has_consecutive_blocks(matrix, test_consecutive_blocks=10):
    rows = len(matrix)
    cols = len(matrix[0])

    for col in range(cols):
        consecutive_count = 0
        for row in range(rows):
            if matrix[row][col] != ".":
                consecutive_count += 1
            else:
                consecutive_count = 0
            if consecutive_count >= test_consecutive_blocks:
                for check_row in range(row, rows):
                    if check_row + 2 < rows and all(matrix[check_row + i][col] != "." for i in range(3)):
                        return True
    return False


def plot_matrix(matrix):
    if has_consecutive_blocks(matrix):
        for row in matrix:
            for cell in row:
                if cell != ".":
                    print("■", end="")
                else:
                    print(" ", end="")
            print()
        return True
    else:
        return False


positions, velocities = read_input_from_file("input.txt")

# Part 1
seconds = 100
updated_position = [0, 0]
for second in range(0, seconds + 1):
    # Clea dates
    matrix = create_blank_matrix(rows, cols)
    for index, _ in enumerate(positions):
        updated_position[0] = (positions[index][0] + velocities[index][0]*second) % rows
        updated_position[1] = (positions[index][1] + velocities[index][1]*second) % cols

        if matrix[updated_position[0]][updated_position[1]] == ".":
            matrix[updated_position[0]][updated_position[1]] = 1
        else:
            matrix[updated_position[0]][updated_position[1]] += 1

print(f'Part 1 result is {sum_quadrants(matrix)}')

# Part 2
seconds = 100000
updated_position = [0, 0]
for second in range(0, seconds + 1):
    # Clea dates
    matrix = create_blank_matrix(rows, cols)
    for index, _ in enumerate(positions):
        updated_position[0] = (positions[index][0] + velocities[index][0]*second) % rows
        updated_position[1] = (positions[index][1] + velocities[index][1]*second) % cols

        if matrix[updated_position[0]][updated_position[1]] == ".":
            matrix[updated_position[0]][updated_position[1]] = 1
        else:
            matrix[updated_position[0]][updated_position[1]] += 1

    result = plot_matrix(matrix)
    if result:
        print(f'Part 2 result is second {second}')
        sys.exit()