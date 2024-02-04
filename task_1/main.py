from data import *
info_2 = info.split()

res = 0

for i in range(1,len(info_2)):
    if int(info_2[i]) > int(info_2[i-1]):
        res += 1

print(res)