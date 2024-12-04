list1 = []
list2 = []

with open("./input.txt", "r") as file:
    for line in file:
        line_split = line.split()
        list1.append(int(line_split[0]))
        list2.append(int(line_split[1]))

list1.sort()
list2.sort()

distance_sum = 0
similarity_score = 0

for i in range(len(list1)):
    num1 = list1[i]
    num2 = list2[i]

    distance = abs(num1 - num2)
    distance_sum += distance

    occurence = list2.count(num1)
    similarity_score += num1 * occurence

print(distance_sum)
print(similarity_score)