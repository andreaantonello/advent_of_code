import time
import sys
from copy import deepcopy
from collections import deque

def read_input_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [[int(char) if char.isdigit() else 0 for char in line.strip()] for line in file.readlines()]
    return matrix

def is_valid_move(x, y, height_map, current_height):
    if 0 <= x < len(height_map) and 0 <= y < len(height_map[0]):
        return height_map[x][y] == current_height + 1
    return False

def bfs(height_map, start_x, start_y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])
    reachable_9s = 0

    while queue:
        x, y = queue.popleft()
        current_height = height_map[x][y]
        if current_height == 9:
            reachable_9s += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and is_valid_move(nx, ny, height_map, current_height):
                visited.add((nx, ny))
                queue.append((nx, ny))
    return reachable_9s

def find_trailheads_and_scores(height_map):
    trailheads = []
    scores = []
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            if height_map[i][j] == 0:
                trailheads.append((i, j))

    # Perform BFS
    for trailhead in trailheads:
        score = bfs(height_map, trailhead[0], trailhead[1])
        scores.append(score)
    return scores



def dfs_count_paths(height_map, x, y, current_height, memo):
    if current_height == 9:
        return 1

    if (x, y, current_height) in memo:
        return memo[(x, y, current_height)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    path_count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid_move(nx, ny, height_map, current_height):
            path_count += dfs_count_paths(height_map, nx, ny, current_height + 1, memo)

    memo[(x, y, current_height)] = path_count
    return path_count

def find_trailhead_ratings(height_map):
    trailhead_ratings = []
    memo = {}
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            if height_map[i][j] == 0:
                rating = dfs_count_paths(height_map, i, j, 0, memo)
                trailhead_ratings.append(rating)
    return trailhead_ratings


matrix = read_input_from_file("input.txt")

scores = find_trailheads_and_scores(matrix)
print("Trailhead scores:", scores)
print("Trailhead Scores:", sum(scores))

# Sum the ratings of all trailheads ????
ratings = find_trailhead_ratings(matrix)
total_rating = sum(ratings)
print("Trailhead Ratings:", ratings)
print("Sum of Trailhead Ratings:", total_rating)