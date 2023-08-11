#!/usr/bin/env python
with open('08.txt','r') as f:
    lines=f.read().strip().split('\n')

grid_w=50
grid_h=6

# test
#data='''
#rect 3x2
#rotate column x=1 by 1
#rotate row y=0 by 4
#rotate column x=1 by 1
#'''
#lines=data.strip().split('\n')
#grid_w=7
#grid_h=3

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
    #DEBUG
    #print('-')
    #for y in range(grid_h):
    #    print(grid[y*grid_w:(y+1)*grid_w])

n=0
for y in range(grid_h):
    for x in range(grid_w):
        if grid[x+y*grid_w]>0:
            n+=1
print(n)

