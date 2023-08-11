#!/usr/bin/env python
from hashlib import md5

salt='cuanljph'

# test
#salt='abc'

mem=[]
hashes3={}
hashes5={}
hashlen=32

n_keys=0
i=-1
while True:
    i+=1
    h=md5(f'{salt}{i}'.encode()).hexdigest()
    mem.append(h)
    for j in range(hashlen-2):
        if h[j]==h[j+1] and h[j]==h[j+2]:
            hashes3[i]=h
            if j<hashlen-4 and h[j]==h[j+3] and h[j]==h[j+4]:
                hashes5[i]=h
            break
    if i>=1000:
        i2=i-1000
        h3=hashes3.get(i2,False)
        if not h3:
            continue
        for j in range(hashlen-2):
            if h3[j]==h3[j+1] and h3[j]==h3[j+2]:
                repeated_char=h3[j]
                break
        for j in range(i2+1,i2+1001):
            h5=hashes5.get(j,False)
            if not h5:
                continue
            if repeated_char*5 in h5:
                n_keys+=1
                print(f'key: {n_keys}, index: {i2}')
                if n_keys==64:
                    print('done')
                    exit()
                break

