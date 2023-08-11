#!/usr/bin/env python
with open('24.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#lines='''
#0/2
#2/2
#2/3
#3/4
#3/5
#0/1
#10/1
#9/10
#'''.strip().split('\n')

parts={}
for line in lines:
    lr=line.split('/')
    l,r=int(lr[0]),int(lr[1])
    arr=parts.get(l,[])
    if not r in arr:
        arr.append(r)
        parts[l]=arr
    arr=parts.get(r,[])
    if not l in arr:
        arr.append(l)
        parts[r]=arr

max_strength=0
max_len=0
def grow_bridge(port,used,strength):
    arr=parts[port]
    end=True
    for p2 in arr:
        pair1=f'{port}-{p2}'
        pair2=f'{p2}-{port}'
        if not pair1 in used and not pair2 in used:
            end=False
            grow_bridge(p2,used+[pair1,pair2],strength+port+p2)
    if end:
        global max_len
        global max_strength
        bl=int(len(used)/2)
        if bl>max_len:
            max_len=bl
            print(f'max len: {max_len}')
            max_strength=0
        if bl==max_len and strength>max_strength:
            max_strength=strength
            print(f'max strength: {max_strength}')

grow_bridge(0,[],0)

