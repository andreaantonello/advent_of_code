import re
import sys
import time
import os
from itertools import product
from copy import deepcopy
from functools import cache


def get_neighbors(matrix, row, col):
    """Get the neighbors of a letter in the matrix at position (row, col)."""
    neighbors_empty = {'point': None, 'letter': None}
    neighbors = []
    rows, cols = len(matrix), len(matrix[0])

    # Directions to check: up, down, left, right, and diagonals
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        # Check if the new position is within bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbors_new = deepcopy(neighbors_empty)
            neighbors_new['point'] = [new_row, new_col]
            neighbors_new['letter'] = matrix[new_row][new_col]
            neighbors.append(neighbors_new)

    return neighbors

def read_input(filename):
    """Read the input from a text file and return as a matrix (list of lists)."""
    with open(filename, 'r') as file:
        matrix = [list(line.strip()) for line in file.readlines()]
    return matrix

def count_different_elements(input_list, element):
    """Count elements in input_list that are different from the given element."""
    return sum(1 for x in input_list if x != element)

def search_dict_entry_by_point(dict, test_point):
    for item, entry in enumerate(dict):
        for point in entry['points']:
            if test_point == point:
                return item
    return None

# Example usage
filename = 'input.txt'
matrix = read_input(filename)


saved_areas_dict = []
empty_dict_entry = {'type': None, 'area': 0, 'perimeter': 0, 'points': [[4, 4], [1, 1]]}

for row_index, rows in enumerate(matrix):
    for col_index, letter in enumerate(rows):
        test_point = [row_index, col_index]

        if row_index == 0 and col_index == 0:
            saved_areas_dict.append({'type': letter, 'area': 1, 'perimeter': 0, 'points': [test_point]})


        neighbors = get_neighbors(matrix, row_index, col_index)
        for neighbor in neighbors:
            if neighbor['letter'] == letter:
                if search_dict_entry_by_point(saved_areas_dict, neighbor['point']) is None:
                    print(f'item {neighbor['point']} found in list {search_dict_entry_by_point(saved_areas_dict, neighbor['point'])}')
                    dict_entry = search_dict_entry_by_point(saved_areas_dict, test_point)
                    saved_areas_dict[dict_entry]['points'].append(neighbor['point'])
        print(saved_areas_dict)

        if row_index == 0 and col_index == 1:
            print(neighbors)
            sys.exit()

        #
        #
        #
        #
        #
        # print(neighbors)
        # sys.exit()
        #
        # for neighbor in neighbors:
        #     # Check each neighbour
        #     for entry in areas_dict:
        #         for point in entry['points']:
        #             if test_point == neighbor['point']:
        #                 pass
        #             else:
        #
        #
        #
        # for entry in saved_areas_dict:
        #     for point in entry['points']:
        #         if test_point == point:
        #             print('Point already accounted for')
        #             pass
        #     else:


            # print(entry)
        # If the letter is already in the dictionary, skip it
        # if letter not in areas_dict:
        #     letter_info[letter] = {'type': letter, 'area': 0, 'perimeter': 0, 'points': []}
        #
        # letter_info[letter]['area'] += 1
        # letter_info[letter]['points'].append(test_point)

        # edge_sides = 4 - len(neighbors)
        # edge_neighbors = count_different_elements(neighbors, letter)
        # letter_info[letter]['perimeter'] += edge_sides + edge_neighbors
        # print(f'Edge sides are {len(neighbors)}')
        # print(count_different_elements(neighbors, letter))

def calculate_total(letter_info):
    total = 0
    for letter, info in letter_info.items():
        total += info['area'] * info['perimeter']
    return total

print(saved_areas_dict)
# print(areas_dict)
