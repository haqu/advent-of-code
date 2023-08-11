#!/usr/bin/env python
with open('08.txt','r') as f:
    lines=f.read().strip().split('\n')

grid_w=50
grid_h=6
grid=[0]*grid_w*grid_h

def rect(w,h):
    for y in range(h):
        for x in range(w):
            grid[x+y*grid_w]=1

def rotate_row(y,n):
    row=[0]*grid_w
    for x in range(grid_w):
        x2=(x+n)%grid_w
        row[x2]=grid[x+y*grid_w]
    for x in range(grid_w):
        grid[x+y*grid_w]=row[x]

def rotate_column(x,n):
    column=[0]*grid_h
    for y in range(grid_h):
        y2=(y+n)%grid_h
        column[y2]=grid[x+y*grid_w]
    for y in range(grid_h):
        grid[x+y*grid_w]=column[y]

import re
for line in lines:
    if line.startswith('rect'):
        m=re.match(r'rect (\d+)x(\d+)',line).groups()
        rect(int(m[0]),int(m[1]))
    elif line.startswith('rotate row'):
        m=re.match(r'rotate row y=(\d+) by (\d+)',line).groups()
        rotate_row(int(m[0]),int(m[1]))
    elif line.startswith('rotate column'):
        m=re.match(r'rotate column x=(\d+) by (\d+)',line).groups()
        rotate_column(int(m[0]),int(m[1]))

chars=' █'
for y in range(grid_h):
    arr=grid[y*grid_w:(y+1)*grid_w]
    line=[chars[i] for i in arr]
    print(''.join(line))

