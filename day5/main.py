import re
from collections import defaultdict, deque
import sys
import time

with open("input.txt", "r") as file:
    input_string = file.read()

def process_file(file_path):
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")
    pairs = [line.strip() for line in lines if "|" in line]
    grouped = [line.strip() for line in lines if "|" not in line and line.strip()]

    separated_pairs = [
        [int(x) for x in pair.split("|")]
        for pair in pairs]

    grouped_lists = [
        [int(x) for x in group.split(",")]
        for group in grouped]
    return separated_pairs, grouped_lists


def find_mid_value(list):
    n = len(list)
    if n == 0:
        raise ValueError("The list is empty. Cannot find the middle element.")
    mid = n // 2
    if n % 2 == 0:
        # Even length: Return two middle elements
        raise ValueError("The list has even length")
    return list[mid]

def page_ordering(rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for rule in rules:
        before, after = map(int, rule.split('|'))
        graph[before].append(after)
        in_degree[after] += 1
        if before not in in_degree:
            in_degree[before] = 0

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    ordering = []

    while queue:
        current = queue.popleft()
        ordering.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(ordering) == len(in_degree):
        return ordering
    else:
        raise ValueError("The rules contain a cycle and cannot be resolved.")


# Part 1
file_path = "input.txt"
separated_pairs, grouped_lists = process_file(file_path)

correct_list = []
mid_value = []
for index, list in enumerate(grouped_lists):
    validity = True
    for rule in separated_pairs:
        if rule[0] in list and rule[1] in list:
            if list.index(rule[0]) > list.index(rule[1]):
                validity = False
                break
    if validity:
        correct_list.append(list)
        mid_value.append(find_mid_value(list))

result = sum(mid_value)
print(f'Quiz 1 result is {result}')

# Part 2
wrong_list = []
mid_value = []
for index, list in enumerate(grouped_lists):
    validity = True
    for rule in separated_pairs:
        if rule[0] in list and rule[1] in list:
            if list.index(rule[0]) > list.index(rule[1]):
                validity = False
                break
    if not validity:
        wrong_list.append(list)

continue_looping = True
loop = 0
while continue_looping:
    wrong_items = 0
    print(f'Starting loop {loop + 1}')
    for index, list in enumerate(wrong_list):
        for rule in separated_pairs:
            if rule[0] in list and rule[1] in list:
                if list.index(rule[0]) > list.index(rule[1]):
                    wrong_items += 1
                    rule_0_index = list.index(rule[0])
                    rule_1_index = list.index(rule[1])
                    list[rule_0_index], list[rule_1_index] = list[rule_1_index], list[
                        rule_0_index]
    if wrong_items == 0:
        continue_looping = False
    print(f'Incorrectly places items are {wrong_items}')
    loop += 1

mid_value = []
for index, list in enumerate(wrong_list):
    mid_value.append(find_mid_value(list))

result = sum(mid_value)
print(f'Quiz 2 result is {result}')