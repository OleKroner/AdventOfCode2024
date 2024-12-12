with open("./test_input.txt") as file:
    stones = [int(stone) for stone in file.read().split()]
    
def blink(old_stones):
    new_stones = []
    
    split_count = 0
    for stone in old_stones:
        if stone == 0:
            new_stones.append(1)
            continue
        if len(str(stone)) % 2 == 0:
            split_count += 1
            new_stones.append(int(str(stone)[0 : len(str(stone)) // 2]))
            new_stones.append(int(str(stone)[len(str(stone)) // 2 :]))
            continue
        new_stones.append(int(stone * 2024))

    return new_stones, split_count

blink_count = 75

def test(iteration: int):
    return int((0.714 * (1.526**iteration)) + 303.15)

split_list = []

for i in range(blink_count):
    print(f"Progress: {i} of {blink_count}")
    stones, splits = blink(stones)
    split_list.append(splits)
    print(len(stones), splits, test(i + 1) * 2)

print(len(stones))