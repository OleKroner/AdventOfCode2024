from collections import defaultdict

with open("./input.txt") as file:
    map = [line for line in file.read().splitlines()]

max_y = len(map)
max_x = len(map[0])

antenna_positions = defaultdict(list)

def is_within_bounds(pos: tuple[int, int]):
    return 0 <= pos[0] < max_y and 0 <= pos[1] < max_x

def find_all_anti_nodes(pos1, diff):
    dy, dx = diff
    nodes = set()

    # Search forwards
    search_pos = pos1
    while is_within_bounds(search_pos):
        nodes.add(search_pos)
        search_pos = (search_pos[0] + dy, search_pos[1] + dx)

    # Search backward
    search_pos = pos1
    while is_within_bounds(search_pos):
        nodes.add(search_pos)
        search_pos = (search_pos[0] - dy, search_pos[1] - dx)

    return nodes

for y, row in enumerate(map):
    for x, node in enumerate(row):
        if node != ".":
            antenna_positions[node].append((x, y))

anti_nodes = set()
all_anti_nodes = set()

for frequency, positions in antenna_positions.items():
    for pos1 in positions:
        for pos2 in positions:
            if pos1 == pos2: continue

            dy, dx = pos1[0] - pos2[0], pos1[1] - pos2[1]
            anti_node = (pos1[0] + dy, pos1[1] + dx)

            if is_within_bounds(anti_node):
                anti_nodes.add(anti_node)

            all_anti_nodes.update(find_all_anti_nodes(pos1, (dy, dx)))

print(f"Number of anti-nodes: {len(anti_nodes)}")
print(f"Number of all anti-nodes: {len(all_anti_nodes)}")