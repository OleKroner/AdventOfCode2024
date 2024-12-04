import re

input = ""

muls = []
total_sum = 0

def mul_multiply(string: str):
    string = string.removeprefix("mul(").removesuffix(")")
    nums = list(map(int, string.split(",")))

    return nums[0] * nums[1]

with open("./input.txt", "r") as file:
    for line in file:
        x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line)
        muls += x
        input += line

for mul in muls:
    total_sum += mul_multiply(mul)

print(total_sum)
total_sum = 0

parsed_input = re.sub("don't\(\).*?do\(\)", "", re.sub("\n", "", input))
muls = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", re.sub("don't\(\).*", "", parsed_input))

for mul in muls:
    total_sum += mul_multiply(mul)

print(total_sum)