safe_reports = 0

with open('Day2-input.txt', 'r') as file:
    for line in file:
        is_safe = True
        decreasing = True
        increasing = True

        line = list(map(int, line.split()))

        for i in range(1, len(line)):
            if line[i] > line[i-1]:
                decreasing = False
            elif line[i] < line[i-1]:
                increasing = False

        if increasing == False and decreasing == False:
            continue
        
        for i in range(len(line)):
            if decreasing and i > 0:
                if (line[i] > line[i-1]) or (abs(line[i] - line[i-1]) > 3) or (abs(line[i] - line[i-1]) == 0):
                    is_safe = False
            elif increasing and i > 0:
                if (line[i] < line[i-1]) or (abs(line[i] - line[i-1]) > 3) or (abs(line[i] - line[i-1]) == 0):
                    is_safe = False
        if is_safe == True:
            safe_reports += 1

print(f"Safe Reports: {safe_reports}")
