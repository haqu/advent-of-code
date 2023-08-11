#!/usr/bin/env python
with open('05.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#lines='''
#0
#3
#0
#1
#-3
#'''.strip().split('\n')

jumps=[]
for line in lines:
    jumps.append(int(line))

n_jumps=len(jumps)

index=0
steps=0
while True:
    #print(index)
    if index<0 or index>n_jumps-1:
        print(steps)
        exit()
    j=jumps[index]
    jumps[index]+=1
    index+=j
    steps+=1

