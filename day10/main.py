import time
import sys
from copy import deepcopy
from collections import deque

def read_input_from_file(filename):
    with open(filename, 'r') as file:
        # Read lines from the file and strip newlines, then convert to integers
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

        # If we've reached a 9, count it
        if current_height == 9:
            reachable_9s += 1

        # Explore all 4 directions
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
    """Count the number of distinct paths from (x, y) to height 9 using DFS."""
    # If we've reached height 9, this is one distinct path
    if current_height == 9:
        return 1

    # Check memoization to avoid redundant computation
    if (x, y, current_height) in memo:
        return memo[(x, y, current_height)]

    # Explore all four possible directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    path_count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid_move(nx, ny, height_map, current_height):
            path_count += dfs_count_paths(height_map, nx, ny, current_height + 1, memo)

    # Store the result in the memoization dictionary
    memo[(x, y, current_height)] = path_count
    return path_count

def find_trailhead_ratings(height_map):
    """Find all trailheads (height 0 positions) and calculate their ratings."""
    trailhead_ratings = []
    memo = {}

    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            if height_map[i][j] == 0:
                # Calculate the rating for this trailhead
                rating = dfs_count_paths(height_map, i, j, 0, memo)
                trailhead_ratings.append(rating)

    return trailhead_ratings




# Read the word search matrix from the file
matrix = read_input_from_file("input.txt")
# Find the trailheads and print the scores
scores = find_trailheads_and_scores(matrix)
print("Trailhead scores:", scores)
print("Trailhead Scores:", sum(scores))


# Sum the ratings of all trailheads ????
ratings = find_trailhead_ratings(matrix)
total_rating = sum(ratings)
print("Trailhead Ratings:", ratings)
print("Sum of Trailhead Ratings:", total_rating)