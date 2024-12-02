safe_reports = 0

with open('input.txt', 'r') as file:
    for line in file:
        unsafe_report = False
        decreasing = False
        increasing = False
        line = line.split()
        for i in range(len(line)):
            line[i] = int(line[i])

        if line[0] > line[1]:
            decreasing = True
        elif line[0] < line[1]:
            increasing = True
        else:
            continue
        for i in range(len(line)):
            if decreasing and i > 0:
                if (line[i] > line[i-1]) or (abs(line[i] - line[i-1]) > 3) or (abs(line[i] - line[i-1]) == 0):
                    unsafe_report = True
            elif increasing and i > 0:
                if (line[i] < line[i-1]) or (abs(line[i] - line[i-1]) > 3) or (abs(line[i] - line[i-1]) == 0):
                    unsafe_report = True
        if unsafe_report != True:
            safe_reports += 1

print(safe_reports)
