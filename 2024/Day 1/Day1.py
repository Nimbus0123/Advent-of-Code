list1 = []
list2 = []
Part1, Part2 = 0, 0

with open('Day1-input.txt', 'r') as file:
    for line in file:
        line = line.split()
        first_id = int(line[0])
        second_id = int(line[1])
        list1.append(first_id)
        list2.append(second_id)

list1.sort()
list2.sort()
appearances = 0

for index, first_number in enumerate(list1):
    for second_number in list2:
        if first_number == second_number:
            appearances += 1
    Part2 += first_number * appearances
    Part1 += abs(list1[index] - list2[index])
    appearances = 0

print(f"Part 1: {Part1}")
print(f"Part 2: {Part2}")