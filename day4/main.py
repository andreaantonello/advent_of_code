import re

# Example input string (replace this with your file content)
with open("input.txt", "r") as file:
    input_string = file.read()

def mirror_matrix(matrix):
    # Reverse each row in the matrix
    mirrored = [row[::-1] for row in matrix]
    return mirrored

def transpose_matrix(matrix):
    # Use zip to transpose the matrix
    transposed = list(zip(*matrix))
    # Convert each tuple into a string
    transposed = [''.join(row) for row in transposed]
    return transposed

def count_horizontal_matches(matrix, word):
    rows = matrix.splitlines()
    row_count = 0
    for row in rows:
        row_count = row_count + row.upper().count(word)
    return row_count

def count_matches(matrix, word):
    """Count the horizontal, vertical, diagonal, and backward matches in the matrix."""
    word_len = len(word)
    rows = len(matrix)
    cols = len(matrix[0])
    match_count = 0

    # Horizontal matches (left to right)
    for r in range(rows):
        for c in range(cols - word_len + 1):
            if matrix[r][c:c+word_len] == word:
                match_count += 1

    # Horizontal matches (right to left)
    for r in range(rows):
        for c in range(word_len - 1, cols):
            if matrix[r][c:c-word_len:-1] == word:
                match_count += 1

    # Vertical matches (downwards)
    for c in range(cols):
        for r in range(rows - word_len + 1):
            if ''.join(matrix[r+i][c] for i in range(word_len)) == word:
                match_count += 1

    # Vertical matches (upwards)
    for c in range(cols):
        for r in range(word_len - 1, rows):
            if ''.join(matrix[r-i][c] for i in range(word_len)) == word:
                match_count += 1

    # Diagonal matches (top-left to bottom-right)
    for r in range(rows - word_len + 1):
        for c in range(cols - word_len + 1):
            if ''.join(matrix[r+i][c+i] for i in range(word_len)) == word:
                match_count += 1

    # Diagonal matches (bottom-left to top-right)
    for r in range(word_len - 1, rows):
        for c in range(cols - word_len + 1):
            if ''.join(matrix[r-i][c+i] for i in range(word_len)) == word:
                match_count += 1

    # Diagonal matches (top-right to bottom-left)
    for r in range(rows - word_len + 1):
        for c in range(word_len - 1, cols):
            if ''.join(matrix[r+i][c-i] for i in range(word_len)) == word:
                match_count += 1

    # Diagonal matches (bottom-right to top-left)
    for r in range(word_len - 1, rows):
        for c in range(word_len - 1, cols):
            if ''.join(matrix[r-i][c-i] for i in range(word_len)) == word:
                match_count += 1

    return match_count


word = "XMAS"
result = count_horizontal_matches(input_string, word)

print(mirror_matrix(word))

print(f"Found '{word}' {result} times.")