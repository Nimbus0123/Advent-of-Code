safe_reports = 0

with open('Day2-input.txt', 'r') as file:
    for line in file:

        line = list(map(int, line.split()))

        possible_lines = [line] + [line[:i] + line[i+1:] for i in range(len(line))]

        for variation in possible_lines:
            decreasing = True
            increasing = True
            is_safe = True

            for i in range(1, len(variation)):
                if variation[i] > variation[i-1]:
                    decreasing = False
                elif variation[i] < variation[i-1]:
                    increasing = False

            if (increasing == False) and (decreasing == False):
                continue

            for i in range(1, len(variation)):
                if decreasing:
                    if (variation[i] > variation[i-1]) or (abs(variation[i] - variation[i-1]) > 3) or (abs(variation[i] - variation[i-1]) == 0):
                        is_safe = False
                elif increasing:
                    if (variation[i] < variation[i-1]) or (abs(variation[i] - variation[i-1]) > 3) or (abs(variation[i] - variation[i-1]) == 0):
                        is_safe = False
            if is_safe == True:
                safe_reports += 1
                break

print(f"Safe Reports: {safe_reports}")