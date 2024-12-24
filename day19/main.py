def can_form_design(towel_patterns, design):
    dp = [False] * (len(design) + 1)
    dp[0] = True

    for i in range(1, len(design) + 1):
        for towel in towel_patterns:
            if i >= len(towel) and design[i - len(towel):i] == towel:
                dp[i] = dp[i] or dp[i - len(towel)]

    return dp[len(design)]


def count_possible_designs(towel_patterns, designs):
    possible_designs = 0
    for design in designs:
        if can_form_design(towel_patterns, design):
            possible_designs += 1
    return possible_designs


# Example input:
def can_form_design(towel_patterns, design):
    dp = [False] * (len(design) + 1)
    dp[0] = True



    for i in range(1, len(design) + 1):
        # Try every towel
        for towel in towel_patterns:
            if i >= len(towel) and design[i - len(towel):i] == towel:
                dp[i] = dp[i] or dp[i - len(towel)]

    return dp[len(design)]


def count_possible_designs(towel_patterns, designs):
    possible_designs = 0
    for design in designs:
        if can_form_design(towel_patterns, design):
            possible_designs += 1
    return possible_designs


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        towel_patterns = file.readline().strip().split(', ')
        file.readline()
        designs = [line.strip() for line in file.readlines()]
    return towel_patterns, designs


# Input file path
file_path = 'input.txt'

towel_patterns, designs = read_input_file(file_path)
result = count_possible_designs(towel_patterns, designs)
print(f'Quiz 1 result {result}')


def count_ways_to_form_design(towel_patterns, design):
    dp = [0] * (len(design) + 1)
    dp[0] = 1

    for i in range(1, len(design) + 1):

        for towel in towel_patterns:
            if i >= len(towel) and design[i - len(towel):i] == towel:
                dp[i] += dp[i - len(towel)]

    return dp[len(design)]


def total_ways_to_form_designs(towel_patterns, designs):
    total_ways = 0
    for design in designs:
        total_ways += count_ways_to_form_design(towel_patterns, design)
    return total_ways


towel_patterns, designs = read_input_file(file_path)

result = total_ways_to_form_designs(towel_patterns, designs)
print(f'Quiz 2 result {result}')





