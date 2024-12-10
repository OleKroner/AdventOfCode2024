with open("./input.txt") as file:
    map = [
        [
            int(tile) for tile in line
        ]
        for line in file.read().splitlines()
    ]
    max_y = len(map)
    max_x = len(map[0])

    trailheads = [
        (y, x)
        for y, line in enumerate(map)
        for x, tile in enumerate(line)
        if tile == 0
    ]

class Tile:
    def __init__(self, pos: tuple[int, int]):
        self.paths: list[Tile] = []
        self.pos = pos
    
    def __str__(self):
        return f"{self.pos} - {[x.pos for x in self.paths]}"
    
    def build_trails(self):
        self.paths = [Tile(pos) for pos in get_surrounding_tiles(self.pos)]

        for child_tile in self.paths:
            child_tile.build_trails()
        
        return self.paths
    
    def get_hiketrail_count(self):      
        if map[self.pos[0]][self.pos[1]] == 9:
            return int(1)
        
        trail_count = 0
        for path in self.paths:
            trail_count += path.get_hiketrail_count()
        
        return int(trail_count)

def is_adjacent_tile(pos: tuple[int, int], height: int):
    return 0 <= pos[0] < max_y and 0 <= pos[1] < max_x and map[pos[0]][pos[1]] - 1 == height

def get_surrounding_tiles(pos: tuple[int, int]):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    return [
        (pos[0] + dx, pos[1] + dy)
        for dx, dy in directions
        if is_adjacent_tile((pos[0] + dx, pos[1] + dy), map[pos[0]][pos[1]])
    ]

def get_trailhead_score(trailhead: tuple[int, int]):
    tiles_to_search = get_surrounding_tiles(trailhead)
    tiles_on_trails = set()
    
    while len(tiles_to_search) != 0:
        y, x = tiles_to_search[0]
        tiles_on_trails.add((map[y][x], (y, x)))
        tiles_to_search.extend(get_surrounding_tiles((y, x)))
        del tiles_to_search[0]
    
    return len([height for height, position in tiles_on_trails if height == 9])

def get_trailhead_rating(trailhead: tuple[int, int]):
    start = Tile(trailhead)
    start.build_trails()

    return start.get_hiketrail_count()

sum_trailhead_score = 0
sum_trailhead_rating = 0

for trailhead in trailheads:
    sum_trailhead_score += get_trailhead_score(trailhead)
    sum_trailhead_rating += get_trailhead_rating(trailhead)

print("Sum of trailehead scores:", sum_trailhead_score)
print("Sum of trailehead ratings:", sum_trailhead_rating)