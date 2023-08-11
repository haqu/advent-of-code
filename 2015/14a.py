#!/usr/bin/env python
with open('14.txt','r') as f:
    lines=f.read().strip().split('\n')

#data='''
#Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
#Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
#'''
#lines=data.strip().split('\n')

deers=[]

import re
for line in lines:
    m=re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.',line).groups()
    name=m[0]
    speed,dur,rest=[int(v) for v in m[1:]]
    deers.append([name,speed,dur,rest,True,dur,0])
    #             0    1     2   3    4    5   6
    # d[4] - is flying
    # d[5] - time before toggling state - flying/resting
    # d[6] - total distance

countdown=2503
while countdown>0:
    countdown-=1
    for d in deers:
        if d[4]: # is flying
            d[6]+=d[1]
            d[5]-=1
            if d[5]==0:
                d[4]=False
                d[5]=d[3]
        else: # is resting
            d[5]-=1
            if d[5]==0:
                d[4]=True
                d[5]=d[2]

max_dist=0
for d in deers:
    if d[6]>max_dist:
        max_dist=d[6]

print(max_dist)

