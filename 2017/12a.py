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

came_from={}
for line in lines:
    lp,rp,*_=line.split(' <-> ')
    n=int(lp)
    nums=[int(v) for v in rp.split(', ')]
    for n2 in nums:
        arr=came_from.get(n2,[])
        arr.append(n)
        came_from[n2]=arr

def find_zero(came_from,n,hist):
    arr=came_from[n]
    for n2 in arr:
        if n2==0:
            return True
        if n2 in hist:
            continue
        if find_zero(came_from,n2,hist+[n2]):
            return True
    return False

res=0
for n in came_from:
    if n==0 or find_zero(came_from,n,[]):
        res+=1

print(res)

