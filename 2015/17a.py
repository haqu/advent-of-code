#!/usr/bin/env python
with open('17.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#20
#15
#5
#5
#10
#'''
#lines=data.strip().split('\n')

sizes=[]
for line in lines:
    sizes.append(int(line))
sizes.sort(reverse=True)
n_sizes=len(sizes)

mask=[0]*n_sizes

def increment(m,pos):
    if pos<0:
        return m
    if m[pos]==0:
        m[pos]=1
    else:
        m[pos]=0
        m=increment(m,pos-1)
    return m

n=0
countdown=2**n_sizes-1
while countdown>0:
    countdown-=1
    mask=increment(mask,n_sizes-1)
    total=150
    for i in range(n_sizes):
        if mask[i]==1:
            total-=sizes[i]
    if total==0:
        n+=1

print(n)

