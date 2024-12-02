safe_reports = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.split()
        for i in range(len(line)):
            line[i] = int(line[i])

        possible_lines = [line]
        possible_lines += ([line[:i] + line[i+1:] for i in range(len(line))])

        for lines in possible_lines:
            decreasing = True
            increasing = True
            is_safe = True

            for i in range(1, len(lines)):
                if lines[i] > lines[i-1]:
                    decreasing = False
                elif lines[i] < lines[i-1]:
                    increasing = False

            if (increasing == False) and (decreasing == False):
                continue

            for i in range(1, len(lines)):
                if decreasing:
                    if (lines[i] > lines[i-1]) or (abs(lines[i] - lines[i-1]) > 3) or (abs(lines[i] - lines[i-1]) == 0):
                        is_safe = False
                elif increasing:
                    if (lines[i] < lines[i-1]) or (abs(lines[i] - lines[i-1]) > 3) or (abs(lines[i] - lines[i-1]) == 0):
                        is_safe = False
            if is_safe == True:
                safe_reports += 1
                break

print(safe_reports)