#!/usr/bin/env python
with open('18.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#.#.#.#
#...##.
##....#
#..#...
##.#..#
#####..
#'''
#lines=data.strip().split('\n')

grid_h=len(lines)
grid_w=len(lines[0])
grid=[]

for line in lines:
    for c in line:
        grid.append(c)

grid1=grid.copy()

def grid_at(x,y):
    if x<0 or y<0 or x>=grid_w or y>=grid_h:
        return '.'
    return grid[x+y*grid_w]

def count_around(x,y):
    count=0
    for x1 in range(x-1,x+2):
        for y1 in range(y-1,y+2):
            if x1==x and y1==y:
                continue
            if grid_at(x1,y1)=='#':
                count+=1
    return count

grid[0]='#'
grid[(grid_w-1)]='#'
grid[(grid_h-1)*grid_w]='#'
grid[(grid_w-1)+(grid_h-1)*grid_w]='#'

countdown=100
while countdown>0:
    countdown-=1
    for y in range(grid_h):
        for x in range(grid_w):
            c=grid_at(x,y)
            count=count_around(x,y)
            if c=='#':
                if count>=2 and count<=3:
                    grid1[x+y*grid_w]='#'
                else:
                    grid1[x+y*grid_w]='.'
            else:
                if count==3:
                    grid1[x+y*grid_w]='#'
                else:
                    grid1[x+y*grid_w]='.'
    grid=grid1.copy()
    grid[0]='#'
    grid[(grid_w-1)]='#'
    grid[(grid_h-1)*grid_w]='#'
    grid[(grid_w-1)+(grid_h-1)*grid_w]='#'

n=0
for i in range(grid_w*grid_h):
    if grid[i]=='#':
        n+=1

print(n)

