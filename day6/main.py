import re
from collections import defaultdict, deque
import sys
import time
import os
from copy import deepcopy

# Example input string (replace this with your file content)
with open("input.txt", "r") as file:
    input_string = file.read()

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def overwriteLines(lines, row_index, col_index, target):
    row = list(lines[row_index])
    row[col_index] = target
    lines[row_index] = ''.join(row)
    return lines

lines = input_string.strip().split("\n")

linesCopy = deepcopy(input_string.strip().split("\n"))
search_chars = ['v', '^', '<', '>']

locations = []
locationsVisited = []

count = 0
while True:
    found = False
    for row_index, row in enumerate(lines):
        for col_index, char in enumerate(row):
            if char in search_chars:
                locations.append((row_index, col_index, char))
                found = True
                break
        if found:
            break

    character = lines[row_index][col_index]
    locationsVisited.append([row_index, col_index])

    count = count + 1
    if row_index == 0 or row_index == len(lines)-1 or col_index == 0 or col_index == len(row)-1:
        print('Exited the puzzle!')
        break

    if character == '^':
        new_location = [row_index - 1, col_index]
    elif character == '>':
        new_location = [row_index, col_index + 1]
    elif character == 'v':
        new_location = [row_index + 1, col_index]
    elif character == '<':
        new_location = [row_index, col_index - 1]

    overwriteLines(lines, row_index, col_index, '.')
    new_character = lines[new_location[0]][new_location[1]]

    if new_character == '.':
        overwriteLines(lines, new_location[0], new_location[1], character)
    else:
        if character == '^':
            overwriteLines(lines, row_index, col_index + 1, '>')
        elif character == '>':
            overwriteLines(lines, row_index + 1, col_index, 'v')
        elif character == 'v':
            overwriteLines(lines, row_index, col_index - 1, '<')
        elif character == '<':
            overwriteLines(lines, row_index - 1, col_index, '^')

seen = set()
unique_list_ordered = []
for lst in locationsVisited:
    tup = tuple(lst)  # Convert list to tuple for hashing
    if tup not in seen:
        unique_list_ordered.append(lst)
        seen.add(tup)

# Print the result
print(unique_list_ordered)
print(f'Unique places visited are {len(unique_list_ordered)}')
