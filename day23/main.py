from itertools import combinations

def read_connections(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]




# Open
file_path = 'input.txt'
connections = read_connections(file_path)

graph = {}
for connection in connections:
    a, b = connection.split('-')
    if a not in graph:
        graph[a] = set()
    if b not in graph:
        graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)

def is_connected_triplet(triplet):
    return all(b in graph[a] for a, b in combinations(triplet, 2))

triplets = combinations(graph.keys(), 3)

valid_triplets = 0
for triplet in triplets:
    if is_connected_triplet(triplet) and any(comp.startswith('t') for comp in triplet):
        valid_triplets += 1

print(valid_triplets)
