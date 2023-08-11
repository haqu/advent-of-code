#!/usr/bin/env python
with open('04.txt','r') as f:
    lines=f.read().strip().split('\n')

abc='abcdefghijklmnopqrstuvwxyz'
import re
for line in lines:
    m=re.match(r'(\S+)-(\d+)\[(\S+)\]',line).groups()
    name=m[0]
    letters=sorted(list(name.replace('-','')))
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
    if checksum2==checksum:
        # test
        #name='qzmt-zixmtkozy-ivhz'
        #sector_id=343
        shift=sector_id%26
        name2=''
        for c in name:
            if c=='-':
                name2+=' '
            else:
                i=abc.index(c)
                i=(i+shift)%26
                name2+=abc[i]
        if 'pole' in name2:
            print(name2)
            print(sector_id)

