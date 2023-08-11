#!/usr/bin/env python
with open('22.txt','r') as f:
    lines=f.read().strip().split('\n')
n_bursts=10000000

# test
#lines='''
#..#
##..
#...
#'''.strip().split('\n')
#n_bursts=100

# 0 - clean
# 1 - weakened
# 2 - infected
# 3 - flagged

grid={}
mid_x=int(len(lines[0])/2)
mid_y=int(len(lines)/2)
for i in range(len(lines)):
    line=lines[i]
    for j in range(len(line)):
        x=j-mid_x
        y=i-mid_y
        if line[j]=='#':
            grid[(x,y)]=2

p=(0,0)
d=(0,-1)

directions=[(0,-1),(1,0),(0,1),(-1,0)] # cw

n_infections=0
for _ in range(n_bursts):
    c=grid.get(p,0)
    if c==0: # clean
        di=directions.index(d)
        d=directions[(di-1)%4] # turn left
        grid[p]=1
    elif c==1: # weakened
        grid[p]=2
        n_infections+=1
    elif c==2: # infected
        di=directions.index(d)
        d=directions[(di+1)%4] # turn right
        grid[p]=3
    elif c==3: # flagged
        di=directions.index(d)
        d=directions[(di+2)%4] # turn around
        grid[p]=0
    p=(p[0]+d[0],p[1]+d[1])

print(n_infections)

