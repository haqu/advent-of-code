#!/usr/bin/env python
with open('09.txt','r') as f:
    lines=f.read().strip().split('\n')

#data='''
#London to Dublin = 464
#London to Belfast = 518
#Dublin to Belfast = 141
#'''
#lines=data.strip().split('\n')

distances={}
cities=[]

for line in lines:
    lp,rp,*_=line.split(' = ')
    d=int(rp)
    c1,c2,*_=lp.split(' to ')
    a=distances.get(c1,[])
    a.append([c2,d])
    distances[c1]=a
    a=distances.get(c2,[])
    a.append([c1,d])
    distances[c2]=a
    if not c1 in cities:
        cities.append(c1)
    if not c2 in cities:
        cities.append(c2)

def get_dist_between(c1,c2):
    a=distances.get(c1,[])
    for pair in a:
        if pair[0]==c2:
            return pair[1]
    print(f'distance between cities not found: {c1}, {c2}')
    exit()

import itertools
perms=list(itertools.permutations(cities))

max_route_dist=0
max_route_cities=None
n_cities=len(cities)

for perm in perms:
    dist=0
    for i in range(n_cities-1):
        dist+=get_dist_between(perm[i],perm[i+1])
    if dist>max_route_dist:
        max_route_dist=dist
        max_route_cities=list(perm)

print(max_route_dist)

