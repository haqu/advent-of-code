#!/usr/bin/env python
from datetime import datetime

n_elves=3012210

# test
#n_elves=5
#n_elves=1000000

elves=list(range(n_elves))
ts=datetime.now().strftime('%H:%M:%S')
print(f'{ts} n_elves: {n_elves}')
i=0
while n_elves>1:
    i2=i+int(n_elves/2)
    if i2>=n_elves:
        i2-=n_elves
        i-=1
    elves.pop(i2)
    n_elves-=1
    if n_elves%10000==0:
        ts=datetime.now().strftime('%H:%M:%S')
        print(f'{ts} n_elves: {n_elves}')
    i+=1
    if i>=n_elves:
        i-=n_elves

print(elves[0]+1)

