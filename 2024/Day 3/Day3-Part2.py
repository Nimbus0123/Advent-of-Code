import re

sum = 0
skip_multiplication = False

with open('Day3-input.txt', 'r') as file:

    for line in file:
        pattern = r"(mul\((\d+),\s*(\d+)\)|do\(\)|don't\(\))"
        matches = re.findall(pattern, line)

        for match in matches:
            if match[0] == 'do()':
                skip_multiplication = False
            elif match[0] == "don't()":
                skip_multiplication = True                
            elif skip_multiplication:
                continue
            elif match[0].startswith("mul"):
                num1, num2 = int(match[1]), int(match[2])
                sum += num1 * num2

    print(f"Sum of multiplications: {sum}")