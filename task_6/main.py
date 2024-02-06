from data import *

total = values.split(',')

total_count = [int(x) for x in total]

j = 0

for _ in range(81):
    for add in range(j):
        total_count.append(8)
    j = 0
    for i, fish in enumerate(total_count):
        if fish == 0:
            j += 1
            total_count[i] = 6
        else:
            total_count[i] = fish - 1

print(len(total_count))