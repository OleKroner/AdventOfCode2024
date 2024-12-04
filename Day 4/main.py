import re

lines = []
x_positions = []
a_positions = []

potential_words = []

max_x = 0
max_y = 0

def find_right(position: tuple[int], steps: int):
    return (position[0], position[1] + steps)

def find_left(position: tuple[int], steps: int):
    return (position[0], position[1] - steps)

def find_up(position: tuple[int], steps: int):
    return (position[0] - steps, position[1])

def find_down(position: tuple[int], steps: int):
    return (position[0] + steps, position[1])

def find_up_right(position: tuple[int], steps: int):
    return (position[0] - steps, position[1] + steps)

def find_up_left(position: tuple[int], steps: int):
    return (position[0] - steps, position[1] - steps)

def find_down_left(position: tuple[int], steps: int):
    return (position[0] + steps, position[1] - steps)

def find_down_right(position: tuple[int], steps: int):
    return (position[0] + steps, position[1] + steps)

directions = {
    "right": find_right,
    "left": find_left,
    "up": find_up,
    "down": find_down,
    "up_right": find_up_right,
    "up_left": find_up_left,
    "down_left": find_down_left,
    "down_right": find_down_right
}

def search_for_word(position: tuple[int], operation: str):
    word = ""
    for i in range(4):
        search_position = directions[operation](position, i)
        if not 0 <= search_position[0] < max_y or not 0 <= search_position[1] < max_x:
            return None
        word += lines[search_position[0]][search_position[1]]

    return word

def search_all_directions(position: tuple[int]):
    words = []
    for direction in directions:
        word = search_for_word(position, direction)
        if word == "XMAS": words.append(word)
    
    return words

def pos_to_letter(pos: tuple[int]):
    return lines[pos[0]][pos[1]]

def is_x_mas(position: tuple[int]):
    if position[0] == 0 or position[0] + 1 == max_y or position[1] == 0 or position[1] + 1 == max_y: return False
    if pos_to_letter(find_down_right(position, 1)) == pos_to_letter(find_up_left(position, 1)) or pos_to_letter(find_down_left(position, 1)) == pos_to_letter(find_up_right(position, 1)): return False
    if pos_to_letter(find_down_left(position, 1)) in ["M", "S"] and pos_to_letter(find_down_right(position, 1)) in ["M", "S"] and pos_to_letter(find_up_left(position, 1)) in ["M", "S"] and pos_to_letter(find_up_right(position, 1)) in ["M", "S"]: return True
    return False

with open("./input.txt", "r") as file:
    for line in file:
        lines.append(line.removesuffix("\n"))
        
for i in range(len(lines)):
    x_indexes = re.finditer("X", lines[i])
    a_indexes = re.finditer("A", lines[i])
    
    for x in x_indexes:
        x_positions.append((i, int(x.start())))
    for a in a_indexes:
        a_positions.append((i, int(a.start())))

max_x = len(lines[0])
max_y = len(lines)

xmas_count = 0
x_mas_count = 0

for position in x_positions:
    xmas_count += len(search_all_directions(position))

for position in a_positions:
    if is_x_mas(position): x_mas_count += 1

print(xmas_count)
print(x_mas_count)