import re
from collections import defaultdict, deque
import sys
import time

def import_input_file(filename):
    with open(filename, "r") as file:
        grids = file.read().strip().split("\n\n")
    return grids

def count_hash_from_file(grids):
    keys = []
    locks = []
    for grid in grids:
        rows = grid.split("\n")
        column_count = len(rows[0])
        counts = [-1] * column_count
        for row in rows:
            for col_index, char in enumerate(row):
                if char == "#":
                    counts[col_index] += 1
                # print(col_index)
        if grid[0] == '.':
            keys.append(counts)
        else:
            locks.append(counts)
    return keys, locks

filename = "input.txt"

# Get the counts
grids = import_input_file(filename)
keys, locks = count_hash_from_file(grids)

threshold = 5
possible_combinations = 0
for index_key, key in enumerate(keys):
    for index_lock, lock in enumerate(locks):
        combination = [a + b for a, b in zip(key, lock)]
        if not any(num > threshold for num in combination):
            possible_combinations += 1
            # print(f'combination works {combination}')

print(f'Possible combinations are {possible_combinations}')