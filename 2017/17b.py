#!/usr/bin/env python
puzzle_input=345

# test
#puzzle_input=3

buffer=[0]
buflen=1
i=0

zero_index=0
res=0

for it in range(50000000):
    i=(i+puzzle_input)%buflen
    if i==zero_index:
        res=it+1
    buflen+=1
    i+=1

print(res)

