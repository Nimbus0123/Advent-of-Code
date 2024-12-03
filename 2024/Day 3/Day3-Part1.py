import re

sum = 0

with open('Day3-input.txt', 'r') as file:
    for line in file:
        pattern = r'mul\((\d+),(\d+)\)'
        matches = re.findall(pattern, line, re.IGNORECASE)
        
        matches = [(int(a), int(b)) for a,b in matches]
        results = [a * b for a,b in matches]
        
        for multiplication in results:
            sum += multiplication

    print(f"Sum of multiplications: {sum}")