import re
import sys
import time
import os
from itertools import product

# Timing the code execution
start_time = time.time()

def import_text_input(filename):
    with open(filename, "r") as file:
        input_string = file.read()
    result = {}
    for line in input_string.strip().split("\n"):
        key, values = line.split(":")  # Split by colon
        key = int(key.strip())  # Convert the key to an integer
        values = list(map(int, values.strip().split()))  # Convert the values to a list of integers
        result[key] = values  # Add to the dictionary
    return result

def multiplyAll(numbers):
    # Multiply all members
    result = 1
    for num in numbers:
        result *= num
    return result

def sumAll(numbers):
    # Multiply all members
    result = 0
    for num in numbers:
        result += num
    return result

def evaluate_left_to_right(values, operators):
    result = values[0]
    i = 0  # Index to track values and operators
    while i < len(operators):
        op = operators[i]
        if op == '+':
            result += values[i + 1]
        elif op == '*':
            result *= values[i + 1]
        elif op == '&':
            # Concatenate the current number with the next
            concatenated = int(str(result) + str(values[i + 1]))
            result = concatenated
        i += 1
    return result

# Function to combine numbers and operators into an expression
def create_expression(numbers, operators, delimiter=""):
    expression = str(numbers[0])
    for num, op in zip(numbers[1:], operators):
        expression += delimiter + op + delimiter + str(num)
    return expression


filename = "input.txt"
result = import_text_input(filename)
count = 0
total_sum = 0
# Iterate through the input txt
for i, (key, values) in enumerate(result.items()):
    print(f'Evaluating line {i + 1} of {len(result.items())}')  # Index is i+1 for better readability
    edgeCase = False

    if not edgeCase:
        # Generate all combinations of '+' and '-' for (list_length - 1) positions
        operator_combinations = list(product("+*&", repeat=len(values) - 1))
        # Evaluate and print each expression
        for operators in operator_combinations:
            expression = create_expression(values, operators)
            evalResult = evaluate_left_to_right(values, operators)  # Use eval to compute the result of the expression
            if evalResult == key:
                total_sum = total_sum + evalResult
                count = count + 1
                break

end_time = time.time()

# Print timing and count results
print(f"Execution time: {end_time - start_time:.4f} seconds")
print(f"Count of matches found: {count}")
print(f"Total matches sum: {total_sum}")