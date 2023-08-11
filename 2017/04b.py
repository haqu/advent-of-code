#!/usr/bin/env python
with open('04.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#lines='''
#abcde fghij
#abcde xyz ecdab
#a ab abc abd abf abj
#iiii oiii ooii oooi oooo
#oiii ioii iioi iiio
#'''.strip().split('\n')

n=0
for line in lines:
    words=[]
    for w in line.split(' '):
        w2=''.join(list(sorted(list(w))))
        words.append(w2)
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

