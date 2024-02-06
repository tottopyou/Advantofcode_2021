from data import *

total = values.split(',')

total_count = [int(x) for x in total]

j = 0

fish = [total_count.count(i) for i in range(9)]
for i in range(256):
    num = fish.pop(0)
    fish[6] += num
    fish.append(num)
    assert len(fish) == 9
print(sum(fish))