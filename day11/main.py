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
def has_even_digits(number):
    # Convert number to string and check the length
    return len(str(abs(number))) % 2 == 0

@cache
def split_number(number):
    num_str = str(number)

    # Find the middle index
    middle = len(num_str) // 2

    # Split the string into two parts
    first_half = num_str[:middle]
    second_half = num_str[middle:]

    return int(first_half), int(second_half)

@cache
def changeStone(input):
    if input == 0:
        return [1]
    elif has_even_digits(input):
        [output1, output2] = split_number(input)
        return [output1, output2]
    else:
        return [input*2024]

input = import_text_input('input.txt')
input_list = list(map(int, input.split()))

blink_num = 75
for blink in range(blink_num):
    new_list = []
    for _, element in enumerate(input_list):
        result = changeStone(element)

        new_list.append(result[0])
        if len(result) > 1:
            new_list.append(result[1])
    input_list = deepcopy(new_list)
    print(f'Blink {blink + 1}: number of stones is {len(input_list)}')