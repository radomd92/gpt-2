import os
import sys

q = set()
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line not in q:
            q.add(line)

q2 = q.copy()
k = [
    '-de-', '-du-', '-la-',
    '-le', '-les-', '-a-',
    '-des-',
    '-sur-', '-dans-', '-un-',
]
for line in q:
    hit = 0
    for occ in k:
        if occ in line:
            hit += 1

    if hit > 0:
        q2.remove(line)

with open(sys.argv[1], 'w') as f:
    for line in q2:
        f.write(line)
