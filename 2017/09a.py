#!/usr/bin/env python
with open('09.txt','r') as f:
    data=f.read().strip()

# test
#data='''
#{{<ab>},{<ab>},{<ab>},{<ab>}}
#'''.strip()

index=0
def scan_group(depth):
    global index
    score=depth
    garbage=False
    while True:
        index+=1
        if data[index]=='!':
            index+=1
            continue
        if garbage:
            if data[index]=='>':
                garbage=False
        else:
            if data[index]=='<':
                garbage=True
            elif data[index]=='}':
                return score
            if data[index]=='{':
                score+=scan_group(depth+1)

print(scan_group(1))

