from data import *
info_2 = info.split()

res = 0
pairs = []

for i in range(0,len(info_2)-3):
    pairs.append(int(info_2[i])+int(info_2[i+1])+int(info_2[i+2]))

for i in range(1,len(pairs)):
    if int(pairs[i]) > int(pairs[i-1]):
        res += 1

print(res+1)