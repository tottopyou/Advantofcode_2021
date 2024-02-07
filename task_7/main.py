from data import *

tot = values.split(',')

total = [int(x) for x in tot]
trips = {}
cost = []
y = 0

for i in range(max(total)):
    for j ,price in enumerate(total):
        x = abs(price - i)
        while x != 0:
            y += x
            x -= 1
        cost.append(y)
        y = 0
        if j == len(total)-1:
            trips[i] = sum(cost)
            cost = []

print(min(trips.values()))