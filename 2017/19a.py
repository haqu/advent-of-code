#!/usr/bin/env python
with open('19.txt','r') as f:
    lines=f.read().split('\n')
lines=lines[:-1]

# test
#lines=[]
#lines.append('     |          ')
#lines.append('     |  +--+    ')
#lines.append('     A  |  C    ')
#lines.append(' F---|----E|--+ ')
#lines.append('     |  |  |  D ')
#lines.append('     +B-+  +--+ ')
#lines.append('                ')

grid_w=len(lines[0])
grid_h=len(lines)
grid=[]

for line in lines:
    grid+=list(line)

x=grid.index('|')
y=0
d=(0,1)
letters=''

while True:
    x,y=(x+d[0],y+d[1])
    c=grid[x+y*grid_w]
    if c=='|' or c=='-':
        continue
    if c!='+':
        letters+=c
    bx,by=(x-d[0],y-d[1])
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    is_end=True
    for (dx,dy) in dirs:
        nx,ny=(x+dx,y+dy)
        if (nx,ny)==(bx,by):
            continue
        if grid[nx+ny*grid_w]!=' ':
            d=(dx,dy)
            is_end=False
            break
    if is_end:
        print(letters)
        exit()

