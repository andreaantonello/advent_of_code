import heapq

# Directions: East, North, West, South (clockwise)
DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # (dx, dy) for [East, North, West, South]


def in_bounds(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#'


def find_start_end(maze):
    start = end = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    return start, end


def dijkstra(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    # Priority queue to store the states (cost, x, y, direction)
    pq = []
    # Distances table initialized to infinity
    dist = {}

    # Initialize starting point
    heapq.heappush(pq, (0, start[0], start[1], 0))  # (cost, x, y, direction)
    dist[(start[0], start[1], 0)] = 0  # Start at (x, y) facing East (0)

    while pq:
        cost, x, y, direction = heapq.heappop(pq)

        # If we reached the end, return the cost
        if (x, y) == end:
            return cost

        # Try moving forward
        dx, dy = DIRECTIONS[direction]
        nx, ny = x + dx, y + dy
        if in_bounds(nx, ny, maze):
            new_cost = cost + 1
            if (nx, ny, direction) not in dist or new_cost < dist[(nx, ny, direction)]:
                dist[(nx, ny, direction)] = new_cost
                heapq.heappush(pq, (new_cost, nx, ny, direction))

        # Try rotating clockwise
        new_direction = (direction + 1) % 4
        new_cost = cost + 1000
        if (x, y, new_direction) not in dist or new_cost < dist[(x, y, new_direction)]:
            dist[(x, y, new_direction)] = new_cost
            heapq.heappush(pq, (new_cost, x, y, new_direction))

        # Try rotating counterclockwise
        new_direction = (direction - 1) % 4
        new_cost = cost + 1000
        if (x, y, new_direction) not in dist or new_cost < dist[(x, y, new_direction)]:
            dist[(x, y, new_direction)] = new_cost
            heapq.heappush(pq, (new_cost, x, y, new_direction))

    return -1  # If no path found


# Read the maze from the txt file
def read_maze_from_file(file_path):
    with open(file_path, 'r') as file:
        maze = [list(line.strip()) for line in file]
    return maze

# Path to the maze file
maze_file = 'input.txt'

# Read the maze
maze = read_maze_from_file(maze_file)
# Find start and end positions
start, end = find_start_end(maze)

# Run Dijkstra's algorithm to find the minimum score
result = dijkstra(maze, start, end)
print("Minimum score:", result)
