import re
import sys

def parse_file(file_path):
    button_a = []
    button_b = []
    prizes = []

    # Regular expressions to match Button A, Button B, and Prize lines
    button_a_pattern = r"Button A: X\+(\d+), Y\+(\d+)"
    button_b_pattern = r"Button B: X\+(\d+), Y\+(\d+)"
    prize_pattern = r"Prize: X=(\d+), Y=(\d+)"

    with open(file_path, 'r') as file:
        content = file.read()

        # Find all matches for each pattern
        button_a_matches = re.findall(button_a_pattern, content)
        button_b_matches = re.findall(button_b_pattern, content)
        prize_matches = re.findall(prize_pattern, content)

        # Convert matches to integers and append to respective lists
        for match in button_a_matches:
            button_a.append(list(map(int, match)))
        for match in button_b_matches:
            button_b.append(list(map(int, match)))
        for match in prize_matches:
            prizes.append(list(map(int, match)))

    return button_a, button_b, prizes

# Path to the input file
file_path = 'input.txt'

# Parse the file
all_button_a, all_button_b, all_prizes = parse_file(file_path)

max_button_presses = 100
A_cost = 3
B_cost = 1
all_scores = []
for index, entry in enumerate(all_button_a):
    button_a = all_button_a[index]
    button_b = all_button_b[index]
    prize = all_prizes[index]
    scores = []
    for press_A in range(max_button_presses):
        for press_B in range(max_button_presses):
            resultX = press_A*button_a[0] + press_B*button_b[0]
            resultY = press_A*button_a[1] + press_B*button_b[1]
            if resultX == prize[0] and resultY == prize[1]:
                current_score = press_A*A_cost + press_B*B_cost
                scores.append(current_score)

    all_scores.append(scores)

cumulative_score = 0
for score in all_scores:
    if score:
        cumulative_score += min(score)
print(cumulative_score)

