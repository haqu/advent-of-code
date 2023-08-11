#!/usr/bin/env python
n_elves=3012210

# test
#n_elves=5
#n_elves=1000000

elves=list(range(n_elves))
print(f'n_elves: {n_elves}')
i=0
while True:
    elves2=[]
    for i in range(0,n_elves,2):
        elves2.append(elves[i])
        i2=i+1
        if i2>=n_elves:
            elves2.pop(0)
            i2=0
    elves=elves2
    n_elves=len(elves)
    print(f'n_elves: {n_elves}')
    if n_elves==1:
        print(elves[0]+1)
        exit()

