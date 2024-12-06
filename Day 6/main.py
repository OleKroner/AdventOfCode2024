import numpy as np
from multiprocessing import Pool, cpu_count, Manager

original_map = []
start_position = (0, 0)
current_position = (0, 0)
current_direction = 0
max_x = 0
max_y = 0

direction_dict = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open("./input.txt") as file:
    lines = file.read().split()
    for y, line in enumerate(lines):
        position = line.find("^")
        if position != -1:
            current_position = start_position = (y, position)
            max_x = len(line) - 1
        original_map.append(list(line))

    max_y = len(original_map) - 1

map = np.array(original_map)
traversal_history = []

def next_direction(direction):
    return (direction + 1) % 4

def get_next_position(position, direction):
    return (
        position[0] + direction_dict[direction][0],
        position[1] + direction_dict[direction][1],
    )

def is_within_bounds(position):
    return 0 <= position[0] <= max_y and 0 <= position[1] <= max_x

def is_path_blocked(position, direction):
    next_position = get_next_position(position, direction)
    if not is_within_bounds(next_position):
        return False
    return map[next_position] == "#"

# Initial traversal
while is_within_bounds(current_position):
    if is_path_blocked(current_position, current_direction):
        current_direction = next_direction(current_direction)
    else:
        map[current_position[0], current_position[1]] = "X"
        traversal_history.append((current_position, current_direction))
        current_position = get_next_position(current_position, current_direction)

x_positions = np.sum(map == "X")

def check_obstruction(args):
    position, start_position = args
    if position == start_position:
        return None

    visited_positions = set()
    virtual_obstruction = {position}
    current_position = start_position
    current_direction = 0

    while is_within_bounds(current_position):
        next_pos = get_next_position(current_position, current_direction)
        
        if next_pos in virtual_obstruction or is_path_blocked(current_position, current_direction):
            current_direction = next_direction(current_direction)
        else:
            current_position = next_pos

        if (current_position, current_direction) in visited_positions:
            return position  # Obstruction detected
        visited_positions.add((current_position, current_direction))

    return None  # No obstruction detected

if __name__ == "__main__":
    num_cores = cpu_count()
    print(f"Using {num_cores} cores for multiprocessing.")

    manager = Manager()
    checked_positions = manager.list()

    unique_positions = []
    for position, _ in traversal_history:
        if position not in checked_positions and position != start_position:
            checked_positions.append(position)
            unique_positions.append(position)

    args = [(position, start_position) for position in unique_positions]

    with Pool(num_cores) as pool:
        results = pool.map(check_obstruction, args)

    possible_obstructions = len({result for result in results if result is not None})

    print("Number of distinct positions traversed by guard:", x_positions)
    print("Total possible obstruction positions discovered:", possible_obstructions)
