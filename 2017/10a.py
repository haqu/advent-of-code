#!/usr/bin/env python
numbers=list(range(256))
with open('10.txt','r') as f:
    lengths=[int(v) for v in f.read().strip().split(',')]

# test
#numbers=list(range(5))
#lengths=[3,4,1,5]

#print(numbers)
#print(lengths)

nn=len(numbers)

i=0
skip_size=0
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
    #print(f'{l} {i}-{i2} {numbers}')
    i+=l+skip_size
    skip_size+=1
    if i>=nn:
        i-=nn

#print(numbers)
print(numbers[0]*numbers[1])

