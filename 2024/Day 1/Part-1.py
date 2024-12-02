list1 = []
list2 = []
sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.split()
        first_id = int(line[0])
        second_id = int(line[1])
        list1.append(first_id)
        list2.append(second_id)

list1.sort()
list2.sort()

for index in range(len(list1)):
    difference = abs(list1[index] - list2[index])
    sum += difference

print(sum)