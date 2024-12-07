with open("./input.txt") as file:
    lines = file.read().split("\n")
    equations = [item.split(":") for item in lines]
    equations = [(int(line[0]), [int(x) for x in line[1].split()]) for line in equations]

def add(a: int, b: int):
    return a + b

def multiply(a: int, b: int):
    return a * b

def concat(a: int, b: int):
    return int(str(a) + str(b))

operation_map = {
    0: add,
    1: multiply,
    2: concat
}

def calculate(values: list[int], operation: str):
    result = values[0]
    for i, operator in enumerate([int(x) for x in operation]):
        result = operation_map[operator](result, values[i + 1])
    return result


test = int(1, )

def increase_operator(operator: str, base: int):
    return int_to_base(int(operator, base) + 1, base, len(operator))

def int_to_base(n: int, base: int, width: int = 0) -> str:
    if not 1 < base <= 36: raise ValueError("int() base must be >= 2 and <= 36")
    char_for_int = "0123456789abcdefghijklmnopqrstuvwxyz"

    if n < base:
        return char_for_int[n].zfill(width)
    
    return (int_to_base(n // base, base) + char_for_int[n % base]).zfill(width)

calibration_result = 0

for equation in equations:
    test_value = equation[0]

    operator_combinations = 2 ** (len(equation[1]) - 1)
    operation = int_to_base(0, 2, len(equation[1]) - 1)

    for i in range(operator_combinations):
        value = calculate(equation[1], operation)
        operation = increase_operator(operation, 2)

        if test_value == value:
            calibration_result += value
            break

new_calibration_result = 0

for i, equation in enumerate(equations):
    progress = format((i+1) / len(equations), "%")
    print(f"{progress}%")
    test_value = equation[0]

    operator_combinations = 3 ** (len(equation[1]) - 1)
    operation = int_to_base(0, 3, len(equation[1]) - 1)

    for i in range(operator_combinations):
        value = calculate(equation[1], operation)
        operation = increase_operator(operation, 3)

        if test_value == value:
            new_calibration_result += value
            break



print(calibration_result)
print(new_calibration_result)