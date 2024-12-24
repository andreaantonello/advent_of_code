import re
import sys
import time
import os
from itertools import product
from copy import deepcopy
from functools import cache

# Timing the code execution
start_time = time.time()

def import_text_input(filename):
    with open(filename, "r") as file:
        input_string = file.read()
    return input_string


@cache
def countStones(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return countStones(1, steps - 1)
    stringStone = str(stone)
    lenStringStone = len(stringStone)
    if lenStringStone % 2 == 0:
        stoneSplit = countStones(int(stringStone[: lenStringStone//2]), steps - 1) + countStones(int(stringStone[lenStringStone//2:]), steps - 1)
        return stoneSplit
    return countStones(stone*2024, steps - 1)


input = import_text_input('input.txt')
input_list = list(map(int, input.split()))

stepsMax = 75
print(sum(countStones(stone, stepsMax) for stone in input_list))