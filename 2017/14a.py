#!/usr/bin/env python
puzzle_input='uugsqrei'

# test
#puzzle_input='flqrgnkx'

def knot_hash_ones(s):
    lengths=[ord(v) for v in list(s)]
    lengths+=[17,31,73,47,23]
    numbers=list(range(256))
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
    n_ones=0
    for i in range(16):
        res=0
        for i2 in range(16):
            res^=numbers[i*16+i2]
        for d in format(res,'04b'):
            if d=='1':
                n_ones+=1
    return n_ones

total=0
for i in range(128):
    total+=knot_hash_ones(f'{puzzle_input}-{i}')

print(total)

