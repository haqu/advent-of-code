#!/usr/bin/env python
with open('10.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#value 5 goes to bot 2
#bot 2 gives low to bot 1 and high to bot 0
#value 3 goes to bot 1
#bot 1 gives low to output 1 and high to bot 0
#bot 0 gives low to output 2 and high to output 0
#value 2 goes to bot 2
#'''
#lines=data.strip().split('\n')

bots={}
outputs={}

import re
for line in lines:
    if line.startswith('value'):
        m=re.match(r'value (\d+) goes to bot (\d+)',line).groups()
        key=m[1]
        arr=bots.get(key,[])
        arr.append(int(m[0]))
        arr.sort()
        bots[key]=arr

while True:
    for line in lines:
        if line.startswith('bot'):
            m=re.match(r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)',line).groups()
            key=m[0]
            arr=bots.get(key,[])
            if len(arr)!=2:
                continue
            if arr[0]==17 and arr[1]==61:
                print(key,arr)
                exit()
            if m[1]=='bot':
                arr2=bots.get(m[2],[])
                arr2.append(arr[0])
                arr2.sort()
                bots[m[2]]=arr2
            elif m[1]=='output':
                arr2=outputs.get(m[2],[])
                arr2.append(arr[0])
                arr2.sort()
                outputs[m[2]]=arr2
            if m[3]=='bot':
                arr2=bots.get(m[4],[])
                arr2.append(arr[1])
                arr2.sort()
                bots[m[4]]=arr2
            elif m[3]=='output':
                arr2=outputs.get(m[4],[])
                arr2.append(arr[1])
                arr2.sort()
                outputs[m[4]]=arr2
            bots[key]=[]

