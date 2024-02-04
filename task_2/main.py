from data import *

info_2 = info.split('\n')

forward = 0
down = 0

for pair in info_2:
    parts = pair.split()
    if parts[0] == 'forward':
        forward += int(parts[1])
    elif parts[0] == 'down':
        down += int(parts[1])
    elif parts[0] == 'up':
        down -= int(parts[1])

print(forward * down)