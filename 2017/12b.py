#!/usr/bin/env python
with open('12.txt','r') as f:
    lines=f.read().strip().split('\n')

#test='''
#0 <-> 2
#1 <-> 1
#2 <-> 0, 3, 4
#3 <-> 2, 4
#4 <-> 2, 3, 6
#5 <-> 6
#6 <-> 4, 5
#'''
#lines=test.strip().split('\n')

links={}
for line in lines:
    lp,rp,*_=line.split(' <-> ')
    n=int(lp)
    nums=[int(v) for v in rp.split(', ')]
    for n2 in nums:
        arr=links.get(n2,[])
        arr.append(n)
        links[n2]=arr

def reconstruct_path(came_from,n):
    path=[n]
    while n in came_from.keys():
        n=came_from[n]
        path.insert(0,n)
    return path

def find_path(start,end):
    open_set=[]
    open_set.append(start)
    came_from={}
    score={}
    score[start]=len(links)+1
    while open_set:
        n=open_set.pop(0)
        if n==end:
            return reconstruct_path(came_from,n)
        linked_numbers=links[n]
        for ln in linked_numbers:
            tscore=score[n]+1
            if tscore<score.get(ln,999999):
                came_from[ln]=n
                score[ln]=tscore
                if not ln in open_set:
                    open_set.insert(0,ln)
    return []

import itertools

n_groups=0
pool=list(links.keys())
while pool:
    n_groups+=1
    n=pool.pop(0)
    print(f'n: {n}, pool len: {len(pool)}')
    pool2=pool.copy()
    for n2 in pool:
        path=find_path(n,n2)
        for n in path:
            if n in pool2:
                pool2.remove(n)
    pool=pool2

print(f'n_groups: {n_groups}')

