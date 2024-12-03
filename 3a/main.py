import re

def sum_mul_expressions(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    mul_expressions = re.findall(r"mul\((\d+),(\d+)\)", content)
    
    total_sum = 0
    
    for x, y in mul_expressions:
        total_sum += int(x) * int(y)
    
    return total_sum


result = sum_mul_expressions("input.txt")

if result is not None:
    print(f"The sum of all mul(x, y) expressions is: {result}")

