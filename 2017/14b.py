#!/usr/bin/env python
puzzle_input='uugsqrei'

# test
#puzzle_input='flqrgnkx'

def knot_hash(s):
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
    bits=''
    for i in range(16):
        res=0
        for i2 in range(16):
            res^=numbers[i*16+i2]
        bits+=format(res,'08b')
    return bits

grid={}
for i in range(128):
    line=knot_hash(f'{puzzle_input}-{i}')
    for j in range(128):
        if line[j]=='1':
            grid[(i,j)]=True

def fill_grid_groups(pos,gid):
    i,j=pos
    grid_groups[pos]=gid
    nears=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    for n in nears:
        if n[0]<0 or n[0]==128 or n[1]<0 or n[1]==128:
            continue
        if grid.get(n,False) and not grid_groups.get(n,False):
            fill_grid_groups(n,gid)

grid_groups={}
n_groups=0
for i in range(128):
    for j in range(128):
        if grid.get((i,j),False) and not grid_groups.get((i,j),False):
            n_groups+=1
            fill_grid_groups((i,j),n_groups)

print(n_groups)

