#!/usr/bin/env python
with open('06.txt','r') as f:
    lines=f.read().strip().split('\n')

#test
#lines=[
#'turn on 0,0 through 999,999',
#'toggle 0,0 through 999,0',
#'turn off 499,499 through 500,500',
#]

import numpy
m=numpy.empty((1000,1000))

def change(c1,c2,state):
    for x in range(c1[0],c2[0]+1):
        for y in range(c1[1],c2[1]+1):
            if state==0:
                m[x][y]=0
            elif state==1:
                m[x][y]=1
            else: #toggle
                m[x][y]=1-m[x][y]

for line in lines:
    if line.startswith('turn on'):
        c1,_,c2=line[8:].split(' ')
        c1a=[int(v) for v in c1.split(',')]
        c2a=[int(v) for v in c2.split(',')]
        change(c1a,c2a,1)
    elif line.startswith('turn off'):
        c1,_,c2=line[9:].split(' ')
        c1a=[int(v) for v in c1.split(',')]
        c2a=[int(v) for v in c2.split(',')]
        change(c1a,c2a,0)
    elif line.startswith('toggle'):
        c1,_,c2=line[7:].split(' ')
        c1a=[int(v) for v in c1.split(',')]
        c2a=[int(v) for v in c2.split(',')]
        change(c1a,c2a,2)

n=0
for x in range(1000):
    for y in range(1000):
        if m[x][y]>0:
            n+=1

print(n)

