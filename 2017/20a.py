#!/usr/bin/env python
with open('20.txt','r') as f:
    lines=f.read().strip().split('\n')

particles=[]

import re
index=0
for line in lines:
    m=re.match(r'p=<(.*),(.*),(.*)>, v=<(.*),(.*),(.*)>, a=<(.*),(.*),(.*)>',line).groups()
    p=[float(n) for n in m[0:3]]
    v=[float(n) for n in m[3:6]]
    a=[float(n) for n in m[6:9]]
    particles.append((index,p,v,a))
    index+=1

min_a_sq=999999
min_v_sq=999999
for particle in particles:
    a=particle[3]
    a_sq=a[0]*a[0]+a[1]*a[1]+a[2]*a[2]
    if a_sq<min_a_sq:
        min_a_sq=a_sq
        p_id=particle[0]
        print(a_sq,p_id)

