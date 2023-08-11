#!/usr/bin/env python
numbers=list(range(256))
with open('10.txt','r') as f:
    lengths=[ord(v) for v in list(f.read().strip())]

# test
#test='''
#AoC 2017
#'''.strip()
#lengths=[ord(v) for v in list(test)]

lengths+=[17,31,73,47,23]

#print(numbers)
#print(lengths)

nn=len(numbers)

i=0
skip_size=0
for _ in range(64):
    for l in lengths:
        i2=i+l
        if i2<nn:
            arr=list(reversed(numbers[i:i2]))
            numbers=numbers[:i]+arr+numbers[i2:]
        else:
            i2w=i2-nn
            arr=list(reversed(numbers[i:]+numbers[:i2w]))
            numbers2=numbers.copy()
            i3=i
            for c in arr:
                numbers2[i3]=c
                i3=(i3+1)%nn
            numbers=numbers2
        i+=l+skip_size
        skip_size+=1
        if i>=nn:
            i%=nn

dense_hash=''
for i in range(16):
    res=0
    for i2 in range(16):
        res^=numbers[i*16+i2]
    dense_hash+='{:02x}'.format(res)

print(dense_hash)

