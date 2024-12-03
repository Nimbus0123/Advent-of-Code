import re

sum = 0
dont = False

with open('Day3-input.txt', 'r') as file:

    for line in file:
        pattern = r"(mul\((\d+),\s*(\d+)\)|do\(\)|don't\(\))"
        matches = re.findall(pattern, line)

        for match in matches:
            if match[0] == 'do()':
                dont = False
            elif match[0] == "don't()":
                dont = True                
            elif dont:
                continue
            elif match[0].startswith("mul"):
                num1, num2 = int(match[1]), int(match[2])
                sum += num1 * num2

    print(f"Sum of multiplications: {sum}")