import sys

def read_input_from_file(filename):
    """Read the word search matrix from a file."""
    with open(filename, 'r') as file:
        # Read lines from the file and strip newlines
        matrix = [line.strip() for line in file.readlines()]
    return matrix

def check_word_match(matrix, direction, startPoint):
    matrix_size = [len(matrix) - 1, len(matrix[0]) - 1]
    # check if word is too big
    word = "XMAS"
    row_end = startPoint[0] + (len(word) - 1)*direction[0]
    col_end = startPoint[1] + (len(word) - 1)*direction[1]
    if not (0 <= row_end <= matrix_size[0] and 0 <= col_end <= matrix_size[1]):
        return False

    for index, char in enumerate(word):
        new_point = [startPoint[0] + index*direction[0], startPoint[1] + index*direction[1]]
        if matrix[new_point[0]][new_point[1]] is not char:
            return False
    return True

def check_tree_match(matrix, startPoint):
    matrix_size = [len(matrix) - 1, len(matrix[0]) - 1]
    # check if word is too big

    if not (startPoint[0] - 1 >= 0 and startPoint[0] + 1 <= matrix_size[0]
        and startPoint[1] - 1 >= 0 and startPoint[1] + 1 <= matrix_size[1]):
        return False
    # Check upper diagonal
    up_left = [startPoint[0] - 1, startPoint[1] - 1]
    up_right = [startPoint[0] + 1, startPoint[1] - 1]
    down_left = [startPoint[0] - 1, startPoint[1] + 1]
    down_right = [startPoint[0] + 1, startPoint[1] + 1]
    if ((matrix[up_left[0]][up_left[1]] == 'M' and matrix[down_right[0]][down_right[1]] == 'S') or
            (matrix[up_left[0]][up_left[1]] == 'S' and matrix[down_right[0]][down_right[1]] == 'M')):
        if ((matrix[up_right[0]][up_right[1]] == 'M' and matrix[down_left[0]][down_left[1]] == 'S') or
                (matrix[up_right[0]][up_right[1]] == 'S' and matrix[down_left[0]][down_left[1]] == 'M')):
            return True



# Solution to quiz 1
directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
# Word to search for
word = "XMAS"

# Read the word search matrix from the file
matrix = read_input_from_file("input1.txt")
matrix_size = [len(matrix), len(matrix[0])]

word_count = 0
for row_index, row in enumerate(matrix):
    for col_index, col in enumerate(matrix):
        if matrix[row_index][col_index] == 'X':
            for direction in directions:
                startPoint = [row_index, col_index]
                match = check_word_match(matrix, direction, startPoint)
                if match:
                    word_count += 1

# Print the matches
print(f"Found '{word}' {word_count} times.")

# Solution to quiz 2

# Read the word search matrix from the file
matrix = read_input_from_file("input2.txt")
matrix_size = [len(matrix), len(matrix[0])]
word_count = 0
for row_index, row in enumerate(matrix):
    for col_index, col in enumerate(matrix):
        if matrix[row_index][col_index] == 'A':
            startPoint = [row_index, col_index]
            match = check_tree_match(matrix, startPoint)
            if match:
                word_count += 1

# Print the matches
print(f"Found '{word}' {word_count} times.")