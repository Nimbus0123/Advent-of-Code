from re import findall

Part1, Part2 = 0, 0
skip_multiplication = False

with open('Day3-input.txt', 'r') as file:

    for line in file:
        pattern = r"(mul\((\d+),\s*(\d+)\)|do\(\)|don't\(\))"
        matches = findall(pattern, line)

        for match in matches:
            if match[0] == "do()":
                skip_multiplication = False
            elif match[0] == "don't()":
                skip_multiplication = True

            elif match[0].startswith("mul"):
                num1, num2 = int(match[1]), int(match[2])
                Part1 += num1 * num2
                if not skip_multiplication:
                    Part2 += num1 * num2

    print(f"Part 1: {Part1}")
    print(f"Part 2: {Part2}")