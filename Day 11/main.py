with open("./input.txt") as file:
    stones = [int(stone) for stone in file.read().split()]

def split_stone(stone: int):
    str_stone = str(stone)
    num1 = int(str_stone[: len(str_stone) // 2])
    num2 = int(str_stone[len(str_stone) // 2 :])
    return num1, num2

cache = {}

def blink_n_times(stone, n):
    # Use pre-calculated result
    if (stone, n) in cache:
        return cache[(stone, n)]
    
    if n == 0: return 1

    # Calculate new result
    if stone == 0:
        count = blink_n_times(1, n-1)
        cache[(stone, n)] = count
        return count
    
    if len(str(stone)) % 2 == 0:
        num1, num2 = split_stone(stone)
        count1 = blink_n_times(num1, n-1)
        count2 = blink_n_times(num2, n-1)
        cache[(num1, n-1)] = count1
        cache[(num2, n-1)] = count2
        return count1 + count2
    
    count = blink_n_times(stone * 2024, n-1)
    cache[(stone * 2024, n-1)] = count
    return count

print(sum(blink_n_times(stone, 25) for stone in stones))
print(sum(blink_n_times(stone, 75) for stone in stones))