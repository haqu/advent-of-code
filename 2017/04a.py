#!/usr/bin/env python
with open('04.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#lines='''
#aa bb cc dd ee
#aa bb cc dd aa
#aa bb cc dd aaa
#'''.strip().split('\n')

n=0
for line in lines:
    words=line.split(' ')
    words.sort()
    is_valid=True
    for i in range(len(words)-1):
        if words[i]==words[i+1]:
            is_valid=False
            break
    if not is_valid:
        continue
    n+=1
print(n)

