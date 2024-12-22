import re
from collections import defaultdict, deque
import sys
import time

# Example input string (replace this with your file content)
with open("input.txt", "r") as file:
    input_string = file.read()


def process_file(file_path):
    """
    Processes a text file to extract pairs and grouped lists.

    :param file_path: Path to the input file.
    :param target_pairs: Set of target pairs in "A|B" format.
    :return: Tuple of separated pairs and grouped lists.
    """
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")

    # Separate lines based on presence of '|'
    pairs = [line.strip() for line in lines if "|" in line]
    grouped = [line.strip() for line in lines if "|" not in line and line.strip()]

    # Process pairs
    separated_pairs = [
        [int(x) for x in pair.split("|")]
        for pair in pairs
    ]

    # Process grouped lists
    grouped_lists = [
        [int(x) for x in group.split(",")]
        for group in grouped
    ]

    return separated_pairs, grouped_lists




def page_ordering(rules):
    # Step 1: Parse rules into a graph
    graph = defaultdict(list)  # Adjacency list
    in_degree = defaultdict(int)  # Count of incoming edges for each node

    # Build the graph and count in-degrees
    for rule in rules:
        before, after = map(int, rule.split('|'))
        graph[before].append(after)
        in_degree[after] += 1
        if before not in in_degree:
            in_degree[before] = 0

    # Step 2: Perform topological sort
    # Find all nodes with no incoming edges
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    ordering = []

    while queue:
        current = queue.popleft()
        ordering.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we sorted all nodes, return the ordering
    if len(ordering) == len(in_degree):
        return ordering
    else:
        raise ValueError("The rules contain a cycle and cannot be resolved.")




file_path = "input.txt"
separated_pairs, grouped_lists = process_file(file_path)

correct_list = []
for index, list in enumerate(grouped_lists):
    # print(f'Analysing list {index}')
    validity = True
    for rule in separated_pairs:
        if rule[0] in list and rule[1] in list:
            if list.index(rule[0]) > list.index(rule[1]):
                validity = False
                break
    if validity:
        correct_list.append(list)

mid_value = []
for list in correct_list:
    n = len(list)
    if n == 0:
        raise ValueError("The list is empty. Cannot find the middle element.")

    mid = n // 2
    if n % 2 == 0:
        # Even length: Return two middle elements
        raise ValueError("The list has even length")
    else:
        mid_value.append(list[mid])

result = sum(mid_value)
print(f'Quiz result is {result}')


# Part 2

correct_list = []
index_list = []
grouped_list_fixed = []
for list_index, grouped_list in enumerate(grouped_lists):
    print(f'Analysing list {list_index}')
    restart = False
    separated_index = 0  # Index for iterating through separated_pairs

    while separated_index < len(separated_pairs):
        if restart:
            separated_index = 0
            restart = False

        rule = separated_pairs[separated_index]
        if rule[0] in grouped_list and rule[1] in grouped_list:
            if grouped_list.index(rule[0]) > grouped_list.index(rule[1]):
                # Swap the items to ensure rule[0] comes before rule[1]
                rule_0_index = grouped_list.index(rule[0])
                rule_1_index = grouped_list.index(rule[1])
                grouped_list[rule_0_index], grouped_list[rule_1_index] = grouped_list[rule_1_index], grouped_list[
                    rule_0_index]
                restart = True
                if separated_index not in index_list:
                    index_list.append(separated_index)

        if not restart:  # Only increment if no restart
            separated_index += 1

    # Add the corrected list to grouped_list_fixed
    grouped_list_fixed.append(grouped_list)


print(f'len of list is {len(grouped_lists)}')
print(f'len of list is {len(grouped_list_fixed)}')


for index, grouped_list in enumerate(grouped_list_fixed):
    print(f'Analysing list {index}')
    validity = True
    for rule in separated_pairs:
        if rule[0] in grouped_list and rule[1] in grouped_list:
            if grouped_list.index(rule[0]) > grouped_list.index(rule[1]):
                print('We have an error!')

mid_value = []
for list in grouped_list_fixed:
    n = len(list)
    if n == 0:
        raise ValueError("The list is empty. Cannot find the middle element.")

    mid = n // 2
    if n % 2 == 0:
        # Even length: Return two middle elements
        raise ValueError("The list has even length")
    else:
        mid_value.append(list[mid])

result = sum(mid_value)
print(f'Quiz result is {result}')

