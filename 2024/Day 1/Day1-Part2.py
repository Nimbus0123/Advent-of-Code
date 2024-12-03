list1 = []
list2 = []
sum = 0

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

for first_number in list1:
    for second_number in list2:
        if first_number == second_number:
            appearances += 1
    sum += first_number * appearances
    appearances = 0

print(f"Total distance: {sum}")