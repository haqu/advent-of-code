#!/usr/bin/env python
with open('06.txt','r') as f:
    banks=f.read().strip().split()

# test
#banks='''
#0 2 7 0
#'''.strip().split()

banks=[int(v) for v in banks]
n_banks=len(banks)
seen_states={}

print(banks)

steps=0
while True:
    i=banks.index(max(banks))
    countdown=banks[i]
    banks[i]=0
    for _ in range(countdown):
        i=(i+1)%n_banks
        banks[i]+=1
    #print(banks)
    steps+=1
    key=tuple(banks)
    if seen_states.get(key,False):
        print(banks)
        print(steps)
        exit()
    seen_states[key]=True

