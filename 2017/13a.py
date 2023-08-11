#!/usr/bin/env python
with open('13.txt','r') as f:
    lines=f.read().strip().split('\n')

#test='''
#0: 3
#1: 2
#4: 4
#6: 4
#'''
#lines=test.strip().split('\n')

ranges=[]
sentry_positions=[]
sentry_dirs=[]
n_layers=0

for line in lines:
    index,rn=(int(v) for v in line.split(': '))
    while n_layers<=index:
        n_layers+=1
        ranges.append(0)
        sentry_positions.append(0)
        sentry_dirs.append(1)
    ranges[index]=rn
    sentry_positions[index]=0

index=-1
sev=0
while True:
    index+=1
    if index==n_layers:
        break
    rn=ranges[index]
    if rn>0 and sentry_positions[index]==0:
        sev+=index*rn
    for i in range(n_layers):
        rn=ranges[i]
        if not rn:
            continue
        p=sentry_positions[i]+sentry_dirs[i]
        if p==0 or p==rn-1:
            sentry_dirs[i]*=-1
        sentry_positions[i]=p

print(sev)

