import re

def clean_string(input_string):
    pattern = r'(mul\([0-9, ]+\)|do\(\)|don\'t\(\))'

    cleaned_string = '\n'.join(re.findall(pattern, input_string))
    return cleaned_string

def remove_lines_after_dont(input_string):
    lines = input_string.splitlines()
    dont_index = None
    for i, line in enumerate(lines):
        if "don't()" in line:
            dont_index = i
            break

    # If a line with "don't()" is found, remove all lines after it
    if dont_index is not None:
        lines = lines[:dont_index + 1]

    # Join the remaining lines back together into a string
    cleaned_string = '\n'.join(lines)

    return cleaned_string

def retain_specific_characters(input_string):
    cleaned_string = "\n".join(re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', input_string))

    return cleaned_string

def process_and_track(input_string):

    lines = input_string.splitlines()
    result = []
    add_mul = True  # Flag to track whether to add mul after a do()

    for line in lines:
        # print(word)
        if line == "do()":
            add_mul = True  # Set flag to add "mul()" after this "do()"
        elif line == "don't()":
            add_mul = False  # Reset the flag as "don't()" stops adding "mul()"
        elif line.startswith("mul("):
            if add_mul:  # If flag is set, add mul after "do()"
                result.append(line)  # Add mul(x, y) to the result
    return '\n'.join(result)  # Join the result into a single string


# Example input string (replace this with your file content)
with open("input.txt", "r") as file:
    input_string = file.read()
pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
matches = re.findall(pattern, input_string)

total_sum = 0
for x, y in matches:
    total_sum = total_sum + int(x)*int(y)

print("Total sum is", total_sum)

cleaned_string = retain_specific_characters(input_string)
cleaned_string = process_and_track(cleaned_string)

matches = re.findall(pattern, cleaned_string)

total_sum = 0
for x, y in matches:
    total_sum = total_sum + int(x)*int(y)
    # print(f"x: {x}, y: {y}")

print("Total cleaned sum is", total_sum)