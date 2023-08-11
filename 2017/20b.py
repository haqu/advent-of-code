#!/usr/bin/env python
with open('20.txt','r') as f:
    lines=f.read().strip().split('\n')

import re
particles=[]
for line in lines:
    m=re.match(r'p=<(.*),(.*),(.*)>, v=<(.*),(.*),(.*)>, a=<(.*),(.*),(.*)>',line).groups()
    p=[int(n) for n in m[0:3]]
    v=[int(n) for n in m[3:6]]
    a=[int(n) for n in m[6:9]]
    particles.append((p,v,a))

nparticles=len(particles)

while True:
    occupied={}
    removed=[]
    for i in range(nparticles):
        particle=particles[i]
        p=particle[0]
        v=particle[1]
        a=particle[2]
        v=(v[0]+a[0],v[1]+a[1],v[2]+a[2])
        p=(p[0]+v[0],p[1]+v[1],p[2]+v[2])
        i2=occupied.get(p,-1)
        if i2>=0:
            particle2=particles[i2]
            if not particle2 in removed:
                removed.append(particle2)
            removed.append(particle)
        else:
            occupied[p]=i
            particles[i]=(p,v,a)
    if removed:
        for p in removed:
            particles.remove(p)
        nparticles=len(particles)
        print(nparticles)

