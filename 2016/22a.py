#!/usr/bin/env python
with open('22.txt','r') as f:
    lines=f.read().strip().split('\n')

# root@ebhq-gridcenter# df -h
# Filesystem              Size  Used  Avail  Use%
# /dev/grid/node-x0-y0     92T   70T    22T   76%

lines.pop(0)
lines.pop(0)

nodes=[]

import re
for line in lines:
    m=re.match(r'/dev/grid/node-x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T +(\d+)%',line).groups()
    x=int(m[0])
    y=int(m[1])
    used=int(m[3])
    avail=int(m[4])
    nodes.append([x,y,used,avail])

#print(nodes)

n_viable=0
import itertools
perms=itertools.permutations(nodes,2)
for perm in perms:
    n1,n2=perm[0],perm[1]
    if n1[2]>0 and n2[3]>=n1[2]:
        n_viable+=1

print(n_viable)

