#!/usr/bin/env python
with open('04.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#aaaaa-bbb-z-y-x-123[abxyz]
#a-b-c-d-e-f-g-h-987[abcde]
#not-a-real-room-404[oarel]
#totally-real-room-200[decoy]
#'''
#lines=data.strip().split('\n')

import re
res=0
for line in lines:
    m=re.match(r'(\S+)-(\d+)\[(\S+)\]',line).groups()
    letters=sorted(list(m[0].replace('-','')))
    sector_id=int(m[1])
    checksum=m[2]
    counts=[letters.count(c) for c in letters]
    counts=sorted(set(counts),reverse=True)
    checksum2=[]
    for count in counts:
        for c in letters:
            if letters.count(c)==count:
                if c not in checksum2:
                    checksum2.append(c)
                    if len(checksum2)==5:
                        break
        if len(checksum2)==5:
            break
    checksum2=''.join(checksum2)
    #print(checksum2)
    if checksum2==checksum:
        res+=sector_id

print(res)

