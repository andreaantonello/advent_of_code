import re
import sys
import time
import os
from itertools import product

start_time = time.time()

def import_text_input(filename):
    with open(filename, "r") as file:
        input_string = file.read()
    result = {}
    for line in input_string.strip().split("\n"):
        key, values = line.split(":")  # Split by colon
        key = int(key.strip())
        values = list(map(int, values.strip().split()))
        result[key] = values
    return result

def multiplyAll(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def sumAll(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

def evaluate_left_to_right(values, operators):
    result = values[0]
    i = 0
    while i < len(operators):
        op = operators[i]
        if op == '+':
            result += values[i + 1]
        elif op == '*':
            result *= values[i + 1]
        elif op == '&':
            concatenated = int(str(result) + str(values[i + 1]))
            result = concatenated
        i += 1
    return result

def create_expression(numbers, operators, delimiter=""):
    expression = str(numbers[0])
    for num, op in zip(numbers[1:], operators):
        expression += delimiter + op + delimiter + str(num)
    return expression


filename = "input.txt"
result = import_text_input(filename)
count = 0
total_sum = 0

for i, (key, values) in enumerate(result.items()):
    print(f'Evaluating line {i + 1} of {len(result.items())}')
    edgeCase = False

    if not edgeCase:
        operator_combinations = list(product("+*&", repeat=len(values) - 1))
        for operators in operator_combinations:
            expression = create_expression(values, operators)
            evalResult = evaluate_left_to_right(values, operators)
            if evalResult == key:
                total_sum = total_sum + evalResult
                count = count + 1
                break

end_time = time.time()

print(f"Execution time: {end_time - start_time:.4f} seconds")
print(f"Count of matches found: {count}")
print(f"Total matches sum: {total_sum}")