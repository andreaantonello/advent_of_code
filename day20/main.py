from collections import deque, Counter

def read_grid_from_file(filename):
    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid

def find_start_end(grid):
    start, end = None, None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    return start, end

def bfs(grid, start, end, allow_cheating=False, wall_position=None):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, time = queue.popleft()

        if (x, y) == end:
            return time

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                if allow_cheating and (nx, ny) == wall_position:
                    visited[nx][ny] = True
                    queue.append((nx, ny, time + 1))
                elif grid[nx][ny] != '#':
                    visited[nx][ny] = True
                    queue.append((nx, ny, time + 1))

    return float('inf')

def find_cheats(grid, start, end):
    normal_path = bfs(grid, start, end, allow_cheating=False)

    if normal_path == float('inf'):
        print("No valid path found from start to end without cheating!")
        return []

    cheats = []

    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                cheat_time = bfs(grid, start, end, allow_cheating=True, wall_position=(i, j))
                if cheat_time < normal_path:
                    saves_time = normal_path - cheat_time
                    cheats.append(saves_time)

    cheat_counts = Counter(cheats)

    results = []
    values = []
    for time_saved in sorted(cheat_counts.keys()):
        count = cheat_counts[time_saved]
        results.append(f"There are {count} cheats that save {time_saved} picoseconds.")
        values.append([count, time_saved])

    return results, values

filename = 'input.txt'
grid = read_grid_from_file(filename)
start, end = find_start_end(grid)
results, values = find_cheats(grid, start, end)

print(values)

total_cheats = 0
for value in values:
    if value[1] >= 100:
        total_cheats += value[0]

for result in results:
    print(result)

print(f'Total cheats are {total_cheats}')