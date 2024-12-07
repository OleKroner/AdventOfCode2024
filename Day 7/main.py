import sys
from multiprocessing import Pool, cpu_count

def add(a: int, b: int):
    return a + b

def multiply(a: int, b: int):
    return a * b

def concat(a: int, b: int):
    return int(f"{a}{b}")

operation_map = {
    0: add,
    1: multiply,
    2: concat,
}

def calculate(values: list[int], operation: list[int]):
    result = values[0]
    for i, operator in enumerate(operation):
        result = operation_map[operator](result, values[i + 1])
    return result

def int_to_base(n: int, base: int, width: int = 0) -> list[int]:
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")
    digits = []
    while n:
        digits.append(n % base)
        n //= base
    digits.reverse()
    return [0] * (width - len(digits)) + digits

with open("./input.txt") as file:
    equations = [
        (int(line.split(":")[0]), list(map(int, line.split(":")[1].split())))
        for line in file if line.strip()
    ]

def solve_equation(equation):
    """Solve a single equation by finding the matching operations."""
    test_value, numbers = equation
    num_operators = len(numbers) - 1
    calibration_result = 0
    new_calibration_result = 0

    # Check for 2 operations
    for op_code in range(2 ** num_operators):
        operation = int_to_base(op_code, 2, num_operators)
        if calculate(numbers, operation) == test_value:
            calibration_result += test_value
            break

    # Check for 3 operations
    for op_code in range(3 ** num_operators):
        operation = int_to_base(op_code, 3, num_operators)
        if calculate(numbers, operation) == test_value:
            new_calibration_result += test_value
            break

    return calibration_result, new_calibration_result

def display_progress(current, total, prefix="Progress", length=50):
    """Displays a simple progress bar."""
    percent = f"{100 * (current / total):.1f}"
    filled_length = int(length * current // total)
    bar = "█" * filled_length + "-" * (length - filled_length)
    sys.stdout.write(f"\r{prefix}: |{bar}| {percent}% Complete")
    sys.stdout.flush()
    if current == total:
        sys.stdout.write("\n")

if __name__ == "__main__":
    total_equations = len(equations)

    print("Processing equations...")
    with Pool(cpu_count()) as pool:
        results = []
        for i, result in enumerate(pool.imap(solve_equation, equations), start=1):
            results.append(result)
            display_progress(i, total_equations, prefix="Equation Progress")

    calibration_result = sum(r[0] for r in results)
    new_calibration_result = sum(r[1] for r in results)

    print("\n")
    print(f"Calibration Result: {calibration_result}")
    print(f"New Calibration Result: {new_calibration_result}")