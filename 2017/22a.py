#!/usr/bin/env python
with open('22.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#lines='''
#..#
##..
#...
#'''.strip().split('\n')

grid={}
mid_x=int(len(lines[0])/2)
mid_y=int(len(lines)/2)
for i in range(len(lines)):
    line=lines[i]
    for j in range(len(line)):
        x=j-mid_x
        y=i-mid_y
        if line[j]=='#':
            grid[(x,y)]=True

p=(0,0)
d=(0,-1)

directions=[(0,-1),(1,0),(0,1),(-1,0)] # cw

n_infections=0
for it in range(10000):
    if grid.get(p,False):
        di=directions.index(d)
        d=directions[(di+1)%4]
        grid[p]=False
    else:
        di=directions.index(d)
        d=directions[(di-1)%4]
        grid[p]=True
        n_infections+=1
    p=(p[0]+d[0],p[1]+d[1])

print(n_infections)

