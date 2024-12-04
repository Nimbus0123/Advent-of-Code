Part1, Part2 = 0, 0
data = []

with open("Day4-input.txt", 'r')as file:
    for line in file:
        data.append(line.strip())

for line_index, line in enumerate(data):
    for char_index, char in enumerate(line):
        if char == 'X':
            if char_index + 3 < len(line):
                if (line[char_index+1] == 'M' and 
                line[char_index+2] == 'A' and 
                line[char_index+3] == 'S'):
                    Part1 += 1
            if char_index -3 >= 0:                
                if (line[char_index-1] == 'M' and 
                line[char_index-2] == 'A' and 
                line[char_index-3] == 'S'):
                    Part1 += 1
            if line_index + 3 < len(data):
                if (data[line_index+1][char_index] == 'M' and 
                data[line_index+2][char_index] == 'A' and 
                data[line_index+3][char_index] == 'S'):
                    Part1 += 1
                if char_index -3 >= 0: 
                    if (data[line_index+1][char_index-1] == 'M' and 
                    data[line_index+2][char_index-2] == 'A' and 
                    data[line_index+3][char_index-3] == 'S'):
                        Part1 += 1
                if char_index + 3 < len(line): 
                    if (data[line_index+1][char_index+1] == 'M' and 
                    data[line_index+2][char_index+2] == 'A' and 
                    data[line_index+3][char_index+3] == 'S'):
                        Part1 += 1
            if line_index - 3 >= 0:
                if (data[line_index-1][char_index] == 'M' and 
                data[line_index-2][char_index] == 'A' and 
                data[line_index-3][char_index] == 'S'):
                    Part1 += 1
                if char_index -3 >= 0: 
                    if (data[line_index-1][char_index-1] == 'M' and 
                    data[line_index-2][char_index-2] == 'A' and 
                    data[line_index-3][char_index-3] == 'S'):
                        Part1 += 1
                if char_index + 3 < len(line): 
                    if (data[line_index-1][char_index+1] == 'M' and 
                    data[line_index-2][char_index+2] == 'A' and 
                    data[line_index-3][char_index+3] == 'S'):
                        Part1 += 1

        if char == 'A' and line_index > 0 and line_index + 1 < len(data) and char_index > 0 and char_index + 1 < len(line):
            if ((data[line_index-1][char_index+1] == 'S' and data[line_index+1][char_index-1] == 'M') or 
            (data[line_index-1][char_index+1] == 'M' and data[line_index+1][char_index-1] == 'S')):
                if ((data[line_index-1][char_index-1] == 'S' and data[line_index+1][char_index+1] == 'M') or 
                (data[line_index-1][char_index-1] == 'M' and data[line_index+1][char_index+1] == 'S')):
                    Part2 += 1

print(f"Part 1: {Part1}")
print(f"Part 2: {Part2}")
