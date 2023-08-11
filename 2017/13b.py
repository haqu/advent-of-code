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
n_layers=0

for line in lines:
    index,rn=(int(v) for v in line.split(': '))
    while n_layers<=index:
        n_layers+=1
        ranges.append(0)
    ranges[index]=rn

delay=0
while True:
    passed=True
    for i in range(n_layers):
        rn=ranges[i]
        if rn==0:
            continue
        v=(rn-1)*2
        passed=(delay+i)%v>0
        #print(delay,i,rn,v,passed)
        if not passed:
            break
    if passed:
        print(delay)
        exit()
    delay+=1
    #input()

